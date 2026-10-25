"""Prepara app/data/red.js (window.RED) con la red REAL de transporte masivo.

Fuente: capas del chat "Mapa de movilidad" (OpenStreetMap, ODbL, y GTFS de SEMOVI
vía Mobility Database para las líneas que faltaban en OSM). Solo se toman líneas,
estaciones, alcaldías y el límite de la CDMX.

Uso:  python3 app/tools/preparar_red.py <carpeta mapa/web/data> app/data/red.js
"""
import json, math, sys, unicodedata
from pathlib import Path

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "../innovafest_proyecto_morelos/mapa/web/data")
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "app/data/red.js")

SISTEMA = {"metro": "Metro", "metrobus": "Metrobús", "trolebus": "Trolebús", "cablebus": "Cablebús",
           "tren_ligero": "Tren Ligero", "tren": "Tren", "mexibus": "Mexibús", "mexicable": "Mexicable"}

def dp(pts, tol):
    """Douglas-Peucker."""
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    norm = math.hypot(dx, dy) or 1e-12
    dmax, idx = 0.0, 0
    for i in range(1, len(pts) - 1):
        x0, y0 = pts[i]
        d = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / norm
        if d > dmax:
            dmax, idx = d, i
    if dmax > tol:
        a = dp(pts[: idx + 1], tol)
        b = dp(pts[idx:], tol)
        return a[:-1] + b
    return [pts[0], pts[-1]]

def r5(p):
    return [round(p[0], 5), round(p[1], 5)]

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    for w in ["metro ", "cetram ", "estacion ", "terminal "]:
        s = s.replace(w, "")
    return s.replace("santa martha", "santa marta").strip()

lin = json.load(open(SRC / "transporte_lineas.json"))
lineas = []
for f in lin["features"]:
    p, g = f["properties"], f["geometry"]
    parts = g["coordinates"] if g["type"] == "MultiLineString" else [g["coordinates"]]
    coords = [[r5(q) for q in dp(part, 0.00012)] for part in parts if len(part) > 1]
    sis = p["m"]
    nombre = p.get("n", "")
    if sis == "tren":
        nombre = p.get("n", "")
    lineas.append({"id": f"{sis}-{p['r']}", "nombre": nombre, "ruta": p["r"], "sistema": sis,
                   "sistema_nombre": SISTEMA.get(sis, sis), "color": p.get("c", "#888"),
                   "destinos": p.get("d"), "km": p.get("km"), "coords": coords})

est = json.load(open(SRC / "transporte_estaciones.json"))
estaciones = []
for i, f in enumerate(est["features"]):
    p = f["properties"]
    lon, lat = f["geometry"]["coordinates"][:2]
    estaciones.append({"id": f"e{i}", "nombre": p["n"], "sistema": p["m"], "lineas": [x.strip() for x in str(p.get("l", "")).split("·") if x.strip()],
                       "color": p.get("c"), "lon": round(lon, 5), "lat": round(lat, 5)})

# Nodos de transbordo: misma estación (nombre normalizado) a menos de 600 m, o distinta a < 180 m
def dist_m(a, b):
    kx = 111320 * math.cos(math.radians(19.4))
    return math.hypot((a["lon"] - b["lon"]) * kx, (a["lat"] - b["lat"]) * 110540)

grupos = []
for e in estaciones:
    for gr in grupos:
        c = gr[0]
        d = dist_m(e, c)
        if (norm(e["nombre"]) == norm(c["nombre"]) and d < 600) or d < 180:
            gr.append(e); break
    else:
        grupos.append([e])
nodos = []
for gr in grupos:
    lineas_set = sorted({f"{x['sistema']}-{l}" for x in gr for l in x["lineas"]})
    if len(lineas_set) >= 2:
        nodos.append({"nombre": gr[0]["nombre"], "lon": round(sum(x["lon"] for x in gr) / len(gr), 5),
                      "lat": round(sum(x["lat"] for x in gr) / len(gr), 5), "lineas": lineas_set,
                      "sistemas": sorted({x["sistema"] for x in gr})})

alc = json.load(open(SRC / "alcaldias.json"))
alcaldias = []
for f in alc["features"]:
    g = f["geometry"]
    rings = g["coordinates"] if g["type"] == "Polygon" else [r for poly in g["coordinates"] for r in poly]
    alcaldias.append({"nombre": f["properties"]["n"],
                      "centro": json.loads(f["properties"]["c"]) if isinstance(f["properties"].get("c"), str) else f["properties"].get("c"),
                      "coords": [[r5(q) for q in dp(r, 0.0006)] for r in rings[:1]]})
lim = json.load(open(SRC / "limite.json"))
g = lim["features"][0]["geometry"]
limite = [[r5(q) for q in dp(r, 0.0006)] for r in (g["coordinates"][:1] if g["type"] == "Polygon" else [g["coordinates"][0][0]])]

RED = {
    "atribucion": "© colaboradores de OpenStreetMap (ODbL) · GTFS de SEMOVI vía Mobility Database",
    "corte": "2026-10-25",
    "bbox": [-99.37, 19.03, -98.84, 19.74],
    "lineas": lineas, "estaciones": estaciones, "nodos": nodos,
    "alcaldias": alcaldias, "limite": limite,
}
txt = "/* Red REAL de transporte masivo de la ZMVM. " + RED["atribucion"] + ". Generado por app/tools/preparar_red.py */\nwindow.RED = " + json.dumps(RED, ensure_ascii=False, separators=(",", ":")) + ";\n"
OUT.write_text(txt, encoding="utf-8")
print(OUT, f"{len(txt)/1024:.0f} KB", len(lineas), "líneas", len(estaciones), "estaciones", len(nodos), "nodos")
