#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DATOS SINTÉTICOS · Laboratorio de Futuros · Chilangatón (25-oct-2026)

Genera una "encuesta" SINTÉTICA de viajes de un día entre semana en las 16 alcaldías
de la CDMX y 12 municipios conurbados del Edomex: viajes de cuidado, tiempos, pasajes
y estrés del traslado. NO son mediciones reales. El modelo se calibra para reproducir
cifras oficiales (anclas) citadas en datos/sinteticos/README.md.

Uso (desde la raíz del repo):  python3 scripts/generar_sinteticos.py
Salida: datos/sinteticos/SINTETICO_*.csv, datos/sinteticos/README.md y app/data/sintetico.js
Todo lo marcado con ➕ es supuesto del equipo.
"""
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
DIR_DATOS = RAIZ / "datos" / "sinteticos"
DIR_APP = RAIZ / "app" / "data"
SEMILLA = 2040
N_OBJETIVO = 6000          # personas sintéticas (se reparten por población)
PISO_TERRITORIO = 120      # mínimo de personas por territorio (luego se pondera)
FECHA = "2026-10-25"
UMBRAL_CAMINATA = 10       # ➕ un tramo a pie dentro de un viaje motorizado "cuenta" si dura >= 10 min
ITERACIONES = 32
AVISO = ("DATOS SINTÉTICOS · generados con scripts/generar_sinteticos.py (semilla 2040). "
         "No son mediciones reales: reproducen distribuciones oficiales (ver datos/sinteticos/README.md).")

URL = {
    "intercensal": "https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/ei/EIC2025-def_CDMX.pdf",
    "eod": "https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf",
    "micro": "https://unamglobal.unam.mx/global_revista/microbus-o-combi-transporte-publico-mas-utilizado-en-el-valle-de-mexico/",
    "estres": "https://unamglobal.unam.mx/usuarios-de-transporte-publico-se-estresan-en-sus-recorridos/",
    "metro": "https://www.nmas.com.mx/ciudad-de-mexico/subira-tarifa-metro-cdmx-2026-gobierno-anuncia-precio-para-proximo-ano/",
    "edomex": "https://www.razon.com.mx/estados/2025/10/11/aumentan-tarifas-del-transporte-publico-en-edomex-cuanto-costara-y-donde-aplica/",
    "trole": "https://www.chilango.com/noticias/transporte/trolebus-chalco-santa-martha-costo/",
    "micro_cdmx": "https://www.adn40.mx/mexico/2025-11-04/tarifa-microbus-cdmx-ha-aumentado-el-precio-del-pasaje-en-20-anos",
    "censo_cdmx": "https://www.inegi.org.mx/contenidos/programas/ccpv/2020/doc/cpv2020_pres_res_cdmx.pdf",
    "censo": "https://www.inegi.org.mx/programas/ccpv/2020/",
}

# ---------------------------------------------------------------------------
# Territorios. Población: Censo 2020 (INEGI), dato real. Centroides aproximados.
# empleo, auto y troncales son supuestos del equipo ➕ (peso relativo de empleos,
# acceso relativo a auto o moto y líneas troncales más usadas desde cada lugar).
# contorno: cdmx · c1 = municipio conurbado de primer contorno · c2 = segundo contorno ➕
# ---------------------------------------------------------------------------
T = [
    ("alvaro-obregon", "Álvaro Obregón", "CDMX", "poniente", "cdmx", 19.3587, -99.2260, 759137, 4.0, 1.10,
     [("metro", "Línea 1", .35), ("metrobus", "Línea 1", .25), ("cablebus", "Línea 3", .10), ("rtp", None, .30)]),
    ("azcapotzalco", "Azcapotzalco", "CDMX", "norte", "cdmx", 19.4869, -99.1846, 432205, 2.5, 1.0,
     [("metro", "Línea 6", .35), ("metro", "Línea 7", .20), ("metrobus", "Línea 6", .20), ("trolebus", None, .25)]),
    ("benito-juarez", "Benito Juárez", "CDMX", "centro", "cdmx", 19.3806, -99.1611, 434153, 7.0, 1.45,
     [("metro", "Línea 2", .30), ("metro", "Línea 12", .20), ("metrobus", "Línea 1", .30), ("trolebus", None, .20)]),
    ("coyoacan", "Coyoacán", "CDMX", "sur", "cdmx", 19.3285, -99.1563, 614447, 3.5, 1.20,
     [("metro", "Línea 3", .35), ("metro", "Línea 2", .20), ("metrobus", "Línea 1", .20),
      ("tren_ligero", "Tren Ligero", .10), ("trolebus", None, .15)]),
    ("cuajimalpa", "Cuajimalpa de Morelos", "CDMX", "poniente", "cdmx", 19.3570, -99.2990, 217686, 3.0, 1.30,
     [("rtp", None, .45), ("tren_interurbano", "El Insurgente", .25), ("metro", "Línea 1", .30)]),
    ("cuauhtemoc", "Cuauhtémoc", "CDMX", "centro", "cdmx", 19.4330, -99.1490, 545884, 10.0, 1.05,
     [("metro", "Línea 2", .25), ("metro", "Línea 3", .20), ("metrobus", "Línea 1", .25),
      ("metrobus", "Línea 7", .15), ("trolebus", None, .15)]),
    ("gustavo-a-madero", "Gustavo A. Madero", "CDMX", "norte", "cdmx", 19.5050, -99.1090, 1173351, 3.0, 0.85,
     [("metro", "Línea 3", .30), ("metrobus", "Línea 1", .20), ("cablebus", "Línea 1", .15),
      ("trolebus", None, .15), ("rtp", None, .20)]),
    ("iztacalco", "Iztacalco", "CDMX", "oriente", "cdmx", 19.3953, -99.0970, 404695, 1.5, 0.90,
     [("metro", "Línea 8", .30), ("metro", "Línea 9", .25), ("metrobus", "Línea 2", .25), ("trolebus", None, .20)]),
    ("iztapalapa", "Iztapalapa", "CDMX", "oriente", "cdmx", 19.3550, -99.0600, 1835486, 3.5, 0.75,
     [("metro", "Línea 8", .25), ("metro", "Línea A", .20), ("metro", "Línea 12", .15),
      ("cablebus", "Línea 2", .15), ("trolebus", None, .10), ("rtp", None, .15)]),
    ("magdalena-contreras", "La Magdalena Contreras", "CDMX", "poniente", "cdmx", 19.3030, -99.2420, 247622, 0.6, 0.95,
     [("rtp", None, .45), ("metro", "Línea 2", .25), ("metrobus", "Línea 1", .30)]),
    ("miguel-hidalgo", "Miguel Hidalgo", "CDMX", "centro", "cdmx", 19.4250, -99.2010, 414470, 8.0, 1.50,
     [("metro", "Línea 7", .30), ("metro", "Línea 2", .20), ("metrobus", "Línea 7", .25),
      ("trolebus", None, .10), ("rtp", None, .15)]),
    ("milpa-alta", "Milpa Alta", "CDMX", "sur", "cdmx", 19.1920, -99.0230, 152685, 0.3, 0.70,
     [("rtp", None, .55), ("metro", "Línea 12", .45)]),
    ("tlahuac", "Tláhuac", "CDMX", "oriente", "cdmx", 19.2860, -99.0050, 392313, 0.8, 0.75,
     [("metro", "Línea 12", .60), ("rtp", None, .25), ("trolebus", None, .15)]),
    ("tlalpan", "Tlalpan", "CDMX", "sur", "cdmx", 19.2700, -99.1800, 699928, 2.5, 1.10,
     [("tren_ligero", "Tren Ligero", .25), ("metrobus", "Línea 1", .25), ("metro", "Línea 2", .25), ("rtp", None, .25)]),
    ("venustiano-carranza", "Venustiano Carranza", "CDMX", "oriente", "cdmx", 19.4300, -99.0950, 443704, 2.5, 0.90,
     [("metro", "Línea 1", .30), ("metro", "Línea B", .20), ("metro", "Línea 5", .15),
      ("metrobus", "Línea 4", .20), ("trolebus", None, .15)]),
    ("xochimilco", "Xochimilco", "CDMX", "sur", "cdmx", 19.2570, -99.1030, 442178, 1.0, 0.85,
     [("tren_ligero", "Tren Ligero", .50), ("rtp", None, .30), ("trolebus", None, .20)]),
    ("valle-de-chalco", "Valle de Chalco Solidaridad", "Edomex", "oriente", "c2", 19.2920, -98.9420, 391731, 0.4, 0.60,
     [("trolebus", "Trolebús Chalco–Santa Martha", .65), ("metro", "Línea A", .35)]),
    ("chalco", "Chalco", "Edomex", "oriente", "c2", 19.2630, -98.8980, 400057, 0.5, 0.65,
     [("trolebus", "Trolebús Chalco–Santa Martha", .70), ("metro", "Línea A", .30)]),
    ("ixtapaluca", "Ixtapaluca", "Edomex", "oriente", "c2", 19.3180, -98.8820, 542211, 0.7, 0.70,
     [("metro", "Línea A", .55), ("trolebus", "Trolebús Chalco–Santa Martha", .45)]),
    ("la-paz", "La Paz", "Edomex", "oriente", "c1", 19.3600, -98.9600, 304088, 0.5, 0.65,
     [("metro", "Línea A", .80), ("mexibus", "Línea 3", .20)]),
    ("nezahualcoyotl", "Nezahualcóyotl", "Edomex", "oriente", "c1", 19.4000, -99.0150, 1077208, 1.5, 0.70,
     [("mexibus", "Línea 3", .35), ("metro", "Línea B", .35), ("metro", "Línea A", .30)]),
    ("chimalhuacan", "Chimalhuacán", "Edomex", "oriente", "c1", 19.4210, -98.9500, 705193, 0.6, 0.55,
     [("mexibus", "Línea 3", .75), ("metro", "Línea A", .25)]),
    ("ecatepec", "Ecatepec de Morelos", "Edomex", "norte", "c1", 19.6010, -99.0500, 1645352, 2.5, 0.75,
     [("metro", "Línea B", .40), ("mexibus", "Línea 1", .25), ("mexibus", "Línea 4", .15),
      ("mexicable", "Línea 1", .10), ("mexicable", "Línea 2", .10)]),
    ("tlalnepantla", "Tlalnepantla de Baz", "Edomex", "norte", "c1", 19.5400, -99.1950, 672202, 3.0, 1.0,
     [("suburbano", "Tren Suburbano", .30), ("metro", "Línea 6", .35), ("metro", "Línea 3", .35)]),
    ("naucalpan", "Naucalpan de Juárez", "Edomex", "poniente", "c1", 19.4780, -99.2390, 834434, 3.0, 1.10,
     [("metro", "Línea 2", .85), ("suburbano", "Tren Suburbano", .15)]),
    ("tecamac", "Tecámac", "Edomex", "norte", "c2", 19.7130, -98.9680, 547503, 0.8, 0.80,
     [("mexibus", "Línea 4", .55), ("mexibus", "Línea 1", .45)]),
    ("tultitlan", "Tultitlán", "Edomex", "norte", "c2", 19.6450, -99.1690, 516341, 1.0, 0.85,
     [("suburbano", "Tren Suburbano", .60), ("metro", "Línea 3", .40)]),
    ("cuautitlan-izcalli", "Cuautitlán Izcalli", "Edomex", "norte", "c2", 19.6460, -99.2460, 555163, 1.5, 1.0,
     [("suburbano", "Tren Suburbano", .60), ("metro", "Línea 2", .40)]),
]
TER = [dict(id=t[0], nombre=t[1], entidad=t[2], zona=t[3], contorno=t[4], lat=t[5], lon=t[6],
            poblacion=t[7], empleo=t[8], auto=t[9], troncales=t[10]) for t in T]
NT = len(TER)
IDX = {t["id"]: i for i, t in enumerate(TER)}
PERIFERIA = {i for i, t in enumerate(TER)
             if t["contorno"] == "c2" or t["id"] in ("milpa-alta", "tlahuac", "xochimilco", "iztapalapa")}

# Pesos de atracción ➕ (escuelas medias y superiores; hospitales)
PESO_ESTUDIO = {"coyoacan": 8, "gustavo-a-madero": 3, "cuauhtemoc": 3, "miguel-hidalgo": 2, "azcapotzalco": 1.5,
                "iztapalapa": 1.5, "xochimilco": 1, "tlalpan": 1, "alvaro-obregon": 1, "benito-juarez": 1.5,
                "naucalpan": 1, "cuautitlan-izcalli": 1, "tlalnepantla": 1, "nezahualcoyotl": 1, "ecatepec": .8}
PESO_SALUD = {"cuauhtemoc": 5, "tlalpan": 4, "benito-juarez": 2, "coyoacan": 2, "gustavo-a-madero": 2,
              "iztapalapa": 2, "miguel-hidalgo": 2}


def haversine(a, b):
    r = 6371.0
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"])
    dp, dl = p2 - p1, math.radians(b["lon"] - a["lon"])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


CIRCUITO = 1.35   # ➕ factor de rodeo de la red respecto a la línea recta
D = [[haversine(TER[i], TER[j]) * CIRCUITO if i != j else 3.0 for j in range(NT)] for i in range(NT)]
W_EMPLEO = [t["empleo"] for t in TER]
W_ESTUDIO = [PESO_ESTUDIO.get(t["id"], .4) for t in TER]
W_SALUD = [PESO_SALUD.get(t["id"], .5) for t in TER]
W_POB = [t["poblacion"] / 1e5 for t in TER]

# Velocidad en vehículo (km/h, incluye paradas) ➕ y espera mediana (min) ➕
VEL = {"pie": 4.5, "bici": 12, "micro": 13, "combi": 17, "rtp": 13, "trolebus": 16, "metro": 31, "metrobus": 18,
       "cablebus": 17, "tren_ligero": 23, "mexibus": 19, "mexicable": 16, "suburbano": 48, "tren_interurbano": 52,
       "auto": 21, "moto": 27}
ESPERA = {"micro": 5, "combi": 5, "rtp": 10, "trolebus": 6, "metro": 3, "metrobus": 5, "cablebus": 2,
          "tren_ligero": 5, "mexibus": 5, "mexicable": 2, "suburbano": 7, "tren_interurbano": 8}
CALLE = {"micro", "combi", "rtp", "trolebus", "auto", "moto"}
SEMICONF = {"metrobus", "mexibus"}
TP = {"micro", "combi", "rtp", "trolebus", "metro", "metrobus", "cablebus", "tren_ligero", "mexibus", "mexicable",
      "suburbano", "tren_interurbano"}
# Pasajes. Con fuente en el repo: Metro 5, micro CDMX 7.50, combi Edomex 14 (mínimo), trolebús Chalco–Santa Martha 13.
# El resto son aproximaciones ➕.
PASAJE = {"metrobus": 6, "trolebus": 2, "cablebus": 7, "tren_ligero": 3, "mexibus": 11, "mexicable": 11,
          "suburbano": 20, "tren_interurbano": 18, "rtp": 2, "micro": 7.5}


def pasaje(modo, linea, km):
    if modo == "combi":
        return 14.0 if km <= 5 else (16.0 if km <= 12 else 18.0)   # 14 real; 16 y 18 ➕
    if modo == "trolebus" and linea == "Trolebús Chalco–Santa Martha":
        return 13.0
    return float(PASAJE.get(modo, 0.0))


# ---------------------------------------------------------------------------
# Población sintética (atributos fijos; los números aleatorios se sacan una sola vez)
# ---------------------------------------------------------------------------
rng = np.random.default_rng(SEMILLA)
POB = np.array([t["poblacion"] for t in TER], float)
N_T = np.maximum(PISO_TERRITORIO, np.round(N_OBJETIVO * POB / POB.sum())).astype(int)
TERR = np.repeat(np.arange(NT), N_T)
N = len(TERR)
TASA_VIAJA = 0.74    # ➕ parte de la población de 6 años o más que viaja en un día entre semana
FACTOR = np.array([POB[t] * TASA_VIAJA / N_T[t] for t in TERR])
A = rng.random((N, 12))
NUM_U = rng.random((N, 140))
NUM_Z = rng.standard_normal((N, 140))
HETERO = rng.standard_normal(N)       # rasgo individual para el estrés
U_ESTRES = rng.random(N)

ROLES = ["ocupada", "estudiante", "hogar", "mayor"]
P_ROL = np.array([.50, .27, .15, .08])          # ➕ calibrado con los propósitos de la EOD 2017
P_MUJER = {"ocupada": .40, "estudiante": .50, "hogar": .80, "mayor": .55}   # ➕
rol = np.array(ROLES)[np.searchsorted(np.cumsum(P_ROL), A[:, 0])]
mujer = np.array([A[i, 1] < P_MUJER[rol[i]] for i in range(N)])


def edad_de(i):
    u = A[i, 2]
    r = rol[i]
    if r == "ocupada":
        return int(18 + 47 * u ** 1.15)
    if r == "estudiante":
        return int(6 + 9 * (u / .55)) if u < .55 else int(15 + 10 * (u - .55) / .45)
    if r == "hogar":
        return int(22 + 53 * u)
    return int(65 + 23 * u ** 1.4)


edad = np.array([edad_de(i) for i in range(N)])


def patron_de(i):
    u = A[i, 3]
    r = rol[i]
    if r == "ocupada":
        tasa = .21 if mujer[i] else .06          # ➕ viajes de cuidado por persona ocupada
        cuidadora = tasa / 1.30
        if u < cuidadora:
            v = u / cuidadora
            return "A2" if v < .45 else ("A3" if v < .70 else "A4")
        v = (u - cuidadora) / (1 - cuidadora)
        return "A5" if v < .091 else "A1"
    if r == "estudiante":
        return "B2" if u < .02 else ("B3" if u < .155 else "B1")
    if r == "hogar":
        return "C1" if u < .25 else ("C2" if u < .35 else ("C3" if u < .75 else ("C4s" if u < .875 else "C4o")))
    return "D1" if u < .35 else ("D2" if u < .75 else "D3")


patron = np.array([patron_de(i) for i in range(N)])
PATRONES = {
    "A1": ["trabajo", "regreso"], "A2": ["cuidado", "trabajo", "regreso"], "A3": ["trabajo", "cuidado", "regreso"],
    "A4": ["cuidado", "trabajo", "cuidado", "regreso"], "A5": ["trabajo", "compras", "regreso"],
    "B1": ["escuela", "regreso"], "B2": ["escuela", "otro", "regreso"], "B3": ["escuela", "regreso", "otro", "regreso"],
    "C1": ["cuidado", "regreso", "cuidado", "regreso"], "C2": ["cuidado", "compras", "regreso"],
    "C3": ["compras", "regreso"], "C4s": ["salud", "regreso"], "C4o": ["otro", "regreso"],
    "D1": ["salud", "regreso"], "D2": ["compras", "regreso"], "D3": ["otro", "regreso"],
}


class Flujo:
    """Números aleatorios propios de cada persona: un cambio de parámetro no revuelve a las demás."""
    __slots__ = ("U", "Z", "i", "j")

    def __init__(self, k):
        self.U, self.Z, self.i, self.j = NUM_U[k], NUM_Z[k], 0, 0

    def u(self):
        v = self.U[self.i % 140]
        self.i += 1
        return float(v)

    def z(self):
        v = self.Z[self.j % 140]
        self.j += 1
        return float(v)

    def logn(self, mediana, sigma):
        return mediana * math.exp(sigma * self.z())


def gravedad(s, origen, pesos, lam):
    w = [pesos[d] * math.exp(-D[origen][d] / lam) for d in range(NT)]
    tot = sum(w)
    u = s.u() * tot
    acc = 0.0
    for d in range(NT):
        acc += w[d]
        if u <= acc:
            return d
    return NT - 1


def t_veh(modo, km, kap, s):
    base = km / VEL[modo] * 60
    f = kap if modo in CALLE else (kap ** .6 if modo in SEMICONF else kap ** .25)
    return base * f * math.exp(.12 * s.z())


def construir_tp(s, home, d, kap, mu, m_acc):
    ter = TER[home]
    edomex = ter["entidad"] == "Edomex"
    peri = home in PERIFERIA
    local = "combi" if edomex else "micro"
    legs = [["pie", None, s.logn(m_acc * (1.15 if peri else 1.0), .45), 0.0, 0.0]]
    if d <= 5.0:
        if edomex or s.u() < min(.97, .72 * mu):
            modo, linea = local, None
        else:
            modo, linea = ("rtp", None) if s.u() < .6 else ("trolebus", None)
        legs.append([modo, linea, t_veh(modo, d, kap, s), s.logn(ESPERA[modo], .5), d])
    else:
        rem = d
        pf = {"c2": .93, "c1": .85}.get(ter["contorno"], .62 if peri else .40)
        if s.u() < min(.98, pf * mu):
            df = min(.4 * d, s.logn(3.0, .5))
            legs.append([local, None, t_veh(local, df, kap, s), s.logn(ESPERA[local], .5), df])
            legs.append(["pie", "transbordo", s.logn(4, .35), 0.0, 0.0])
            rem -= df
        u = s.u()
        acc = 0.0
        modo, linea = ter["troncales"][-1][0], ter["troncales"][-1][1]
        for m, l, p in ter["troncales"]:
            acc += p
            if u <= acc:
                modo, linea = m, l
                break
        if d > 14 and s.u() < .70:
            d1 = rem * .55
            legs.append([modo, linea, t_veh(modo, d1, kap, s), s.logn(ESPERA[modo], .5), d1])
            legs.append(["pie", "transbordo", s.logn(4.5, .35) + (3 if linea == "Línea A" else 0), 0.0, 0.0])
            m2, l2 = ("metro", "Metro (otra línea)") if s.u() < .75 else ("metrobus", "Metrobús (otra línea)")
            legs.append([m2, l2, t_veh(m2, rem - d1, kap, s), s.logn(ESPERA[m2], .5), rem - d1])
        else:
            legs.append([modo, linea, t_veh(modo, rem, kap, s), s.logn(ESPERA[modo], .5), rem])
        if s.u() < min(.6, .22 * mu):
            legs.append(["pie", "transbordo", s.logn(3, .35), 0.0, 0.0])
            legs.append(["micro", None, t_veh("micro", 1.5, kap, s), s.logn(ESPERA["micro"], .5), 1.5])
    legs.append(["pie", None, s.logn(m_acc * .9, .45), 0.0, 0.0])
    return legs


def lugar(s, k, tipo, previo, par):
    """Devuelve la actividad: territorio, ancla (casa o lejos), distancia y lugar."""
    home = TERR[k]
    if tipo == "regreso":
        return dict(t=home, ancla="casa", dl=0.0, dfh=0.0, lug=0)
    cerca_de_lejos = previo is not None and previo["ancla"] == "lejos" and tipo in ("compras", "otro")
    if cerca_de_lejos:
        return dict(t=previo["t"], ancla="lejos", dl=0.0, dfh=previo["dfh"], lug=previo["lug"] + 100, cerca=previo["lug"])
    lam_trab = par["lam_c"] if TER[home]["entidad"] == "CDMX" else par["lam_e"]
    if tipo == "trabajo":
        p_loc = par["p_local_c"] if TER[home]["entidad"] == "CDMX" else par["p_local_e"]
        if s.u() < p_loc:
            d = home        # ➕ empleo cerca de casa (comercio, servicios, trabajo informal)
        else:
            d = gravedad(s, home, W_EMPLEO, lam_trab)
    elif tipo == "escuela":
        if edad[k] < 15:
            return dict(t=home, ancla="casa", dl=s.logn(.9, .6), dfh=0.0, lug=s.u())
        if s.u() < .5:
            return dict(t=home, ancla="casa", dl=s.logn(2.5, .6), dfh=0.0, lug=s.u())
        d = gravedad(s, home, W_ESTUDIO, 15.0)
    elif tipo == "cuidado":
        if s.u() < .85:
            return dict(t=home, ancla="casa", dl=s.logn(1.1, .6), dfh=0.0, lug=s.u())
        d = gravedad(s, home, W_POB, 6.0)
    elif tipo == "compras":
        if s.u() < .85:
            return dict(t=home, ancla="casa", dl=s.logn(1.4, .6), dfh=0.0, lug=s.u())
        d = gravedad(s, home, W_EMPLEO, 10.0)
    elif tipo == "salud":
        if s.u() < .6:
            return dict(t=home, ancla="casa", dl=s.logn(2.5, .6), dfh=0.0, lug=s.u())
        d = gravedad(s, home, W_SALUD, 12.0)
    else:  # otro
        if s.u() < .7:
            return dict(t=home, ancla="casa", dl=s.logn(2.0, .7), dfh=0.0, lug=s.u())
        d = gravedad(s, home, W_EMPLEO, 10.0)
    intra = par["intra_c"] if (tipo == "trabajo" and TER[home]["entidad"] == "CDMX") else 3.0
    dist = (s.logn(intra, .6) if d == home else D[home][d] * math.exp(.15 * s.z()))
    return dict(t=d, ancla="lejos", dl=0.0, dfh=max(1.0, dist), lug=s.u() + 1)


def distancia(s, a, b):
    if a["ancla"] == "casa" and b["ancla"] == "casa":
        if a["lug"] == 0:
            return b["dl"]
        if b["lug"] == 0:
            return a["dl"]
        return (a["dl"] + b["dl"]) / 2
    if a["ancla"] == "casa":
        return max(1.0, b["dfh"] + a["dl"] * (s.u() - .5))
    if b["ancla"] == "casa":
        return max(1.0, a["dfh"] + b["dl"] * (s.u() - .5))
    if b.get("cerca") == a["lug"] or a.get("cerca") == b["lug"]:
        return s.logn(1.5, .5)
    if a["t"] == b["t"]:
        return s.logn(2.5, .5)
    return D[a["t"]][b["t"]] * math.exp(.12 * s.z())


def simular(par, detalle=False):
    personas, viajes, tramos = [], [], []
    for k in range(N):
        s = Flujo(k)
        home = TERR[k]
        ent = TER[home]["entidad"]
        kap = par["kap"]   # ➕ congestión de hora pico, igual para toda la metrópoli
        # acceso a auto o moto
        base = TER[home]["auto"]
        p_priv = min(.9, (par["a_w"] if mujer[k] else par["a_m"]) * base * (.8 if edad[k] < 15 else 1))
        priv = None
        if A[k, 4] < p_priv:
            p_moto = 0 if (mujer[k] and A[k, 6] > .25) or edad[k] < 18 else (.32 if TER[home]["zona"] in ("oriente", "norte") else .2)
            priv = "moto" if A[k, 5] < p_moto else "auto"
        actual = dict(t=home, ancla="casa", dl=0.0, dfh=0.0, lug=0)
        min_dia = costo_dia = 0.0
        transb = n_care = 0
        min_care = 0.0
        usa_tp = camina = usa_priv = False
        for n, prop in enumerate(PATRONES[patron[k]]):
            sig = lugar(s, k, prop, actual, par)
            d = distancia(s, actual, sig)
            d50 = par["d50"] * (1 + par["delta"] if mujer[k] else 1) * (1.15 if prop == "cuidado" else 1)
            x = (d - d50) / .35
            p_pie = 1 / (1 + math.exp(min(60, x)))
            if s.u() < p_pie:
                legs = [["pie", None, d / VEL["pie"] * 60 * math.exp(.1 * s.z()), 0.0, d]]
            elif priv and d > 1.0 and s.u() < .88:
                legs = [[priv, None, (3 if priv == "auto" else 2) + t_veh(priv, d, kap, s), 0.0, d]]
                usa_priv = True
            elif d < 8 and s.u() < .015:
                legs = [["bici", None, 2 + d / VEL["bici"] * 60, 0.0, d]]
            else:
                legs = construir_tp(s, home, d, kap, par["mu"], par["m_acc"])
                if sig["ancla"] == "casa" and actual["ancla"] == "lejos":
                    legs = legs[::-1]
            dur = sum(l[2] + l[3] for l in legs)
            veh = [l for l in legs if l[0] != "pie"]
            tp_legs = [l for l in legs if l[0] in TP]
            costo, metro_pagado = 0.0, False
            for l in tp_legs:
                if l[0] == "metro":
                    if not metro_pagado:
                        costo += 5.0
                        metro_pagado = True
                else:
                    costo += pasaje(l[0], l[1], l[4])
            solo_pie = len(veh) == 0
            if solo_pie or any(l[0] == "pie" and l[2] >= UMBRAL_CAMINATA for l in legs):
                camina = True
            if tp_legs:
                usa_tp = True
            transb += max(0, len(veh) - 1)
            min_dia += dur
            costo_dia += costo
            if prop == "cuidado":
                n_care += 1
                min_care += dur
            viajes.append((FACTOR[k], ent, prop, bool(tp_legs), any(l[0] in ("micro", "combi") for l in legs),
                           solo_pie, dur, k))
            if detalle:
                for j, l in enumerate(legs):
                    tramos.append(dict(persona_id=f"S{k:05d}", viaje=n + 1, tramo=j + 1, proposito=prop,
                                       de_territorio=TER[actual["t"]]["id"], a_territorio=TER[sig["t"]]["id"],
                                       modo=l[0], linea=l[1] or "", min=round(l[2], 1), espera_min=round(l[3], 1),
                                       km=round(l[4], 2), costo=round(pasaje(l[0], l[1], l[4]) if l[0] in TP and l[0] != "metro" else 0.0, 2),
                                       sintetico="SI"))
            actual = sig
        personas.append(dict(k=k, factor=FACTOR[k], ent=ent, contorno=TER[home]["contorno"], terr=home,
                             mujer=bool(mujer[k]), edad=int(edad[k]), rol=rol[k], patron=patron[k], priv=priv or "",
                             min_dia=min_dia, costo_dia=costo_dia, transb=transb, usa_tp=usa_tp, camina=camina,
                             usa_priv=usa_priv, n_care=n_care, min_care=min_care))
    return personas, viajes, tramos


def wmean(x, w):
    w = np.asarray(w, float)
    return float(np.sum(np.asarray(x, float) * w) / np.sum(w)) if np.sum(w) > 0 else float("nan")


def metricas(personas, viajes):
    P = pd.DataFrame(personas)
    V = pd.DataFrame(viajes, columns=["w", "ent", "prop", "tp", "micro", "solo_pie", "dur", "k"])
    m = {}
    trab = V[V.prop == "trabajo"]
    m["min_trab_cdmx"] = wmean(trab[trab.ent == "CDMX"].dur, trab[trab.ent == "CDMX"].w)
    m["min_trab_edomex"] = wmean(trab[trab.ent == "Edomex"].dur, trab[trab.ent == "Edomex"].w)
    m["min_trab_todos"] = wmean(trab.dur, trab.w)
    tm = trab[~trab.solo_pie]
    m["min_trab_sin_pie"] = wmean(tm.dur, tm.w)
    tc = trab[trab.ent == "CDMX"]
    m["pct30_cdmx"] = 100 * wmean(tc.dur <= 30, tc.w)
    m["camina_m"] = 100 * wmean(P[P.mujer].camina, P[P.mujer].factor)
    m["camina_h"] = 100 * wmean(P[~P.mujer].camina, P[~P.mujer].factor)
    m["priv_m"] = 100 * wmean(P[P.mujer].usa_priv, P[P.mujer].factor)
    m["priv_h"] = 100 * wmean(P[~P.mujer].usa_priv, P[~P.mujer].factor)
    vt = V[V.tp]
    m["micro"] = 100 * wmean(vt.micro, vt.w)
    for p in ["trabajo", "escuela", "cuidado", "compras", "regreso"]:
        m["prop_" + p] = 100 * wmean(V.prop == p, V.w)
    m["prop_otros"] = 100 * wmean(V.prop.isin(["salud", "otro"]), V.w)
    return m, P, V


# ---------------------------------------------------------------------------
# Calibración iterativa (cada parámetro persigue una cifra oficial)
# ---------------------------------------------------------------------------
OBJ = dict(min_trab_cdmx=54.0, min_trab_edomex=60.0, pct30_cdmx=34.1, min_trab_sin_pie=63.0,
           camina_m=71.4, camina_h=60.3, priv_m=18.2, priv_h=26.4, micro=74.1)


def calibrar():
    par = dict(kap=1.5, lam_c=8.0, lam_e=8.0, intra_c=2.5, p_local_c=.10, p_local_e=.35, d50=1.6, delta=.10, m_acc=6.2,
               a_w=.34, a_m=.40, mu=.9)
    for it in range(ITERACIONES):
        personas, viajes, _ = simular(par)
        m, _, _ = metricas(personas, viajes)
        par["lam_c"] *= (OBJ["min_trab_cdmx"] / m["min_trab_cdmx"]) ** 2.0
        par["lam_e"] *= (OBJ["min_trab_edomex"] / m["min_trab_edomex"]) ** 2.0
        par["p_local_c"] = min(.6, max(0.0, par["p_local_c"] + .008 * (OBJ["pct30_cdmx"] - m["pct30_cdmx"])))
        par["d50"] *= math.exp(.035 * (OBJ["min_trab_sin_pie"] - m["min_trab_sin_pie"]))
        prom = (m["camina_m"] + m["camina_h"]) / 2
        par["m_acc"] *= math.exp(.025 * ((OBJ["camina_m"] + OBJ["camina_h"]) / 2 - prom))
        par["delta"] = max(0.0, par["delta"] + .02 * ((OBJ["camina_m"] - OBJ["camina_h"]) - (m["camina_m"] - m["camina_h"])))
        par["a_w"] *= OBJ["priv_m"] / max(1e-6, m["priv_m"])
        par["a_m"] *= OBJ["priv_h"] / max(1e-6, m["priv_h"])
        par["mu"] *= math.exp(.03 * (OBJ["micro"] - m["micro"]))
        par["lam_c"] = min(max(par["lam_c"], 2.0), 80.0)
        par["lam_e"] = min(max(par["lam_e"], 2.0), 80.0)
        par["d50"] = min(max(par["d50"], .5), 4.0)
    return par


def calibrar_estres(P):
    """Estrés 'siempre o casi siempre' entre quienes usan transporte público (15+ años)."""
    objetivo = {"cdmx": 18.0, "c1": 24.0, "c2": 35.0}
    base = (.018 * (P.min_dia - 150) + .12 * (P.transb - 4) + .25 * P.mujer.astype(float)
            + .6 * HETERO[P.k.values])
    estres = np.zeros(len(P), bool)
    alfas = {}
    for g, obj in objetivo.items():
        sel = (P.contorno == g) & P.usa_tp & (P.edad >= 15)
        lo, hi = -8.0, 8.0
        for _ in range(60):
            a = (lo + hi) / 2
            p = 1 / (1 + np.exp(-(a + base[sel])))
            e = U_ESTRES[P.k[sel].values] < p
            share = 100 * wmean(e, P.factor[sel])
            if share < obj:
                lo = a
            else:
                hi = a
        alfas[g] = (lo + hi) / 2
        p = 1 / (1 + np.exp(-(alfas[g] + base[sel])))
        estres[sel.values] = U_ESTRES[P.k[sel].values] < p
    return estres, alfas


# ---------------------------------------------------------------------------
# Personajes (escritos a mano con la misma lógica de tiempos y pasajes; SINTÉTICOS)
# ---------------------------------------------------------------------------
def dia(inicio, items, estres):
    """items: tuplas (de, a, modo, linea, min, costo, proposito) o ("PAUSA", min) o ("HASTA", "hh:mm")."""
    h, m = map(int, inicio.split(":"))
    reloj = h * 60 + m
    tramos = []
    for it in items:
        if it[0] == "PAUSA":
            reloj += it[1]
            continue
        if it[0] == "HASTA":
            hh, mm = map(int, it[1].split(":"))
            reloj = hh * 60 + mm
            continue
        de, a, modo, linea, mins, costo, prop = it
        tramos.append(dict(sale=f"{reloj // 60:02d}:{reloj % 60:02d}", de=de, a=a, modo=modo, linea=linea,
                           min=mins, costo=costo, proposito=prop))
        reloj += mins
    veh_por_viaje, viajes, actual = [], [], []
    for t in tramos:          # un viaje termina al llegar a una actividad (trabajo, cuidado, casa...)
        actual.append(t)
        if t["a"].startswith(("Oficina", "Casa", "Hospital", "Facultad", "Zona de reparto", "CECI", "Fin")):
            viajes.append(actual)
            actual = []
    if actual:
        viajes.append(actual)
    transb = sum(max(0, len([t for t in v if t["modo"] not in ("pie", "espera")]) - 1) for v in viajes)
    return dict(tramos=tramos, total_min=sum(t["min"] for t in tramos),
                total_costo=round(sum(t["costo"] for t in tramos), 2), transbordos=transb, estres=estres)


TCS = "Trolebús Chalco–Santa Martha"
ROSA_HOY = dia("04:40", [
    ("Casa", "Casa de la vecina (deja a su nieta)", "pie", None, 4, 0, "cuidado"),
    ("Casa de la vecina", "Paradero de combis", "pie", None, 5, 0, "trabajo"),
    ("Paradero de combis", "Paradero de combis", "espera", None, 5, 0, "trabajo"),
    ("Paradero de combis", "Estación del trolebús (Valle de Chalco)", "combi", None, 9, 14, "trabajo"),
    ("Estación del trolebús", "Andén del trolebús", "espera", None, 4, 0, "trabajo"),
    ("Valle de Chalco", "Santa Martha", "trolebus", TCS, 22, 13, "trabajo"),
    ("Santa Martha (trolebús)", "Santa Martha (Metro)", "pie", None, 4, 0, "trabajo"),
    ("Santa Martha", "Pantitlán", "metro", "Línea A", 19, 5, "trabajo"),
    ("Pantitlán (Línea A)", "Pantitlán (Línea 9)", "pie", None, 6, 0, "trabajo"),
    ("Andén de la Línea 9", "Andén de la Línea 9 (deja pasar un tren lleno)", "espera", None, 4, 0, "trabajo"),
    ("Pantitlán", "Tacubaya", "metro", "Línea 9", 20, 0, "trabajo"),
    ("Tacubaya (Línea 9)", "Tacubaya (Línea 7)", "pie", None, 4, 0, "trabajo"),
    ("Tacubaya", "Polanco", "metro", "Línea 7", 6, 0, "trabajo"),
    ("Metro Polanco", "Oficina en Polanco", "micro", None, 6, 7.5, "trabajo"),
    ("HASTA", "15:10"),
    ("Oficina en Polanco", "Metro Polanco", "pie", None, 7, 0, "regreso"),
    ("Polanco", "Tacubaya", "metro", "Línea 7", 7, 5, "regreso"),
    ("Tacubaya (Línea 7)", "Tacubaya (Línea 9)", "pie", None, 4, 0, "regreso"),
    ("Tacubaya", "Pantitlán", "metro", "Línea 9", 21, 0, "regreso"),
    ("Pantitlán (Línea 9)", "Pantitlán (Línea A)", "pie", None, 6, 0, "regreso"),
    ("Pantitlán", "Santa Martha", "metro", "Línea A", 20, 0, "regreso"),
    ("Santa Martha (Metro)", "Santa Martha (trolebús)", "pie", None, 4, 0, "regreso"),
    ("Fila del trolebús", "Andén del trolebús", "espera", None, 5, 0, "regreso"),
    ("Santa Martha", "Valle de Chalco", "trolebus", TCS, 23, 13, "regreso"),
    ("Estación del trolebús", "Casa de su mamá (le lleva comida y medicinas)", "combi", None, 8, 14, "cuidado"),
    ("PAUSA", 40),
    ("Casa de su mamá", "Casa de la vecina (recoge a su nieta)", "pie", None, 5, 0, "cuidado"),
    ("Casa de la vecina", "Casa", "pie", None, 4, 0, "regreso"),
], "alto")

INTEGRADA = "Tarifa integrada del corredor ➕"
ROSA_2030 = dia("04:55", [
    ("Casa", "Paradero de la alimentadora (con su nieta)", "pie", None, 4, 0, "cuidado"),
    ("Paradero", "Paradero (Trama le avisa cuándo salir)", "espera", None, 2, 0, "cuidado"),
    ("Paradero", "Estación del trolebús (Valle de Chalco)", "combi", "Alimentadora integrada ➕", 8, 18, "cuidado"),
    ("Estación del trolebús", "CECI junto a la estación (deja a su nieta)", "pie", None, 2, 0, "cuidado"),
    ("CECI", "Andén del trolebús", "pie", None, 1, 0, "trabajo"),
    ("Andén del trolebús", "Andén del trolebús", "espera", None, 2, 0, "trabajo"),
    ("Valle de Chalco", "Santa Martha", "trolebus", TCS + " (exprés en hora pico ➕)", 16, 0, "trabajo"),
    ("Santa Martha (trolebús)", "Santa Martha (Metro)", "pie", None, 3, 0, "trabajo"),
    ("Santa Martha", "Pantitlán", "metro", "Línea A", 18, 0, "trabajo"),
    ("Pantitlán (Línea A)", "Pantitlán (Línea 9), Trama indica vagón y salida", "pie", None, 4, 0, "trabajo"),
    ("Andén de la Línea 9", "Andén (el siguiente tren viene más vacío)", "espera", None, 2, 0, "trabajo"),
    ("Pantitlán", "Tacubaya", "metro", "Línea 9", 18, 0, "trabajo"),
    ("Tacubaya (Línea 9)", "Tacubaya (Línea 7)", "pie", None, 4, 0, "trabajo"),
    ("Tacubaya", "Polanco", "metro", "Línea 7", 5, 0, "trabajo"),
    ("Metro Polanco", "Oficina en Polanco (ruta iluminada)", "pie", None, 5, 0, "trabajo"),
    ("HASTA", "15:10"),
    ("Oficina en Polanco", "Metro Polanco", "pie", None, 5, 0, "regreso"),
    ("Polanco", "Tacubaya", "metro", "Línea 7", 6, 18, "regreso"),
    ("Tacubaya (Línea 7)", "Tacubaya (Línea 9)", "pie", None, 4, 0, "regreso"),
    ("Tacubaya", "Pantitlán", "metro", "Línea 9", 18, 0, "regreso"),
    ("Pantitlán (Línea 9)", "Pantitlán (Línea A)", "pie", None, 4, 0, "regreso"),
    ("Pantitlán", "Santa Martha", "metro", "Línea A", 18, 0, "regreso"),
    ("Santa Martha (Metro)", "Santa Martha (trolebús), transbordo directo", "pie", None, 3, 0, "regreso"),
    ("Andén del trolebús", "Andén del trolebús", "espera", None, 2, 0, "regreso"),
    ("Santa Martha", "Valle de Chalco", "trolebus", TCS + " (exprés en hora pico ➕)", 16, 0, "regreso"),
    ("Estación del trolebús", "CECI junto a la estación (recoge a su nieta)", "pie", None, 2, 0, "cuidado"),
    ("CECI", "Casa de su mamá", "combi", "Alimentadora integrada ➕", 8, 0, "cuidado"),
    ("PAUSA", 40),
    ("Casa de su mamá", "Casa", "pie", None, 5, 0, "regreso"),
], "medio")

ERNESTO_HOY = dia("07:00", [
    ("Casa (Santa Cruz Meyehualco)", "Paradero", "pie", None, 9, 0, "salud"),
    ("Paradero", "Paradero", "espera", None, 7, 0, "salud"),
    ("Paradero", "Metro Constitución de 1917", "micro", None, 12, 7.5, "salud"),
    ("Acceso del Metro", "Andén (escaleras; el elevador no sirve)", "pie", None, 6, 0, "salud"),
    ("Constitución de 1917", "Chabacano", "metro", "Línea 8", 24, 0, "salud"),
    ("Chabacano (Línea 8)", "Chabacano (Línea 9), transbordo largo con escaleras", "pie", None, 9, 0, "salud"),
    ("Chabacano", "Centro Médico", "metro", "Línea 9", 5, 0, "salud"),
    ("Metro Centro Médico", "Hospital (consulta de las 8:30)", "pie", None, 9, 0, "salud"),
    ("HASTA", "12:30"),
    ("Hospital", "Metro Centro Médico", "pie", None, 10, 0, "regreso"),
    ("Centro Médico", "Chabacano", "metro", "Línea 9", 5, 0, "regreso"),
    ("Chabacano (Línea 9)", "Chabacano (Línea 8)", "pie", None, 9, 0, "regreso"),
    ("Chabacano", "Constitución de 1917", "metro", "Línea 8", 25, 0, "regreso"),
    ("Andén", "Salida (escaleras)", "pie", None, 6, 0, "regreso"),
    ("Paradero", "Paradero", "espera", None, 8, 0, "regreso"),
    ("Metro Constitución de 1917", "Paradero cercano", "micro", None, 13, 7.5, "regreso"),
    ("Paradero cercano", "Casa", "pie", None, 8, 0, "regreso"),
], "medio")

ERNESTO_2030 = dia("07:10", [
    ("Casa (Santa Cruz Meyehualco)", "Parada del RTP con rampa", "pie", None, 9, 0, "salud"),
    ("Parada", "Parada (Trama le dice cuándo salir)", "espera", None, 3, 0, "salud"),
    ("Parada", "Metro Constitución de 1917", "rtp", None, 13, 0, "salud"),
    ("Acceso del Metro", "Andén (elevador en servicio, reportado en Trama)", "pie", None, 3, 0, "salud"),
    ("Constitución de 1917", "Chabacano", "metro", "Línea 8", 24, 0, "salud"),
    ("Chabacano (Línea 8)", "Chabacano (Línea 9), ruta accesible", "pie", None, 7, 0, "salud"),
    ("Chabacano", "Centro Médico", "metro", "Línea 9", 5, 0, "salud"),
    ("Metro Centro Médico", "Hospital (consulta de las 8:30)", "pie", None, 9, 0, "salud"),
    ("HASTA", "12:30"),
    ("Hospital", "Metro Centro Médico", "pie", None, 9, 0, "regreso"),
    ("Centro Médico", "Chabacano", "metro", "Línea 9", 5, 0, "regreso"),
    ("Chabacano (Línea 9)", "Chabacano (Línea 8), ruta accesible", "pie", None, 7, 0, "regreso"),
    ("Chabacano", "Constitución de 1917", "metro", "Línea 8", 24, 0, "regreso"),
    ("Andén", "Salida (elevador)", "pie", None, 3, 0, "regreso"),
    ("Parada", "Parada del RTP", "espera", None, 4, 0, "regreso"),
    ("Metro Constitución de 1917", "Parada cercana", "rtp", None, 13, 0, "regreso"),
    ("Parada cercana", "Casa", "pie", None, 8, 0, "regreso"),
], "bajo")

VALERIA_HOY = dia("05:30", [
    ("Casa (Ecatepec)", "Paradero (calle sin luz)", "pie", None, 8, 0, "escuela"),
    ("Paradero", "Paradero", "espera", None, 6, 0, "escuela"),
    ("Paradero", "Metro Ciudad Azteca", "combi", None, 14, 14, "escuela"),
    ("Paradero de Ciudad Azteca", "Andén de la Línea B", "pie", None, 4, 0, "escuela"),
    ("Ciudad Azteca", "Guerrero", "metro", "Línea B", 36, 5, "escuela"),
    ("Guerrero (Línea B)", "Guerrero (Línea 3)", "pie", None, 6, 0, "escuela"),
    ("Guerrero", "Universidad", "metro", "Línea 3", 30, 0, "escuela"),
    ("Metro Universidad", "Facultad en CU", "pie", None, 16, 0, "escuela"),
    ("HASTA", "16:00"),
    ("Facultad en CU", "Metro Universidad", "pie", None, 16, 0, "regreso"),
    ("Universidad", "Guerrero", "metro", "Línea 3", 32, 5, "regreso"),
    ("Guerrero (Línea 3)", "Guerrero (Línea B)", "pie", None, 6, 0, "regreso"),
    ("Guerrero", "Ciudad Azteca", "metro", "Línea B", 38, 0, "regreso"),
    ("Andén de la Línea B", "Paradero de Ciudad Azteca", "pie", None, 4, 0, "regreso"),
    ("Paradero", "Paradero (fila larga)", "espera", None, 8, 0, "regreso"),
    ("Metro Ciudad Azteca", "Paradero de su colonia", "combi", None, 16, 14, "regreso"),
    ("Paradero de su colonia", "Casa (de noche, calle sin luz)", "pie", None, 8, 0, "regreso"),
], "alto")

VALERIA_2030 = dia("05:35", [
    ("Casa (Ecatepec)", "Paradero (Trama propone la calle con luz)", "pie", None, 9, 0, "escuela"),
    ("Paradero", "Paradero (Trama le avisa cuándo salir)", "espera", None, 3, 0, "escuela"),
    ("Paradero", "Metro Ciudad Azteca", "combi", None, 14, 14, "escuela"),
    ("Paradero de Ciudad Azteca", "Andén de la Línea B", "pie", None, 4, 0, "escuela"),
    ("Ciudad Azteca", "Guerrero", "metro", "Línea B", 35, 5, "escuela"),
    ("Guerrero (Línea B)", "Guerrero (Línea 3)", "pie", None, 6, 0, "escuela"),
    ("Guerrero", "Universidad", "metro", "Línea 3", 29, 0, "escuela"),
    ("Metro Universidad", "Facultad en CU", "pie", None, 16, 0, "escuela"),
    ("HASTA", "16:00"),
    ("Facultad en CU", "Metro Universidad", "pie", None, 16, 0, "regreso"),
    ("Universidad", "Guerrero", "metro", "Línea 3", 30, 5, "regreso"),
    ("Guerrero (Línea 3)", "Guerrero (Línea B)", "pie", None, 6, 0, "regreso"),
    ("Guerrero", "Ciudad Azteca", "metro", "Línea B", 36, 0, "regreso"),
    ("Andén de la Línea B", "Paradero de Ciudad Azteca", "pie", None, 4, 0, "regreso"),
    ("Paradero", "Paradero", "espera", None, 4, 0, "regreso"),
    ("Metro Ciudad Azteca", "Paradero de su colonia", "combi", None, 16, 14, "regreso"),
    ("Paradero de su colonia", "Casa (Sendero Seguro con luz)", "pie", None, 9, 0, "regreso"),
], "alto")

TONO_HOY = dia("09:00", [
    ("Casa (Nezahualcóyotl)", "Zona de reparto (Roma y Condesa)", "moto", None, 42, 30, "trabajo"),
    ("Zona de reparto", "Fin de bloque 1 (5 entregas)", "moto", None, 70, 15, "trabajo"),
    ("PAUSA", 20),
    ("Zona de reparto", "Fin de bloque 2 (6 entregas, hora de comida)", "moto", None, 85, 18, "trabajo"),
    ("PAUSA", 25),
    ("Zona de reparto", "Fin de bloque 3 (5 entregas, lluvia)", "moto", None, 80, 17, "trabajo"),
    ("PAUSA", 15),
    ("Zona de reparto", "Fin de bloque 4 (4 entregas)", "moto", None, 60, 13, "trabajo"),
    ("Zona de reparto", "Casa (Nezahualcóyotl)", "moto", None, 45, 30, "regreso"),
], "alto")

TONO_2030 = dia("09:00", [
    ("Casa (Nezahualcóyotl)", "Zona de reparto (Roma y Condesa)", "moto", None, 41, 30, "trabajo"),
    ("Zona de reparto", "Fin de bloque 1 (5 entregas, evita 3 cruces peligrosos)", "moto", None, 70, 15, "trabajo"),
    ("PAUSA", 20),
    ("Zona de reparto", "Fin de bloque 2 (6 entregas, hora de comida)", "moto", None, 83, 18, "trabajo"),
    ("PAUSA", 25),
    ("Zona de reparto", "Fin de bloque 3 (5 entregas; aviso de lluvia, ruta con menos encharcamientos)", "moto", None, 76, 17, "trabajo"),
    ("PAUSA", 15),
    ("Zona de reparto", "Fin de bloque 4 (4 entregas)", "moto", None, 60, 13, "trabajo"),
    ("Zona de reparto", "Casa (Nezahualcóyotl)", "moto", None, 44, 30, "regreso"),
], "medio")

PERSONAJES = [
    dict(id="rosa", nombre="Rosa", edad=54, territorio="valle-de-chalco",
         descripcion=("Vive en Valle de Chalco y limpia oficinas en Polanco. Cuida a su mamá y a su nieta de 6 años. "
                      "Su ruta: combi, Trolebús Chalco–Santa Martha, Línea A, Línea 9 y Línea 7."),
         dias=dict(
             hoy=ROSA_HOY, trama_2030=ROSA_2030,
             inercial_2040=dict(total_min=270, nota=("Sin integración ni cuidado junto a las estaciones: más gente en la misma red, "
                                                     "la Línea A con cortes por lluvia y hundimiento y pasajes que suben por separado. "
                                                     "Unas 4 h 30 min moviéndose (escenarios-2040.md).")),
             transformacion_2040=dict(total_min=120, nota=("Una autoridad y una tarifa metropolitanas, cuidado junto a las estaciones, "
                                                           "su mamá en la Casa de Día y una red adaptada al agua y al hundimiento: "
                                                           "unas 2 h al día (escenarios-2040.md).")),
             colapso_2040=dict(total_min=None, nota=("Pantitlán lleva 4 meses cerrado. La ruta emergente tarda tanto que Rosa deja "
                                                     "su trabajo en Polanco y vende comida en su colonia, ganando menos (escenarios-2040.md).")),
         ), sintetico=True),
    dict(id="ernesto", nombre="Don Ernesto", edad=72, territorio="iztapalapa",
         descripcion=("Vive en Iztapalapa y camina con bastón. Va cada mes a consulta al Centro Médico. "
                      "Su problema no es solo el tiempo: escaleras, elevadores que no sirven y transbordos largos."),
         dias=dict(
             hoy=ERNESTO_HOY, trama_2030=ERNESTO_2030,
             inercial_2040=dict(total_min=185, nota=("Una de cada cuatro personas tendrá 60 años o más ➕ y los elevadores siguen sin "
                                                     "mantenimiento: más tiempo y más riesgo de caída.")),
             transformacion_2040=dict(total_min=110, nota=("Red accesible de punta a punta y parte de sus consultas en un centro de salud "
                                                           "de su alcaldía.")),
             colapso_2040=dict(total_min=None, nota=("Con cortes en la Línea 8 y transbordos sin elevador, deja de ir a sus consultas.")),
         ), sintetico=True),
    dict(id="valeria", nombre="Valeria", edad=19, territorio="ecatepec",
         descripcion=("Estudia en Ciudad Universitaria y vive en Ecatepec. Sale de noche y regresa de noche; "
                      "la calle de su paradero no tiene luz."),
         dias=dict(
             hoy=VALERIA_HOY, trama_2030=VALERIA_2030,
             inercial_2040=dict(total_min=265, nota=("Más gente en la Línea B y pasajes que suben por separado en el Edomex.")),
             transformacion_2040=dict(total_min=170, nota=("Tarifa única metropolitana, Mexibús y Línea B integrados y calles con luz en "
                                                           "los primeros y últimos tramos.")),
             colapso_2040=dict(total_min=None, nota=("Por el costo y el tiempo, deja la carrera o se cambia a una escuela más cercana ➕.")),
         ), sintetico=True),
    dict(id="tono", nombre="Toño", edad=31, territorio="nezahualcoyotl",
         descripcion=("Repartidor en moto con aplicaciones. Vive en Nezahualcóyotl y reparte en la Roma y la Condesa. "
                      "Su trabajo es moverse: casi la mitad de quienes murieron en la calle en 2025 iba en moto."),
         dias=dict(
             hoy=TONO_HOY, trama_2030=TONO_2030,
             inercial_2040=dict(total_min=400, nota=("Más motos y unas 500 muertes viales al año (escenarios-2040.md).")),
             transformacion_2040=dict(total_min=330, nota=("Carriles seguros, reglas para las plataformas y menos de 200 muertes viales "
                                                           "al año (escenarios-2040.md).")),
             colapso_2040=dict(total_min=None, nota=("La red falla y crece el reparto en moto: más horas y más choques.")),
         ), sintetico=True),
]
for p in PERSONAJES:   # la gasolina de Toño no es pasaje: se marca
    if p["id"] == "tono":
        p["nota_costo"] = "En Toño, 'costo' es gasolina estimada ➕, no pasaje."


# ---------------------------------------------------------------------------
# Ejecución
# ---------------------------------------------------------------------------
def main():
    DIR_DATOS.mkdir(parents=True, exist_ok=True)
    DIR_APP.mkdir(parents=True, exist_ok=True)
    par = calibrar()
    personas, viajes, tramos = simular(par, detalle=True)
    m, P, V = metricas(personas, viajes)
    estres, alfas = calibrar_estres(P)
    P["estres"] = estres
    sel_e = lambda g: (P.contorno == g) & P.usa_tp & (P.edad >= 15)
    m["estres_cdmx"] = 100 * wmean(P[sel_e("cdmx")].estres, P[sel_e("cdmx")].factor)
    m["estres_c1"] = 100 * wmean(P[sel_e("c1")].estres, P[sel_e("c1")].factor)
    m["estres_c2"] = 100 * wmean(P[sel_e("c2")].estres, P[sel_e("c2")].factor)

    # --- calibración ---
    E, I, M = URL["eod"], URL["intercensal"], "min"
    filas = [
        ("Personas ocupadas que viven en la CDMX y llegan al trabajo en 30 min o menos", 34.1, m["pct30_cdmx"], "%",
         "INEGI, Encuesta Intercensal 2025", I),
        ("Viaje al trabajo, promedio, quienes viven en la CDMX (todos los viajes)", 54, m["min_trab_cdmx"], M,
         "INEGI, EOD 2017", E),
        ("Viaje al trabajo, promedio, quienes viven en municipios conurbados (todos los viajes)", 60, m["min_trab_edomex"], M,
         "INEGI, EOD 2017", E),
        ("Viaje al trabajo, promedio, ZMVM (todos los viajes)", 57, m["min_trab_todos"], M, "INEGI, EOD 2017", E),
        ("Viaje al trabajo sin contar viajes solo a pie, ZMVM", 63, m["min_trab_sin_pie"], M, "INEGI, EOD 2017", E),
        ("Mujeres que viajan y caminan en algún tramo", 71.4, m["camina_m"], "%", "INEGI, EOD 2017", E),
        ("Hombres que viajan y caminan en algún tramo", 60.3, m["camina_h"], "%", "INEGI, EOD 2017", E),
        ("Mujeres que viajan y usan transporte privado", 18.2, m["priv_m"], "%", "INEGI, EOD 2017", E),
        ("Hombres que viajan y usan transporte privado", 26.4, m["priv_h"], "%", "INEGI, EOD 2017", E),
        ("Viajes en transporte público que usan micro o combi en algún tramo", 74.1, m["micro"], "%",
         "UNAM Global con la EOD 2017", URL["micro"]),
        ("Viajes para llevar o recoger a alguien (cuidado)", 6.6, m["prop_cuidado"], "%", "INEGI, EOD 2017", E),
        ("Viajes para ir al trabajo", 22.0, m["prop_trabajo"], "%", "INEGI, EOD 2017", E),
        ("Viajes para ir a estudiar", 11.9, m["prop_escuela"], "%", "INEGI, EOD 2017", E),
        ("Viajes de compras", 6.5, m["prop_compras"], "%", "INEGI, EOD 2017", E),
        ("Viajes para regresar al hogar", 47.3, m["prop_regreso"], "%", "INEGI, EOD 2017", E),
        ("Viajes sociales, trámites, salud y otros", 5.7, m["prop_otros"], "%", "INEGI, EOD 2017", E),
        ("Estrés del traslado siempre o casi siempre: viven en la CDMX", 18, m["estres_cdmx"], "%",
         "UNAM Global (estudio exploratorio)", URL["estres"]),
        ("Estrés del traslado: municipios conurbados (primer contorno ➕)", 24, m["estres_c1"], "%",
         "UNAM Global (estudio exploratorio)", URL["estres"]),
        ("Estrés del traslado: Estado de México (segundo contorno ➕)", 35, m["estres_c2"], "%",
         "UNAM Global (estudio exploratorio)", URL["estres"]),
    ]
    calib = [dict(indicador=a, oficial=b, sintetico=round(c, 1), unidad=u, fuente=f, url=l,
                  ok=bool(abs(c - b) <= 1.5)) for a, b, c, u, f, l in filas]

    # --- personas y tramos ---
    P["persona_id"] = [f"S{k:05d}" for k in P.k]
    P["territorio_id"] = [TER[t]["id"] for t in P.terr]
    P["zona"] = [TER[t]["zona"] for t in P.terr]
    P["sexo"] = np.where(P.mujer, "mujer", "hombre")
    personas_csv = pd.DataFrame(dict(
        persona_id=P.persona_id, territorio_id=P.territorio_id, entidad=P.ent, zona=P.zona, contorno=P.contorno,
        sexo=P.sexo, edad=P.edad, rol=P.rol, cadena=P.patron, acceso_auto_moto=P.priv, factor=P.factor.round(1),
        min_dia=P.min_dia.round(1), pasajes_dia=P.costo_dia.round(2), transbordos_dia=P.transb,
        usa_transporte_publico=np.where(P.usa_tp, "SI", "NO"), camina_algun_tramo=np.where(P.camina, "SI", "NO"),
        viajes_cuidado=P.n_care, min_cuidado=P.min_care.round(1),
        estres_siempre_o_casi=np.where(P.usa_tp & (P.edad >= 15), np.where(P.estres, "SI", "NO"), ""),
        sintetico="SI"))
    personas_csv.to_csv(DIR_DATOS / "SINTETICO_personas.csv", index=False, encoding="utf-8")
    pd.DataFrame(tramos).to_csv(DIR_DATOS / "SINTETICO_tramos.csv", index=False, encoding="utf-8")

    # --- territorios e índice de pobreza de tiempo ---
    V["terr"] = [TERR[k] for k in V.k]
    filas_t = []
    for i, t in enumerate(TER):
        p = P[P.terr == i]
        a15 = p[p.edad >= 15]
        trab = V[(V.terr == i) & (V.prop == "trabajo")]
        cuid = a15[a15.n_care > 0]
        tpu = a15[a15.usa_tp]
        filas_t.append(dict(
            id=t["id"], nombre=t["nombre"], entidad=t["entidad"], zona=t["zona"], contorno=t["contorno"],
            lat=t["lat"], lon=t["lon"], poblacion=t["poblacion"], n_muestra=len(p),
            min_trabajo=round(float(trab.dur.mean()), 1),
            pct_30min=round(100 * float((trab.dur <= 30).mean()), 1),
            pct_mas_2h=round(100 * float((a15.min_dia > 120).mean()), 1),
            pct_cuidadoras=round(100 * float((a15.n_care > 0).mean()), 1),
            min_cuidado_extra=round(float(cuid.min_care.mean()) if len(cuid) else 0.0, 1),
            gasto_diario=round(float(tpu.costo_dia.mean()), 1),
            pct_estres=round(100 * float(tpu.estres.mean()), 1),
            pct_camina_mujeres=round(100 * float(p[p.mujer].camina.mean()), 1),
            pct_camina_hombres=round(100 * float(p[~p.mujer].camina.mean()), 1),
            pct_usa_tp=round(100 * float(a15.usa_tp.mean()), 1),
        ))
    TT = pd.DataFrame(filas_t)
    carga = TT.pct_cuidadoras / 100 * TT.min_cuidado_extra
    carga_n = 100 * carga / carga.max()
    gasto_n = 100 * TT.gasto_diario / TT.gasto_diario.max()
    bruto = .35 * TT.pct_mas_2h + .25 * (100 - TT.pct_30min) + .20 * carga_n + .20 * gasto_n
    TT["ipt_bruto"] = bruto.round(1)
    TT["ipt"] = (100 * (bruto - bruto.min()) / (bruto.max() - bruto.min())).round(0).astype(int)
    TT["sintetico"] = "SI"
    TT.to_csv(DIR_DATOS / "SINTETICO_territorios.csv", index=False, encoding="utf-8")
    pd.DataFrame([dict(indicador=c["indicador"], oficial=c["oficial"], valor_sintetico=c["sintetico"],
                       diferencia=round(c["sintetico"] - c["oficial"], 1), unidad=c["unidad"], fuente=c["fuente"],
                       url=c["url"], ok=c["ok"], sintetico="SI") for c in calib]).to_csv(
        DIR_DATOS / "SINTETICO_calibracion.csv", index=False, encoding="utf-8")

    # --- app/data/sintetico.js ---
    territorios_js = []
    for r in TT.to_dict("records"):
        r = {k: (v.item() if hasattr(v, "item") else v) for k, v in r.items()}
        r["sintetico"] = True
        territorios_js.append(r)
    data = dict(
        aviso=AVISO, semilla=SEMILLA, generado=FECHA,
        muestra=dict(personas=int(len(P)), tramos=int(len(tramos))),
        territorios=territorios_js, personajes=PERSONAJES, calibracion=calib,
        metodo=dict(
            ipt=("IPT = reescala 0–100 de [0.35·(% que pasa más de 2 h al día moviéndose) + 0.25·(% que NO llega al trabajo "
                 "en 30 min) + 0.20·(carga de cuidado normalizada) + 0.20·(gasto en pasajes normalizado)]. 0 = el territorio "
                 "con menos pobreza de tiempo de los 28; 100 = el que más."),
            carga_cuidado="(% que hace viajes de cuidado) × (minutos diarios en esos viajes), normalizado a 100 = máximo.",
            umbral_caminata_min=UMBRAL_CAMINATA,
            parametros={k: round(v, 3) for k, v in par.items()},
            alfas_estres={k: round(v, 3) for k, v in alfas.items()},
        ),
    )
    js = ("// " + AVISO + "\n// Generado por scripts/generar_sinteticos.py. No editar a mano.\n"
          "window.SINTETICO = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")
    (DIR_APP / "sintetico.js").write_text(js, encoding="utf-8")

    escribir_readme(calib, TT, par, len(P), len(tramos))
    print(f"Personas: {len(P)} · tramos: {len(tramos)}")
    for c in calib:
        print(f"{'OK ' if c['ok'] else 'XX '} {c['indicador'][:70]:70s} oficial {c['oficial']:>6} sintético {c['sintetico']:>6}")
    for p in PERSONAJES:
        print(p["id"], {k: (v.get("total_min"), v.get("total_costo")) for k, v in p["dias"].items()})


def escribir_readme(calib, TT, par, n_p, n_t):
    tabla = "\n".join(
        f"| {c['indicador']} | {c['oficial']} {c['unidad']} | {c['sintetico']} {c['unidad']} | "
        f"{c['sintetico'] - c['oficial']:+.1f} | {'✅' if c['ok'] else '⚠️'} | [{c['fuente']}]({c['url']}) |" for c in calib)
    top = TT.sort_values("ipt", ascending=False).head(8)
    tabla_t = "\n".join(f"| {r.nombre} | {r.entidad} | {r.ipt} | {r.min_trabajo} | {r.pct_30min} | {r.pct_mas_2h} | "
                        f"{r.pct_cuidadoras} | {r.gasto_diario} | {r.pct_estres} |" for r in top.itertuples())
    txt = f"""# ⚠️ DATOS SINTÉTICOS: no son mediciones

**Estos archivos NO vienen de una encuesta real.** Son una población inventada por computadora para poder construir y probar el prototipo mientras no exista la encuesta de viajes de cuidado y estrés del traslado. Los números están **calibrados** para parecerse a las cifras oficiales que sí existen (tabla de abajo), pero **ninguna fila es una persona real** y **no se deben citar como dato**.

- Cada archivo empieza con `SINTETICO_` y cada fila trae la columna `sintetico = SI`.
- En la app, todo lo que viene de aquí lleva la etiqueta **SINTÉTICO**.
- Se regeneran igual siempre (semilla {SEMILLA}): `python3 scripts/generar_sinteticos.py`.
- Lo marcado con ➕ es supuesto del equipo.

## Qué hay aquí

| Archivo | Qué es | Columnas principales |
| --- | --- | --- |
| `SINTETICO_personas.csv` | {n_p:,} personas que viajan en un día entre semana | `persona_id`, `territorio_id`, `entidad`, `zona`, `contorno`, `sexo`, `edad`, `rol` (ocupada, estudiante, hogar, mayor), `cadena` (patrón del día), `acceso_auto_moto`, `factor` (cuántas personas reales representa), `min_dia`, `pasajes_dia`, `transbordos_dia`, `usa_transporte_publico`, `camina_algun_tramo`, `viajes_cuidado`, `min_cuidado`, `estres_siempre_o_casi`, `sintetico` |
| `SINTETICO_tramos.csv` | {n_t:,} tramos: un renglón por cada pedazo de cada viaje | `persona_id`, `viaje`, `tramo`, `proposito`, `de_territorio`, `a_territorio`, `modo`, `linea`, `min` (en movimiento), `espera_min`, `km`, `costo` (pasaje del tramo; el Metro se cobra una vez por viaje), `sintetico` |
| `SINTETICO_territorios.csv` | 16 alcaldías y 12 municipios con sus indicadores y el índice | `ipt`, `ipt_bruto`, `min_trabajo`, `pct_30min`, `pct_mas_2h`, `pct_cuidadoras`, `min_cuidado_extra`, `gasto_diario`, `pct_estres`, `pct_camina_mujeres`, `pct_camina_hombres`, `pct_usa_tp`, `n_muestra`, `poblacion` (real, Censo 2020) |
| `SINTETICO_calibracion.csv` | Comparación oficial contra sintético | `indicador`, `oficial`, `valor_sintetico`, `diferencia`, `unidad`, `fuente`, `url`, `ok`, `sintetico` |
| `../../app/data/sintetico.js` | Lo mismo, resumido para la app (`window.SINTETICO`), con 4 personajes | — |

## Cómo se hizo, en palabras simples

1. **Repartimos {n_p:,} personas** entre 16 alcaldías y 12 municipios conurbados según su población real ([Censo 2020]({URL['censo']})). Los territorios chicos tienen al menos {PISO_TERRITORIO} personas, y el `factor` corrige ese reparto.
2. **A cada persona le damos un rol** (ocupada, estudiante, hogar o mayor), un sexo, una edad y un **patrón de día**: por ejemplo casa → dejar a alguien → trabajo → casa. Las proporciones de roles y patrones están hechas para que los propósitos de los viajes queden como en la EOD 2017.
3. **Cada actividad tiene un lugar.** El trabajo y la escuela se eligen con un modelo de gravedad: más probable si hay muchos empleos o escuelas y si queda cerca. El cuidado, las compras y la salud suelen estar cerca de casa.
4. **Cada viaje se arma por tramos:** caminar a la parada, esperar, micro o combi, transbordo, Metro u otra troncal y caminar al destino. Cada modo tiene su velocidad y su espera ➕, y cada tramo su pasaje.
5. **Calibramos:** con una congestión fija de hora pico ➕, el programa ajusta 9 perillas (qué tan lejos queda el empleo, caminata, acceso a auto o moto, uso de micro) durante {ITERACIONES} vueltas, hasta que los resultados se parecen a las cifras oficiales.
6. **Estrés:** quien usa transporte público tiene más probabilidad de estresarse si viaja más tiempo y hace más transbordos ➕. Ajustamos el nivel de cada grupo para que coincida con el estudio de la UNAM.

## Anclas reales (lo que el modelo debe reproducir) y calibración

Tolerancia: ±1.5 puntos o ±1.5 minutos.

| Indicador | Oficial | Sintético | Diferencia | ¿Cumple? | Fuente |
| --- | --- | --- | --- | --- | --- |
{tabla}

**Ojo con dos anclas:**

- **34.1%** viene de la Encuesta Intercensal 2025 y los minutos al trabajo de la EOD 2017: son encuestas y años distintos. Aquí conviven en la misma población a propósito.
- **Estrés:** el estudio de la UNAM es **exploratorio**, no representativo. Además, interpretamos ➕ "municipios conurbados" como los de primer contorno, a menos de unos 20 km del Zócalo (Nezahualcóyotl, Tlalnepantla, Naucalpan, La Paz, Ecatepec y Chimalhuacán), y "Estado de México" como los de segundo contorno (Valle de Chalco, Chalco, Ixtapaluca, Tecámac, Tultitlán y Cuautitlán Izcalli).

**Pasajes usados.**

- Con fuente en el repo:
  - [Metro, 5 pesos]({URL['metro']})
  - [micro de la CDMX, 7.50]({URL['micro_cdmx']})
  - [combi del Edomex, 14 pesos mínimo]({URL['edomex']})
  - [Trolebús Chalco–Santa Martha, 13 pesos]({URL['trole']})
- Aproximados ➕:
  - Metrobús, 6
  - trolebús de la CDMX, 2
  - Cablebús, 7
  - Tren Ligero, 3
  - Mexibús y Mexicable, 11
  - Suburbano, 20
  - El Insurgente, 18
  - RTP, 2
  - combi del Edomex de 5 a 12 km, 16; de más de 12 km, 18

## Índice de pobreza de tiempo (IPT)

Fórmula abierta, para que cualquiera la discuta:

```
IPT_bruto = 0.35 · (% de personas de 15+ que pasan más de 2 h al día moviéndose)
          + 0.25 · (% de personas ocupadas que NO llegan al trabajo en 30 min)
          + 0.20 · carga de cuidado normalizada   [ (% que hace viajes de cuidado) × (min diarios en esos viajes); 100 = el máximo ]
          + 0.20 · gasto en pasajes normalizado   [ pesos diarios entre quienes usan transporte público; 100 = el máximo ]
IPT = 100 · (IPT_bruto − mínimo) / (máximo − mínimo)    → 0 = el territorio con menos pobreza de tiempo de los 28; 100 = el que más
```

Los pesos (0.35, 0.25, 0.20, 0.20) son una propuesta ➕ del equipo. El piloto los validaría con las propias usuarias.

**Los 8 territorios con más pobreza de tiempo (sintético):**

| Territorio | Entidad | IPT | Min al trabajo | % llega en 30 min | % más de 2 h | % cuida | Pasajes al día ($) | % estrés |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{tabla_t}

## Supuestos del equipo ➕

- **Roles:** ocupada 50%, estudiante 27%, hogar 15% y mayor 8%. Proporción de mujeres en cada rol: 40%, 50%, 80% y 55%.
- **Cuidado:**
  - Las mujeres cuidan mucho más: 0.21 viajes de cuidado por mujer ocupada contra 0.06 por hombre ocupado.
  - Una cuarta parte de quienes se dedican al hogar lleva y recoge a alguien dos veces al día.
  - Con eso, los viajes de cuidado quedan en 6.6% del total, como en la EOD.
- **Tiempos y costos:** velocidades y esperas por modo, factor de rodeo de la red de 1.35, pesos de empleo, escuelas y hospitales por territorio, acceso a auto o moto por territorio, y líneas troncales de cada lugar.
- **Caminata:** un tramo a pie dentro de un viaje en vehículo cuenta si dura {UMBRAL_CAMINATA} minutos o más. Los viajes solo a pie siempre cuentan.
- **Empleo cerca de casa:** en el Edomex, 35% de quienes trabajan lo hace en su propio municipio; en la CDMX, esa parte se calibra.
- **Población que viaja:** 74% de la población.
- **Personajes:** Rosa, Don Ernesto, Valeria y Toño están escritos a mano con la misma lógica de tiempos y pasajes. Son inventados.
  - Los días `trama_2030` suponen el piloto ➕: tarifa integrada del corredor de 18 pesos por viaje, alimentadoras con horario coordinado, trolebús exprés en hora pico, CECI junto a la estación y avisos de la app.

## Límites

- No hay geografía fina: cada territorio es un punto (su centroide) y las distancias son en línea recta por 1.35.
- Un solo día típico entre semana: no hay fines de semana, lluvia ni cortes. Los cortes se simulan en la app, no aquí.
- No hay ingreso ni hogares completos: el acceso a auto es una aproximación por territorio.
- Solo hay 12 de los municipios conurbados y no se modela Hidalgo.
- La calibración asegura promedios y porcentajes, no la forma completa de las distribuciones ni las cifras por alcaldía. **Las diferencias entre territorios son plausibles, no medidas.**

## Cómo se reemplazan por datos reales

| Hueco sintético | Dato real que lo reemplaza | Cuándo (ruta de la propuesta) |
| --- | --- | --- |
| Viajes de cuidado por sexo, cadenas del día y estrés | **Encuesta del piloto:** 300 usuarias del corredor Chalco–Santa Martha y Línea A, con las mismas columnas de estos archivos | 0–3 meses |
| Tiempos puerta a puerta por colonia | **Validaciones anónimas de la tarjeta MI** y del trolebús (agregadas, sin datos personales) | 3–12 meses |
| Toda la población y los propósitos | **Nueva Encuesta Origen-Destino** con viajes de cuidado por sexo; la última es de 2017 | 12–24 meses |
| Red y paradas | GTFS oficial de SEMOVI (ya disponible) | Ya |

**Regla:** cuando llegue un dato real, se reemplaza la columna y se quita la marca `sintetico` **solo** en esa columna. Nunca se mezclan sin marca.
"""
    (DIR_DATOS / "README.md").write_text(txt, encoding="utf-8")


if __name__ == "__main__":
    main()
