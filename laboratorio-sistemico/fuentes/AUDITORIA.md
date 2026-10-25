# Auditoría de cobertura y verificación

Registro de cada ronda de revisión: qué se revisó, con qué método, qué se encontró y qué se corrigió. Cada ronda la hace un agente que no escribió ni corrigió lo que revisa. Los informes completos quedaron en la carpeta temporal de la sesión; aquí está su resumen.

## D25 · Diccionario de Señales y Tendencias 2025

### Ronda 1 · Revisión mecánica (25-oct-2026)

| Prueba | Método | Resultado |
|---|---|---|
| Cifras | Cada número del texto de cada página (pp. 7-46) debe aparecer en su ficha | 129 de 129 presentes |
| Nombres propios | Cada palabra con mayúscula inicial de cuatro letras o más, salvo conectores, debe aparecer en su ficha | 970 de 976. Las 6 «faltantes» son palabras comunes al inicio de oración (Programas, Basado, Podemos, Integrar, Resultado, Internacionalmente): falsos positivos |
| Destinos del inventario | Cada unidad de [inventarios/D25.md](inventarios/D25.md) apunta a un archivo y un ancla que existen | 132 de 132 unidades con destino válido; 0 en N/A |
| Paráfrasis | Tramos de 16 palabras o más idénticos al original | Se reescribieron los tramos que no son nombres, títulos ni listas |

### Ronda 2 · Revisión independiente (25-oct-2026)

Dos agentes nuevos leyeron las 47 páginas completas, con las imágenes, y las compararon con las fichas.

| Tramo | Veredicto | Hallazgos | Lo principal |
|---|---|---|---|
| pp. 1-26 | INCOMPLETO | 21: 1 media, 20 bajas | La p. 2 lleva licencia Creative Commons BY-NC-SA y el repositorio solo registraba el «©». Faltaban partes de los ensayos de las pp. 5 y 6. Había erratas sin documentar, paráfrasis que decían más que la fuente y metadatos desalineados |
| pp. 27-47 | COMPLETO | 21: 1 media, 20 bajas | Paráfrasis con matices perdidos, erratas que no lo eran y metadatos de relevancia y alcance |

Lo que salió bien en los dos tramos:
- Los 40 QR coinciden con las fichas y con el README.
- Ningún nombre propio ni cifra falta en su ficha.
- No hay copia literal de más de 15 palabras.
- El índice corregido y el orden de lectura reconstruido son correctos.

**Correcciones:** un agente corrector cotejó los 42 hallazgos con la página antes de tocar nada.
- **Resultado:** corrigió 40, dejó 2 a medias (B-13 y B-20) y no corrigió A-4. El DLE registra «creatura» como forma culta, así que no es errata.
- **Licencia:** se agregó la unidad D25.PRE.04 y la licencia quedó en `CLAUDE.md`, el método, el README, el registro y la sección «Fuente» de las 40 fichas.
- **Erratas:** se fijó un criterio en el README y se copió a la plantilla de fichas. Las faltas de puntuación que no cambian el sentido no se registran.
- **B-20:** la contraportada quedó descrita en el inventario al regenerarlo.
- **Revisión mecánica después de corregir:**
  - `gen_d25.py`: 40 fichas y 133 unidades, sin unidades en N/A ni fallas.
  - `cobertura_d25.py`: 129 de 129 cifras y 968 de 968 nombres propios. Siete palabras comunes al inicio de oración se agregaron a la lista de exclusión.

### Ronda 3 · Revisión independiente (25-oct-2026)

| Tramo | Veredicto | Hallazgos | Lo principal |
|---|---|---|---|
| pp. 1-26 | INCOMPLETO | 17: 2 medios y 15 bajos | No falta ningún dato. Los medios son la sigla INAPAM con el nombre equivocado en la fuente sin registrar, y una nota ➕ errónea sobre la fecha de la Ley Silla. Lo demás es criterio de erratas, matices de «En una línea» y atribuciones sin [inferencia] |
| pp. 27-47 | INCOMPLETO | 15: 1 medio y 14 bajos | No falta ningún dato y los 23 hallazgos de la ronda 2-B quedaron resueltos. El medio es la nota de D25-23, que comparaba viajes diarios del Metro con bases distintas |

Comprobaciones de la ronda:
- `cobertura_d25.py` da 129 de 129 cifras y 968 de 968 nombres propios.
- Los 40 QR y los pares se confirmaron de nuevo.
- El inventario tiene 174 enlaces y ninguno roto.
- No hay prosa copiada de 16 palabras o más.

Verificaciones web hechas durante la ronda:
- **DLE:** registra «creatura» como «f. cult. criatura», sin marca de desusada (dle.rae.es, 25-oct-2026). La decisión de no tratarla como errata se sostiene.
- **Ley Silla:** el decreto salió en el DOF el 19-dic-2024, con 180 días de adecuación hasta junio de 2025. La fuente acierta.
- **Metro:** con la misma base (total anual entre 365), 2019 da unos 4.5 millones de viajes diarios, frente a 3.4 millones en 2025. Se corrigió M1.

**Correcciones:** el mismo corrector de la ronda 2 resolvió 31 de los 32 hallazgos después de cotejarlos con la página, la imagen o la estructura del PDF.
- Quedó pendiente el B-H15, que era opcional: dar unidad propia a las notas al pie de la p. 34, que ya están en D25-34.
- El README tiene ahora reglas para mayúsculas, texto de ilustraciones y prefijos separados.
- Las erratas pasaron de 5 a 9 y el inventario a 138 unidades, con D25.PRE.05 para los 37 botones sin acción del índice.
- Después de corregir: `gen_d25.py` da 40 fichas, 138 unidades y 0 fallas; `cobertura_d25.py` da 129 de 129 cifras y 968 de 968 nombres.

### Cierre

El usuario pidió ajustar el trabajo al tiempo del hackatón (25-oct-2026, 13:28), así que no se abre una ronda 4 de D25. Lo que queda son hallazgos menores de estilo y de criterio, y la siguiente ronda se hará después del evento.

## P25 · Póster de García (2025)

| Ronda | Veredicto | Resultado |
|---|---|---|
| 1 · Mecánica | — | 40 de 40 unidades con destino; texto original completo por sección (licencia CC BY) |
| 2 · Independiente | INCOMPLETO | 13 hallazgos: 3 medios y 10 bajos (#21 a #33 del informe); los 13 se corrigieron |
| 3 · Independiente | INCOMPLETO | 20 hallazgos: 3 medios y 17 bajos. El contenido está completo: los 12 bloques «Texto original» son idénticos a la imagen, los 13 hallazgos de la ronda 2 están resueltos y las lecturas por píxel del corrector se reprodujeron con ±0.03 millones. Los medios: la jerarquía de *Findings*, una inferencia sin marcar sobre la caída de RTP y una atribución a P25 sin respaldo en M2 |
| Corrección de la ronda 3 | — | El corrector resolvió los 19 hallazgos de sus archivos, cada uno verificado contra el PDF: colores medidos a 400 y 600 ppp, sello y metadatos. Los cruzados (M2, 04, M1, mapa y registro) se corrigieron aparte. La KB-TP (99 registros, de 1991 a 2024) la revisaron por separado dos agentes, los correctores de D25 y de P25 |
| 4 · Independiente | En curso | Auditor nuevo |

Hallazgos de severidad media de la ronda 2:
- Tres erratas atribuidas al póster que no lo eran. La capa de texto del PDF corta finales de línea, pero la imagen está completa.
- Las referencias estaban normalizadas sin avisarlo.
- Faltaban las tres anotaciones de revisión del PDF.

**Correcciones:** un corrector resolvió los 13 hallazgos después de cotejarlos con el PDF.
- Ahora hay 43 unidades: se sumaron P25.41 a P25.43 para las anotaciones.
- Se agregaron las referencias literales.
- Se documentaron las anotaciones en un §20 nuevo.
- Se completó la traducción.
- Se agregó la evidencia de M1 sobre RTP al análisis crítico.

## Investigación de las dimensiones (M1-M9)

### Verificación de cifras contra sus fuentes (25-oct-2026)

Dos verificadores que no escribieron los documentos abrieron las fuentes citadas y buscaron alternativas cuando no abrían.

| Verificador | Alcance | Confirmadas | Matizar | Corregir | No verificables | Inconsistencias entre documentos |
|---|---|---|---|---|---|---|
| A | M1, M2, M3 y M7 | 35 | 6 | 0 | 0 | 15 |
| B | M4, M5, M6, M8, M9 y la columna «Hoy» de los escenarios | 28 | 9 | 2 | 2 | 20 |

**Correcciones aplicadas:**

| Tema | Qué cambió | Dónde |
|---|---|---|
| Concesionado | 74% es la cifra base: zona metropolitana, EOD 2017. El 80% del PIM no tiene año ni método | M9, mapa sistémico |
| Trenes del Metro | 313 son trenes disponibles (Segundo Informe), 290 trenes en operación (ago-2026) y 269 el mismo indicador en dic-2025 | M1, M9, mapa |
| Costo del Mundial | Se agregó el balance de julio: 23,003 mdp en total, 8,989 en movilidad | M7 |
| ISN | Al FIMAS va el punto adicional, de 3% a 4%, no todo el impuesto | M7, 04, 09, E3 |
| Línea 1 | Terminó unos 32 meses después de la meta de marzo de 2023, no «tres veces lo previsto» | M1, mapa, 04 |
| Plan Ciclista | Los 34 km son 17 por sentido, todos en Tlalpan | M3, M9, mapa, 04 |
| Plataformas | Las cifras del IMSS son nacionales | M2, 04, equivalencias |
| Pago sin contacto | Empezó en el Metro el 27-sep-2024 en 11 de 12 líneas, y en jun-2026 ya lo aceptaban todas las estaciones | M1 |
| Hogares expulsados | Más de 20 mil al año es un promedio de dos décadas del PGOT; 30 mil viene de una declaración de 2025. No es una medición de 2023-2025 | M4, 04, 06, 07, 09, mapa |
| 81% con Tarjeta MI | La fuente no dice sobre qué universo; «red de gobierno» es inferencia | M8, M9, 04, 06, E1, 09, mapa |
| ENIF | 85% es la población que usa sobre todo efectivo en compras de hasta 500 pesos, no los pagos. Se agregó la fuente del INEGI | M8 |
| Decil I | Es el costo de los pasajes de una persona frente al ingreso de su hogar, no el gasto del hogar. Se escribieron los supuestos | M6, 04, 07, E4, 09, equivalencias |
| Contingencias | 2024 igualó el récord de 1993. Las 5 de 2025 están contadas hasta agosto | M5, 06, E3, 09 |
| Emisiones | 61.3% es de la CDMX en 2016, con tres alcances; 58.3% es de la zona metropolitana en 2018 | M9, 04 |
| Otras | Viajes de cuidado sin regreso a casa; personal ocupado en lugar de empleo; red ciclista de 573 km mapeados; Monterrey con el dato de 2018; alcance nacional de la ENVIPE; Línea 4 de Metrobús en 2026; lluvia de enero a noviembre | M3 a M6, M9, 06, 09, mapa |

**Quedó sin verificar:**
- Cuántos autobuses nuevos tendrá RTP: 380, 390 o 500.
- Si el alza del colectivo empezó el 1 o el 2 de noviembre de 2025.
- Los 5,183 mdp del Mundial y el documento oficial del balance de julio.
- La meta original de la Línea 1 en una fuente primaria.
- El 80% y el 86% del PIM.
- El dato de inseguridad en el transporte para la CDMX: tabulado 1.6 y microdatos de la ENSU.
- El total de contingencias de 2025.
- Los 40 cm al año de hundimiento.
- El 36% de viajes de más de una hora en el tabulado original de la EOD.

### Consistencia interna de la síntesis (25-oct-2026)

Un verificador sin acceso a la web comparó 02 a 09 contra las dimensiones y rehízo los cálculos con sus propios scripts.

- **Resultado:** 44 hallazgos (1 alto, 11 medios y 32 bajos).
- **Lo que cuadra:** los conteos (139 señales, 22 impulsores, 24 tendencias, 11 estrategias e indicadores), la matriz de impacto cruzado, las tablas generadas y las señales tempranas.

**Hallazgo alto y su corrección: el eje 2 mezclaba choques externos con resultados de política.**
- **El problema:**
  - Con esa escala, E1 (el escenario probable) caía en el cuadrante de E2.
  - E3 caía en el de E4.
  - El tablero no podía distinguir una buena respuesta de una presión leve.
- **La corrección:**
  - El eje 2 pasó a medir solo choques externos: calor, lluvia, hundimiento, red eléctrica, sismos y finanzas externas (09-P1 a P6).
  - Los resultados quedaron en un bloque aparte de desempeño bajo presión (09-D1 a D8).
- **Lectura nueva:**
  - El punto «Hoy» pasó de (0.20, 0.60) a (0.20, 0.50).
  - El futuro probable se declara como la frontera entre E1 y E2.
  - Cambiaron 05, 06, E1-E4, 09 y las equivalencias.

**Otras correcciones:**

| Tema | Qué cambió | Dónde |
|---|---|---|
| Metas de muertes viales | 212 en 2030, que es la meta oficial, y menos de 150 en 2035 | 07, 09 |
| Línea 3 | Obras previas en 2026 con 5,000 mdp; renovación integral desde 2027 | M1, M6, M7 |
| Metrobús 100% eléctrico | Se anotan las dos metas: 2030 en el Segundo Informe y 2033 en M5 y M7 **[por verificar]** | M9 |
| Concesionado bajo contrato en E3 | El 70% es su parte de los viajes en transporte público, no la parte de sus viajes con contrato | E3 |
| Red ciclista | 573 km mapeados: 474 activos, 62 fuera de servicio y 37 en otra condición **[por verificar]** | M3, 06, mapa |
| Emisiones | Una sola métrica, la reducción frente a 2018 | 06, E3, E4 |
| Señales tempranas | Se corrigieron los indicadores asignados y se marcaron las señales que no tienen indicador | 09 §4 |
| Hechos con varios ID | Se documentaron S-M1-06 = S-M8-08, el alza de 1.50 pesos con cuatro ID y la licencia permanente con dos | 03 |
| IDs locales | Convención de prefijos al citar entre documentos («09-R2», «mapa-R2») | Método, equivalencias |
| Otros | Revisión cada seis meses; [supuesto] en las secciones de 2040; G7 y P3 con [inferencia]; Fonacipe casi por 13; CIPHER con seis tipos; fila de M9 en el tablero; Línea 12 hacia 2029 en E1; IDs mal citados en E1; tiempo medio frente a «cualquier persona» en la visión | 03, 04, 06, 07, 09, M3, mapa |

### Revisión mecánica de enlaces

`check_links.py` revisa todos los `.md`, sus enlaces internos y anclas, y que no haya archivos de otro tipo. Resultado del 25-oct-2026, después de todas las correcciones: 940 enlaces internos, 0 rotos y 0 archivos que no sean `.md`. Las herramientas están en [herramientas.md](herramientas.md).
