# 🏆 Primer lugar · Laboratorio de Futuros · Chilangatón 2026

*Ficha del reconocimiento · Ciudad de México · 25 de octubre de 2026*

El equipo **La Chilangonería del futuro** ganó el **primer lugar del Laboratorio de Futuros** del Chilangatón con **[Trama · la red que cuida tu tiempo](PROPUESTA.md)**.

Trama es una propuesta para devolver tiempo a quien vive lejos y cuida. Sale de nuestro análisis de la movilidad de la CDMX y su zona metropolitana al 2040.

---

## 1. El evento

| | |
| --- | --- |
| **Qué** | Chilangatón: un Hackatón para los retos de hoy y un Laboratorio de Futuros para los de mañana |
| **Cuándo** | Domingo 25 de octubre de 2026. Empezó a las 8:00; la entrega fue a las 14:00 |
| **Dónde** | UTOPÍA Elena Poniatowska Amor, Av. Miguel Hidalgo 128, San Lucas, Coyoacán |
| **Organizan** | Secretaría de Educación, Ciencia, Tecnología e Innovación (SECTEI) y Secretaría de Desarrollo Económico (SEDECO) de la Ciudad de México |
| **Convocatoria** | [luma.com/j55anly0](https://luma.com/j55anly0) |

**El reto del Laboratorio:** cada mesa imagina dos futuros para 2040, uno que no queremos y otro que sí. Después propone qué haría falta para llegar al segundo y evitar el primero ([convocatoria](https://luma.com/j55anly0)).

**Nuestro tema:** movilidad.

**Pregunta focal:** ¿cómo se moverán las personas en la CDMX y su zona metropolitana en 2040, y quién gana o pierde con ello?

**Lente:** cuidados y periferias.

**Cómo calificó el jurado:** con cinco criterios: análisis prospectivo, pertinencia social, contribución del conocimiento, claridad y viabilidad, y presentación. Detalle en [CRITERIOS-EVALUACION.md](CRITERIOS-EVALUACION.md).

---

## 2. Qué presentamos

| Pieza | Qué es | Dónde |
| --- | --- | --- |
| Investigación | 34 fuerzas de cambio con fuente, en cinco dimensiones (STEEP), y su matriz impacto × incertidumbre | [investigacion.md](investigacion.md) |
| Historia | Línea del tiempo 2006–2026: qué se decidió y qué no | [retrospectiva-2006-2026.md](retrospectiva-2006-2026.md) |
| Escenarios | Colapso, Inercial y Transformación al 2040, con cifras y **11 metas** | [escenarios-2040.md](escenarios-2040.md) |
| Propuesta | **Trama**: app, tablero y simulador que manejan el transporte público de la metrópoli como un solo sistema | [PROPUESTA.md](PROPUESTA.md) |
| Prototipo | Una sola página web con la red real de transporte masivo (48 líneas y 689 estaciones) y datos **SINTÉTICOS** marcados | [app/](app/) |
| Pitch | Guion y preguntas probables del jurado | [pitch.md](pitch.md) |

**El dato que abre la historia:** solo 34.1% de las personas ocupadas que viven en la CDMX llega a su trabajo en 30 minutos o menos. En el país, la cifra es 51.5% ([INEGI, Intercensal 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/ei/EIC2025-def_CDMX.pdf)).

---

## 3. El día, según los commits

Horas de la Ciudad de México, tomadas del historial de este repo.

| Hora | Qué quedó listo |
| --- | --- |
| 10:58 | Investigación: 34 fuerzas con fuente |
| 11:44 | Guía de señales, tendencias y fuerzas |
| 11:55 | Retrospectiva 2006–2026; a las 12:14 ya traía 10 correcciones tras verificar las cifras |
| 12:12 | Tres escenarios al 2040 y tablero de coordinación |
| 12:41 | Rúbrica del jurado y autoevaluación |
| 13:13 | Propuesta Trama y las 11 metas |
| 13:14–13:30 | Prototipo: red real, datos sintéticos y las vistas Mi día, Red viva y Futuros 2040 |
| 14:00 | Entrega |
| 14:23 | Se une el prompt para los mockups de la app (PR #2) |

---

## 4. Cómo trabajamos

- **Método:** 34 fuerzas en cinco dimensiones (STEEP) → clasificación → matriz impacto × incertidumbre → 2 incertidumbres críticas → 3 escenarios → ruta de regreso de 2040 a hoy.
- **Reglas de calidad:**
  - cada cifra lleva su fuente enlazada;
  - las proyecciones del equipo van marcadas con ➕;
  - los datos sintéticos dicen **SINTÉTICO** y nunca se presentan como medición.
- **Herramientas:**
  - Varios chats de Claude (IA) trabajaron en paralelo para investigar, verificar cifras y construir el prototipo. Los coordinamos con un [tablero](TABLERO.md) y con este repo, y el equipo revisó cifras y fuentes.
  - Python y JavaScript sin frameworks.
  - Datos de INEGI, OpenStreetMap y el GTFS de SEMOVI.

---

## 5. Equipo

**La Chilangonería del futuro**

⏳ *Pendiente: nombres de las y los integrantes, su rol y su liga (GitHub o LinkedIn), con su permiso.*

---

## 6. Evidencia

⏳ *Pendiente: foto del reconocimiento o constancia (`img/primer-lugar.jpg`) y liga a la publicación oficial, si existe.*

---

## 7. Qué sigue

La ruta de Trama, según [PROPUESTA.md](PROPUESTA.md) (§7):

- **0–3 meses:**
  - convenio de datos con SEMOVI y el Edomex;
  - comité con el Sistema de Cuidados y una universidad (UNAM o IPN);
  - primer índice de pobreza de tiempo con datos abiertos.
- **3–12 meses:**
  - encuesta a 300 usuarias del corredor oriente, que reemplaza a los datos sintéticos;
  - piloto de la app con 2,000 usuarias.
- **12–24 meses:**
  - medir si bajan los minutos y el estrés del traslado;
  - proponer 3 centros de cuidado junto a estaciones.

---

## 8. Gracias

A la SECTEI y a la SEDECO por abrir el Laboratorio, al jurado y a UTOPÍA Elena Poniatowska Amor.

Datos de la red: © colaboradores de OpenStreetMap (ODbL) y GTFS de SEMOVI vía Mobility Database. Estadísticas: INEGI.
