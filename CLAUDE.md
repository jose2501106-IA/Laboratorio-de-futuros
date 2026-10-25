# CLAUDE.md · Laboratorio de Futuros · Movilidad CDMX 2040 · Trama

Lee este archivo completo antes de tocar el repo. Aquí está todo lo necesario para seguir la investigación y construir el prototipo de **Trama**.

---

## 1. Contexto en 30 segundos

- **Evento:** Chilangatón, Laboratorio de Futuros (SECTEI y SEDECO), en UTOPÍA Elena Poniatowska Amor, Coyoacán. Domingo 25 de octubre de 2026; entrega a las 14:00.
- **Tema:** movilidad.
- **Pregunta focal:** ¿cómo se moverán las personas en la CDMX y su zona metropolitana en 2040, y quién gana o pierde con ello?
- **Lente:** cuidados y periferias.
- **Tesis:** la movilidad de 2040 se decide en dos preguntas que nadie ha cerrado:
  1. si la metrópoli se gobierna como una sola (P5, P3);
  2. si la transición va a fondo (A7, E5).
  Si las dos salen bien, llegamos a la metrópoli que cuida; si nada cambia, a la de las cuatro horas; y si además llegan golpes, a la metrópoli rota.
- **Propuesta:** **Trama · la red que cuida tu tiempo**: app, tablero y simulador que manejan el transporte público de la metrópoli como un solo sistema, con una meta: devolver tiempo a quien vive lejos y cuida. Detalle en [PROPUESTA.md](PROPUESTA.md).
- **Persona guía:** **Rosa**, 54 años. Vive en Valle de Chalco, limpia oficinas en Polanco y cuida a su mamá y a su nieta de 6 años.

---

## 2. La rúbrica manda

Todo cambio debe decir **a qué criterio le suma**. Si no le suma a ninguno, no va. Detalle en [CRITERIOS-EVALUACION.md](CRITERIOS-EVALUACION.md).

| # | Criterio | Qué exige |
| --- | --- | --- |
| 1 | Análisis prospectivo | La propuesta sale de las tendencias y los escenarios, y explica cómo cambia las trayectorias |
| 2 | Pertinencia social | Un problema relevante, sus implicaciones sociales y los beneficios de atenderlo |
| 3 | Contribución del conocimiento | Qué hay que investigar, desarrollar o innovar, y cómo eso lleva a la transformación |
| 4 | Claridad y viabilidad preliminar | Una propuesta delimitada y una ruta inicial razonable |
| 5 | Presentación | Problema → análisis → propuesta, en orden y dentro del tiempo |

---

## 3. Reglas que no se rompen

1. **El repo es PÚBLICO.** Nada privado, nada de datos personales, nada de llaves ni tokens. Solo José puede hacerlo privado.
2. **No se sube el diccionario de señales de CENTRO** (ni textual ni parafraseado en bloque) mientras el repo sea público.
3. **El proyecto de agua (InnovaFest) no se copia aquí.** Del repo del Mapa solo se usan capas de **movilidad**.
4. **Cada cifra lleva fuente enlazada.** Se parafrasea; no se copian párrafos. Las proyecciones y supuestos del equipo se marcan con ➕.
5. **Los datos sintéticos se marcan siempre:**
   - prefijo `SINTETICO_` en el nombre del archivo;
   - columna `sintetico = SI` en cada fila;
   - `sintetico: true` en cada objeto JSON;
   - etiqueta visible **SINTÉTICO** en la interfaz, junto a cada número sintético;
   - aviso fijo en la app.
   Nunca se presentan como medición.
6. **Español de México, fácil de leer:** frases cortas, una idea por párrafo y ejemplos concretos.
7. **Git:**
   - Solo el gerente de maniobra sube a `main`. Los demás chats trabajan en `claude/<tema>`.
   - Antes de subir: `git fetch origin && git rebase origin/main`.
   - Los commits terminan con:
     ```
     Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
     Claude-Session: https://claude.ai/code/session_012PpBdpcyDp83uijAGz6oah
     ```
8. **Un solo CLAUDE.md en la raíz.** Si un chat tiene su propio CLAUDE.md, lo guarda en su carpeta (por ejemplo `sistema/CLAUDE.md`), no en la raíz.

---

## 4. Mapa del repo

| Archivo o carpeta | Qué es |
| --- | --- |
| [CRITERIOS-EVALUACION.md](CRITERIOS-EVALUACION.md) | Rúbrica y autoevaluación |
| [TABLERO.md](TABLERO.md) | Coordinación entre chats: quién hace qué, reglas y pendientes |
| [README.md](README.md) | Puerta de entrada |
| [PROPUESTA.md](PROPUESTA.md) | **La propuesta: Trama**, mapeada a la rúbrica |
| [escenarios-2040.md](escenarios-2040.md) | Tres escenarios (Colapso, Inercial y Transformación), cifras, **las 11 metas** y el semáforo |
| [retrospectiva-2006-2026.md](retrospectiva-2006-2026.md) | Línea del tiempo y aritmética del escenario inercial |
| [senales-tendencias-fuerzas.md](senales-tendencias-fuerzas.md) | Guía fácil: F1–F8, TD1–TD10 y SD1–SD10 |
| [investigacion.md](investigacion.md) | Documento completo: 34 fuerzas con fuente y matriz |
| [pitch.md](pitch.md) | Guion y preguntas del jurado |
| `app/` | **Prototipo de Trama** (`index.html`, `data/red.js`, `data/sintetico.js`, `build.py` y `dist/trama.html`) |
| `datos/sinteticos/` | **Datos SINTÉTICOS** con su README y tabla de calibración |
| `scripts/generar_sinteticos.py` | Generador de los sintéticos (semilla 2040) |
| `img/` | Matriz, cruce, ruta y rúbrica |

---

## 5. Convención de IDs

- **[investigacion.md](investigacion.md)** (IDs oficiales): **S1–S7** social, **T1–T5** tecnológica, **E1–E9** económica, **A1–A7** ambiental y **P1–P6** política.
- **Guía [senales-tendencias-fuerzas.md](senales-tendencias-fuerzas.md):** **F1–F8** fuerzas, **TD1–TD10** tendencias y **SD1–SD10** señales. F9, "el negocio del pasaje", está en revisión: no se usa sin fuente sólida.
- **Escenarios:** **Colapso** ("La metrópoli rota"), **Inercial** ("La metrópoli de las cuatro horas") y **Transformación** ("La metrópoli que cuida").
- **Metas:** "Meta 1" a "Meta 11", como en [escenarios-2040.md](escenarios-2040.md#las-metas-son). No uses M1–M9: ese prefijo es del chat de Análisis sistémico.

---

## 6. Escenarios y metas (lo esencial)

| Indicador | Hoy | Colapso 2040 ➕ | Inercial 2040 ➕ | Transformación 2040 ➕ |
| --- | --- | --- | --- | --- |
| Ocupados de la CDMX que llegan en 30 min o menos | 34.1% (2025) | ~23% | 28.7% | 50% |
| Viaje al trabajo, ZMVM | 63 min (2017) | 80 min o más | 72 min | 55 min |
| Pasaje de la periferia frente al Metro | 2.8× (14 contra 5 pesos) | Más de 5× | 3.7–4.4× | Una tarifa integrada |
| Muertes viales al año, CDMX | 424 (2025) | Más de 600 | Unas 500 | Menos de 200 |
| Pasajeros del Metro al año | 1,115 M (2023) | Menos de 1,000 M | 1,366 M | Más de 2,100 M |
| Metrobuses eléctricos | 168 (2026) | Unos 300 | 672 | 100% desde 2033 |
| Viajes en bici al día | 456 mil (2024) | ~450 mil | 0.96 M | 1.5 M |
| Emisiones frente a 2016 | Sin inventario reciente | Sin baja | −36% | −83% |
| Suspensiones de la Línea A por lluvia | 14 o más (2025) | Cierres de meses | Una docena o más | Casi ninguna |
| **El día de Rosa** | 3 h 52 min (SINTÉTICO) | Deja su trabajo: Pantitlán lleva 4 meses cerrado | 4 h 30 min | 2 h |

**Las 11 metas a 2040** (con hitos 2030 y 2035 en [escenarios-2040.md](escenarios-2040.md#las-metas-son)):
1. 50% llega a su trabajo en 30 min o menos.
2. Viaje al trabajo de 55 min.
3. Una sola tarifa y una tarjeta.
4. Menos de 200 muertes viales al año.
5. Metrobús 100% eléctrico (desde 2033).
6. Emisiones −83% frente a 2016.
7. 1.5 millones de viajes en bici al día.
8. Línea A casi sin cortes por lluvia.
9. Más de 2,100 millones de pasajeros del Metro al año.
10. La mitad de personas con más de 2 h diarias de traslado ➕, con la pobreza de tiempo medida y publicada cada año.
11. Un centro de cuidado a 15 min a pie o menos en toda la red masiva.

Cuántas cumple cada escenario: **Colapso 0 de 11**, **Inercial 0 de 11** (una a medias) y **Transformación 11 de 11**.

---

## 7. Cifras verificadas que más se usan

| Dato | Fuente |
| --- | --- |
| 34.1% de los ocupados que viven en la CDMX llega en 30 min o menos (país: 51.5%) | [INEGI, Intercensal 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/ei/EIC2025-def_CDMX.pdf) |
| 71.4% de las mujeres camina en algún tramo, contra 60.3% de los hombres; transporte privado: 18.2% contra 26.4% | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |
| 74.1% de los viajes en transporte público usa micro o combi en algún tramo | [UNAM Global con la EOD 2017](https://unamglobal.unam.mx/global_revista/microbus-o-combi-transporte-publico-mas-utilizado-en-el-valle-de-mexico/) |
| Estrés siempre o casi siempre: 18% (CDMX), 24% (conurbados) y 35% (Edomex). Estudio exploratorio | [UNAM Global](https://unamglobal.unam.mx/usuarios-de-transporte-publico-se-estresan-en-sus-recorridos/) |
| 211 horas y 10,721 pesos al año en el tráfico por cada persona que se traslada | [IMCO, 2026](https://imco.org.mx/costo-del-trafico-2026/) |
| Pasaje mínimo en el Edomex: 14 pesos (oct-2025); Metro: 5 | [La Razón](https://www.razon.com.mx/estados/2025/10/11/aumentan-tarifas-del-transporte-publico-en-edomex-cuanto-costara-y-donde-aplica/) |
| Trolebús Chalco–Santa Martha: promete bajar un viaje de 2 h a 45 min | [Chilango](https://www.chilango.com/noticias/transporte/cuando-abrira-trolebus-chalco-santa-martha-asi-van-las-obras-ruta-conectara-cdmx-edomex/) |
| La Línea A tuvo al menos 18 suspensiones en 2025, 14 de ellas por lluvia | [Infobae](https://www.infobae.com/mexico/2026/01/01/linea-a-del-metro-cdmx-registra-nuevo-record-en-2025-por-las-veces-que-suspendio-servicio/) |
| Metrobús 100% eléctrico en 2033 | [Expansión Política](https://politica.expansion.mx/cdmx/2026/08/27/metrobus-cdmx-electrico-2033) |
| Emisiones −36% o −83% a 2040, según el financiamiento | [SEDEMA, ELAC](https://www.sedema.cdmx.gob.mx/storage/app/media/DGCPCA/PACCM_y_ELAC_uv.pdf) |
| El plan a 2045 no trae metas de movilidad ni menciona el cuidado en esa línea | [Cuadernillo del PGD](https://sedeco.cdmx.gob.mx/storage/app/media/Proyecto%20PGD/PGD_cuadernillo.pdf) |
| EOD 2017: 34,558,044 viajes en un día entre semana en la ZMVM | [INEGI, EOD 2017](https://www.inegi.org.mx/contenidos/programas/eod/2017/doc/resultados_eod_2017.pdf) |

Las demás cifras, con su fuente, están en [investigacion.md](investigacion.md) y [retrospectiva-2006-2026.md](retrospectiva-2006-2026.md).

---

## 8. Trama: qué construimos

**Principios:** el día completo, no un viaje; el sistema completo, no una línea; el futuro, no solo hoy.

| Vista | Para quién | Qué hace |
| --- | --- | --- |
| **Mi día** | Usuarias, como Rosa | Planea cadenas de cuidado con todos los modos. Muestra tiempo, pesos, transbordos y estrés; compara hoy contra "con Trama"; avisa de cortes antes de salir; tiene modos "viaje tranquilo" y "accesible" |
| **Red viva** | SEMOVI, Edomex, Sistema de Cuidados, alcaldías y municipios | Mapa de la red real, el índice de pobreza de tiempo por territorio, los cortes y a quién afectan, y dónde poner centros de cuidado |
| **Futuros 2040** | Quien decide y el jurado | Palancas de gobernanza (partida ↔ integrada) y de transición (a medias ↔ a fondo), más los golpes externos. Dice hacia qué escenario vamos, qué metas se cumplen y cómo sería el día de Rosa |
| **Recorrido** | El pitch | Tres pasos guiados: Rosa hoy → la ciudad → el futuro |

**Índice de pobreza de tiempo (IPT, 0–100).** El método es abierto; la fórmula exacta está en [datos/sinteticos/README.md](datos/sinteticos/README.md). Combina:
- el % de personas con más de 2 h diarias de traslado;
- el % que no llega a su trabajo en 30 min;
- la carga de cuidado;
- el gasto en pasajes.

**Privacidad:** sin cuentas obligatorias, solo agregados (10 personas o más por celda), sin rastreo individual y con código abierto.

---

## 9. Arquitectura

### Prototipo (hoy)

- **Una sola página web**, sin backend: HTML, CSS y JS vanilla con un mapa SVG y proyección propia (lon/lat corregida por cos(lat)).
- **Datos:**
  - `app/data/red.js` (`window.RED`) es la red **real** simplificada: líneas, estaciones y alcaldías de OpenStreetMap y GTFS de SEMOVI. La atribución es obligatoria en pantalla.
  - `app/data/sintetico.js` (`window.SINTETICO`) son los datos **SINTÉTICOS**: territorios, personajes y calibración. Lo genera `scripts/generar_sinteticos.py`.
- **Publicación:** `python3 app/build.py` arma `app/dist/trama.html`, un solo archivo con todo adentro, que se publica como artifact.
- **Librerías:** solo de cdnjs y con versión exacta; si se puede, ninguna.

### Producto (después del evento)

| Pieza | Propuesta |
| --- | --- |
| Rutas multimodales y cadenas de cuidado | OpenTripPlanner 2 con GTFS de SEMOVI y del Edomex, más OSM; viajes con varias paradas y ventanas de tiempo |
| Tiempo real | GTFS-RT donde exista; alertas oficiales de STC, Metrobús y SEMOVI |
| Índice y datos abiertos | Pipeline en Python con DuckDB; publicación trimestral en CSV y GeoJSON |
| Simulador 2040 | Dinámica de sistemas (stocks y flujos) calibrada con los tres escenarios |
| Frontend | Web app ligera y offline (PWA) con MapLibre; WCAG 2.2 AA; celulares de gama baja |
| Canales sin datos | WhatsApp o SMS y tableros impresos en paraderos |
| Privacidad | Agregación con k ≥ 10, privacidad diferencial para validaciones de tarjeta y auditoría externa |

### Modelo de datos (una sola ontología para las cinco capas)

| Entidad | Ejemplo |
| --- | --- |
| `Persona` | id, territorio, sexo, edad, ocupada, cuida_a[], sintetico |
| `CadenaDelDia` | persona_id, escenario, tramos[], total_min, total_costo, transbordos, estres |
| `Tramo` | sale, de, a, modo, linea, min, costo, proposito |
| `Red` | `Linea` (id, sistema, color, geometría) y `Estacion` (id, nombre, lineas[], lon, lat, accesible) |
| `Territorio` | id, nombre, entidad, zona, población, ipt y sus componentes |
| `Corte` | línea, tramo, causa (lluvia, hundimiento, falla), inicio, fin, personas afectadas |
| `Escenario` | palancas (gobernanza, transición, golpes) e indicadores; metas cumplidas |

---

## 10. Datos sintéticos: cómo se usan

- Reemplazan **por ahora** la encuesta de viajes de cuidado y estrés del traslado.
- Se calibran contra las anclas reales: 34.1%, 63 min, 71.4% contra 60.3%, 74.1%, estrés 18%, 24% y 35%, y los pasajes. La tabla de calibración vive en `datos/sinteticos/SINTETICO_calibracion.csv` y en su README.
- **Semilla fija (2040):** cualquiera puede regenerarlos con `python3 scripts/generar_sinteticos.py`.
- Si un supuesto no tiene fuente en el repo, se marca con ➕ y se dice.
- **Se reemplazan** por la encuesta del piloto, una nueva encuesta origen-destino y las validaciones anónimas de la tarjeta MI.

---

## 11. Diseño

- **Paleta (la misma del deck):**

  | Nombre | Hex |
  | --- | --- |
  | asfalto | #16181D |
  | papel | #F5F2EA |
  | tinta | #1C1E24 |
  | tinta suave | #4A4F5A |
  | niebla | #B9BDC6 |
  | rosa | #D1006A |
  | rosa oscuro | #B0005A |
  | rosa claro | #FF5FA8 |
  | teal | #0E7C74 |
  | teal texto | #0B6A63 |
  | teal tinte | #DDEFEC |
  | rosa tinte | #F7DDE8 |

- **Tipografía:** Space Grotesk para títulos y Public Sans para texto (Google Fonts).
- **Colores por sistema:** usa los del GTFS o los oficiales. Nunca uses solo el color para dar significado; acompáñalo de texto o patrón.
- **Tono:** cálido y claro. Rosa es el centro; las cifras, el respaldo.
- **Accesibilidad:** contraste AA, foco visible, `aria-label` en controles y mapa, y responsivo desde 360 px.

---

## 12. Backlog del prototipo (en orden)

1. Red viva con la red real y el IPT por territorio (SINTÉTICO).
2. Mi día de Rosa: hoy contra "con Trama" y el aviso de lluvia en la Línea A.
3. Futuros 2040: dos palancas y los golpes externos → escenario, metas y día de Rosa.
4. Recorrido de presentación de unos 30 segundos.
5. Dónde van los centros de cuidado: ranking de estaciones de transbordo.
6. Simulador de tarifa integrada en el corredor oriente: quién gana y cuánto.
7. Modo "accesible": estaciones con elevador, cuando haya dato.
8. Exportar el IPT en CSV y GeoJSON.

**Terminado quiere decir:**
- abre sin errores de consola;
- se ve bien en el celular;
- cada número sintético dice SINTÉTICO;
- la atribución de OSM y GTFS está visible;
- y `build.py` regenera `dist/trama.html`.

---

## 13. Cómo correr

```bash
python3 scripts/generar_sinteticos.py   # regenera datos/sinteticos/ y app/data/sintetico.js
python3 app/build.py                    # arma app/dist/trama.html (un solo archivo)
python3 -m http.server -d app           # abre http://localhost:8000
```

---

## 14. Glosario mínimo

- **Pobreza de tiempo:** cuando el traslado se come las horas de cuidado, descanso o trabajo.
- **Cadena de cuidado:** el día de quien cuida, con varias paradas (escuela, clínica, mercado), no un viaje de ida y vuelta.
- **Incertidumbre crítica:** una fuerza de alto impacto cuyo rumbo no se conoce. Aquí son dos: gobernanza y transición.
- **Comodín:** un evento poco probable y de alto impacto, como un sismo o una sequía larga.
- **Backcasting:** trazar la ruta de regreso desde el futuro deseado hasta hoy.
