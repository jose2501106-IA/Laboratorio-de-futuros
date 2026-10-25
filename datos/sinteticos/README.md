# ⚠️ DATOS SINTÉTICOS: no son mediciones

**Estos archivos NO vienen de una encuesta real.** Son una población inventada por computadora para poder construir y probar el prototipo mientras no exista la encuesta de viajes de cuidado y estrés del traslado. Los números están **calibrados** para parecerse a las cifras oficiales que sí existen (tabla de abajo), pero **ninguna fila es una persona real** y **no se deben citar como dato**.

- Cada archivo empieza con `SINTETICO_` y cada fila trae la columna `sintetico = SI`.
- En la app, todo lo que viene de aquí lleva la etiqueta **SINTÉTICO**.
- Se regeneran igual siempre (semilla 2040): `python3 scripts/generar_sinteticos.py`.
- Lo marcado con ➕ es supuesto del equipo.

## Qué hay aquí

| Archivo | Qué es | Columnas principales |
| --- | --- | --- |
| `SINTETICO_personas.csv` | 6,162 personas que viajan en un día entre semana | `persona_id`, `territorio_id`, `entidad`, `zona`, `contorno`, `sexo`, `edad`, `rol` (ocupada, estudiante, hogar, mayor), `cadena` (patrón del día), `acceso_auto_moto`, `factor` (cuántas personas reales representa), `min_dia`, `pasajes_dia`, `transbordos_dia`, `usa_transporte_publico`, `camina_algun_tramo`, `viajes_cuidado`, `min_cuidado`, `estres_siempre_o_casi`, `sintetico` |
| `SINTETICO_tramos.csv` | 34,945 tramos: un renglón por cada pedazo de cada viaje | `persona_id`, `viaje`, `tramo`, `proposito`, `de_territorio`, `a_territorio`, `modo`, `linea`, `min` (en movimiento), `espera_min`, `km`, `costo` (pasaje del tramo; el Metro se cobra una vez por viaje), `sintetico` |
| `SINTETICO_territorios.csv` | 16 alcaldías y 12 municipios con sus indicadores y el índice | `ipt`, `ipt_bruto`, `min_trabajo`, `pct_30min`, `pct_mas_2h`, `pct_cuidadoras`, `min_cuidado_extra`, `gasto_diario`, `pct_estres`, `pct_camina_mujeres`, `pct_camina_hombres`, `pct_usa_tp`, `n_muestra`, `poblacion` (real, Censo 2020) |
| `SINTETICO_calibracion.csv` | Comparación oficial contra sintético | `indicador`, `oficial`, `valor_sintetico`, `diferencia`, `unidad`, `fuente`, `url`, `ok`, `sintetico` |
| `../../app/data/sintetico.js` | Lo mismo, resumido para la app (`window.SINTETICO`), con 4 personajes | — |

## Cómo se hizo, en palabras simples

1. **Repartimos 6,162 personas** entre 16 alcaldías y 12 municipios conurbados según su población real ([Censo 2020](https://www.inegi.org.mx/programas/ccpv/2020/)). Los territorios chicos tienen al menos 120 personas, y el `factor` corrige ese reparto.
2. **A cada persona le damos un rol** (ocupada, estudiante, hogar o mayor), un sexo, una edad y un **patrón de día**: por ejemplo casa → dejar a alguien → trabajo → casa. Las proporciones de roles y patrones están hechas para que los propósitos de los viajes queden como en la EOD 2017.
3. **Cada actividad tiene un lugar.** El trabajo y la escuela se eligen con un modelo de gravedad: más probable si hay muchos empleos o escuelas y si queda cerca. El cuidado, las compras y la salud suelen estar cerca de casa.
4. **Cada viaje se arma por tramos:** caminar a la parada, esperar, micro o combi, transbordo, Metro u otra troncal y caminar al destino. Cada modo tiene su velocidad y su espera ➕, y cada tramo su pasaje.
5. **Calibramos:** con una congestión fija de hora pico ➕, el programa ajusta 9 perillas (qué tan lejos queda el empleo, caminata, acceso a auto o moto, uso de micro) durante 32 vueltas, hasta que los resultados se parecen a las cifras oficiales.
6. **Estrés:** quien usa transporte público tiene más probabilidad de estresarse si viaja más tiempo y hace más transbordos ➕. Ajustamos el nivel de cada grupo para que coincida con el estudio de la UNAM.

## Anclas reales (lo que el modelo debe reproducir) y calibración

Tolerancia: ±1.5 puntos o ±1.5 minutos.

| Indicador | Oficial | Sintético | Diferencia | ¿Cumple? | Fuente |
| --- | --- | --- | --- | --- | --- |
| Personas ocupadas que viven en la CDMX y llegan al trabajo en 30 min o menos | 34.1 % | 34.0 % | -0.1 | ✅ | [INEGI, Encuesta Intercensal 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/ei/EIC2025-def_CDMX.pdf) |
| Viaje al trabajo, promedio, quienes viven en la CDMX (todos los viajes) | 54 min | 53.8 min | -0.2 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viaje al trabajo, promedio, quienes viven en municipios conurbados (todos los viajes) | 60 min | 59.8 min | -0.2 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viaje al trabajo, promedio, ZMVM (todos los viajes) | 57 min | 56.6 min | -0.4 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viaje al trabajo sin contar viajes solo a pie, ZMVM | 63 min | 63.0 min | +0.0 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Mujeres que viajan y caminan en algún tramo | 71.4 % | 71.2 % | -0.2 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Hombres que viajan y caminan en algún tramo | 60.3 % | 60.2 % | -0.1 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Mujeres que viajan y usan transporte privado | 18.2 % | 18.2 % | +0.0 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Hombres que viajan y usan transporte privado | 26.4 % | 26.4 % | +0.0 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viajes en transporte público que usan micro o combi en algún tramo | 74.1 % | 73.8 % | -0.3 | ✅ | [UNAM Global con la EOD 2017](https://unamglobal.unam.mx/global_revista/microbus-o-combi-transporte-publico-mas-utilizado-en-el-valle-de-mexico/) |
| Viajes para llevar o recoger a alguien (cuidado) | 6.6 % | 6.9 % | +0.3 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viajes para ir al trabajo | 22.0 % | 21.7 % | -0.3 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viajes para ir a estudiar | 11.9 % | 12.0 % | +0.1 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viajes de compras | 6.5 % | 6.6 % | +0.1 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viajes para regresar al hogar | 47.3 % | 47.3 % | +0.0 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Viajes sociales, trámites, salud y otros | 5.7 % | 5.6 % | -0.1 | ✅ | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| Estrés del traslado siempre o casi siempre: viven en la CDMX | 18 % | 18.0 % | +0.0 | ✅ | [UNAM Global (estudio exploratorio)](https://unamglobal.unam.mx/usuarios-de-transporte-publico-se-estresan-en-sus-recorridos/) |
| Estrés del traslado: municipios conurbados (primer contorno ➕) | 24 % | 24.0 % | +0.0 | ✅ | [UNAM Global (estudio exploratorio)](https://unamglobal.unam.mx/usuarios-de-transporte-publico-se-estresan-en-sus-recorridos/) |
| Estrés del traslado: Estado de México (segundo contorno ➕) | 35 % | 34.9 % | -0.1 | ✅ | [UNAM Global (estudio exploratorio)](https://unamglobal.unam.mx/usuarios-de-transporte-publico-se-estresan-en-sus-recorridos/) |

**Ojo con dos anclas:**

- **34.1%** viene de la Encuesta Intercensal 2025 y los minutos al trabajo de la EOD 2017: son encuestas y años distintos. Aquí conviven en la misma población a propósito.
- **Estrés:** el estudio de la UNAM es **exploratorio**, no representativo. Además, interpretamos ➕ "municipios conurbados" como los de primer contorno, a menos de unos 20 km del Zócalo (Nezahualcóyotl, Tlalnepantla, Naucalpan, La Paz, Ecatepec y Chimalhuacán), y "Estado de México" como los de segundo contorno (Valle de Chalco, Chalco, Ixtapaluca, Tecámac, Tultitlán y Cuautitlán Izcalli).

**Pasajes usados.**

- Con fuente en el repo:
  - [Metro, 5 pesos](https://www.nmas.com.mx/ciudad-de-mexico/subira-tarifa-metro-cdmx-2026-gobierno-anuncia-precio-para-proximo-ano/)
  - [micro de la CDMX, 7.50](https://www.adn40.mx/mexico/2025-11-04/tarifa-microbus-cdmx-ha-aumentado-el-precio-del-pasaje-en-20-anos)
  - [combi del Edomex, 14 pesos mínimo](https://www.razon.com.mx/estados/2025/10/11/aumentan-tarifas-del-transporte-publico-en-edomex-cuanto-costara-y-donde-aplica/)
  - [Trolebús Chalco–Santa Martha, 13 pesos](https://www.chilango.com/noticias/transporte/trolebus-chalco-santa-martha-costo/)
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
| Tultitlán | Edomex | 100 | 63.8 | 18.6 | 39.0 | 11.0 | 44.5 | 36.2 |
| Valle de Chalco Solidaridad | Edomex | 94 | 74.2 | 20.3 | 40.9 | 9.1 | 37.7 | 43.2 |
| Chimalhuacán | Edomex | 92 | 71.4 | 26.5 | 43.1 | 14.7 | 36.3 | 31.1 |
| Nezahualcóyotl | Edomex | 88 | 62.0 | 15.0 | 39.8 | 12.9 | 33.7 | 23.9 |
| Tláhuac | CDMX | 86 | 76.2 | 25.4 | 43.4 | 17.9 | 16.9 | 20.5 |
| Ixtapaluca | Edomex | 81 | 73.1 | 19.8 | 39.6 | 14.0 | 37.4 | 43.4 |
| Tecámac | Edomex | 75 | 55.8 | 30.9 | 29.2 | 12.4 | 36.1 | 29.5 |
| Chalco | Edomex | 74 | 77.9 | 26.7 | 35.1 | 11.7 | 35.2 | 29.0 |

## Supuestos del equipo ➕

- **Roles:** ocupada 50%, estudiante 27%, hogar 15% y mayor 8%. Proporción de mujeres en cada rol: 40%, 50%, 80% y 55%.
- **Cuidado:**
  - Las mujeres cuidan mucho más: 0.21 viajes de cuidado por mujer ocupada contra 0.06 por hombre ocupado.
  - Una cuarta parte de quienes se dedican al hogar lleva y recoge a alguien dos veces al día.
  - Con eso, los viajes de cuidado quedan en 6.6% del total, como en la EOD.
- **Tiempos y costos:** velocidades y esperas por modo, factor de rodeo de la red de 1.35, pesos de empleo, escuelas y hospitales por territorio, acceso a auto o moto por territorio, y líneas troncales de cada lugar.
- **Caminata:** un tramo a pie dentro de un viaje en vehículo cuenta si dura 10 minutos o más. Los viajes solo a pie siempre cuentan.
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
