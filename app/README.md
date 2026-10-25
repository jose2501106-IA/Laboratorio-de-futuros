# Trama · prototipo

**Trama, la red que cuida tu tiempo.** Ve el transporte público de la metrópoli como **un solo sistema**: Metro, Metrobús, Trolebús, Cablebús, Tren Ligero, RTP, corredores concesionados, Mexibús, Mexicable, Suburbano, El Insurgente, Ecobici y caminar. Tiene una sola meta: devolver tiempo a quien vive lejos y cuida.

Es el prototipo de la propuesta del equipo ([PROPUESTA.md](../PROPUESTA.md)) para el Laboratorio de Futuros del Chilangatón 2026.

## Qué tiene

| Vista | Para quién | Qué hace |
| --- | --- | --- |
| **Mi día** | Quien viaja, como Rosa | El día completo como cadena de cuidado, con todos los modos, el caminar y la espera. Compara "Hoy" contra "Con Trama · piloto 2030" y dice cuánto tiempo se devuelve al día y al mes. Tiene los modos "viaje tranquilo" y "accesible", y un aviso simulado de lluvia en la Línea A con su ruta alterna. |
| **Red viva** | Quien gestiona: SEMOVI, Edomex, Sistema de Cuidados, alcaldías y municipios | Mapa de la red real de 48 líneas. Cada territorio aparece con su índice de pobreza de tiempo (IPT): ranking y ficha. Hay dos botones: "¿Dónde van los centros de cuidado?" y "Lluvia en Línea A", que muestra a quién afecta el corte. |
| **Futuros 2040** | Quien decide y el jurado | Dos palancas, que son las incertidumbres críticas (gobernanza y transición), más los golpes externos y "Trama en marcha". Indica hacia qué escenario vamos (Colapso, Inercial o Transformación), cuántas de las 11 metas se cumplen y cómo es el día de Rosa en 2040. |
| **Recorrido de 30 s** | El pitch | Tres pasos guiados: Rosa hoy → la ciudad → el futuro. Se sale con el botón Salir o con Esc. |

Cada vista tiene un enlace directo: `#midia`, `#red` y `#futuros`. Con `#recorrido`, el recorrido arranca solo.

## Cómo abrirlo

```bash
python3 -m http.server -d app        # luego abre http://localhost:8000
python3 app/build.py                 # arma app/dist/trama.html, un solo archivo para publicar
```

`dist/trama.html` es la versión publicada como artifact. No incluye `<html>`, `<head>` ni `<body>`, porque el artifact los pone.

## De dónde salen los datos

**Real**
- `data/red.js` (`window.RED`): las líneas, estaciones y nodos de transbordo de la red masiva, más las alcaldías y el límite de la CDMX.
- Se arma con `python3 app/tools/preparar_red.py <mapa/web/data> app/data/red.js`, a partir de las capas de movilidad del chat del Mapa (solo movilidad, nada de agua).
- Fuente: © colaboradores de OpenStreetMap (ODbL) y el GTFS de SEMOVI vía Mobility Database. La atribución se ve en el mapa.

**SINTÉTICO**
- `data/sintetico.js` (`window.SINTETICO`): territorios con IPT, personajes con sus cadenas del día y la tabla de calibración.
- Lo genera `scripts/generar_sinteticos.py` (semilla 2040). Está calibrado con INEGI (EOD 2017 e Intercensal 2025) y la UNAM. Ver [datos/sinteticos/](../datos/sinteticos/).
- En pantalla, cada número sintético lleva la etiqueta **SINTÉTICO**, y la barra superior tiene un aviso fijo con el botón "Ver calibración".
- Si falta el archivo, la app usa un respaldo mínimo, también sintético.

**Proyecciones del equipo ➕**
- Futuros 2040 interpola entre los valores de los tres escenarios de [escenarios-2040.md](../escenarios-2040.md).
- El efecto de "Trama en marcha" es un supuesto del equipo: +0.15 en gobernanza, +0.10 en transición y 30% menos daño de los golpes externos.

## Notas técnicas

- HTML, CSS y JavaScript vanilla. El mapa es SVG con proyección propia: lon/lat corregida por cos(19.4°).
- No usa librerías ni teselas externas. Funciona sin backend.
- Respeta los temas claro y oscuro y `prefers-reduced-motion`. Es responsivo desde 360 px.
- Controles con `aria-label` y foco visible.

## Pendiente

- Simulador de tarifa integrada en el corredor oriente: quién gana y cuánto.
- Estaciones con elevador reales para el modo "accesible".
- Exportar el IPT en CSV y GeoJSON.
