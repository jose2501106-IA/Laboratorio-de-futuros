# Registro de fuentes

Fuentes que se ingieren completas, con inventario y auditoría de cobertura. Las fuentes de la investigación (cientos de notas, informes y bases de datos) se citan dentro de cada documento, en su sección de fuentes.

| ID | Fuente | Autoría | Año | Tipo | Licencia | Original | Unidades | Inventario | Estado |
|---|---|---|---|---|---|---|---|---|---|
| D25 | *Diccionario de Señales y Tendencias 2025* | CENTRO, Especialidad en Diseño del Mañana; eds. Karla Paniagua y Francesca Tur | 2025 (archivo creado el 1-feb-2025 y modificado el 24-feb-2025; en los créditos, «Centro de diseño y comunicación, S.C., 2024») | Publicación, 47 págs. | Creative Commons BY-NC-SA, sin versión indicada (distintivo en la p. 2); la misma página lleva «©» tras «(Eds).». Se atribuye siempre, sin uso comercial, y lo derivado se comparte con la misma licencia ([nota de uso](../03-senales/diccionario-2025/README.md#nota-de-uso)) | Fuera del repositorio: lo conserva el usuario. Archivo recibido: `diccionario_de_futuros-y-tendencias  2025.pdf` (1.7 MB) | 138 unidades: preliminares (portada, créditos, licencia, índice y la capa de formulario del índice), 2 ensayos, método, 40 señales, 40 QR (39 con enlace válido), 40 ilustraciones, 9 erratas de la publicación fuera de las señales (5 de créditos e índice y 4 del ensayo de la p. 5) y contraportada | [D25](inventarios/D25.md) | Ingerida |
| P25 | *Exploring the Futures of Public Transportation in Mexico City* | José Rubén García Ramírez, CENTRO | 2025 (archivo del 2-jun-2025, versión con tres comentarios de revisión) | Póster, 1 pág. | CC BY, sin versión indicada (el sello dice «cc BY») | Fuera del repositorio: lo conserva el usuario. Archivo recibido: `Futures of Public Transportation in CDMX - Jose Ruben Garcia.pdf` (5.3 MB). Contenido completo en [estudios/P25](../estudios/P25-garcia-2025-futuros-transporte-publico.md). La capa de texto del PDF corta el final de algunas líneas: manda la imagen | 43 unidades: 39 del póster, 1 de los metadatos del archivo y 3 anotaciones de revisión | [P25](inventarios/P25.md) | Ingerida |
| KB-TP | Base de Conocimiento sobre Transporte Público | Ligada a D25-23, D25-31 y P25 [inferencia: José Rubén García Ramírez] | Hitos de 1991 a 2024 | Hoja de cálculo pública de Google | No declarada | https://docs.google.com/spreadsheets/d/16TsvXMkd1KinF_qsaD0rT-OTXRGZ76sRY2mlWniCeh0/edit?usp=sharing | 99 registros | — | Referenciada; se ingiere en el chat de históricos |

Las otras 19 bases de conocimiento del diccionario están listadas en [03-senales/diccionario-2025/README.md](../03-senales/diccionario-2025/README.md#bases-de-conocimiento).

## Cómo se ingirió cada fuente

1. **Original:** se recibió el PDF y no se modificó. Por decisión del usuario, el repositorio no guarda PDF.
2. **Texto completo:** se extrajo con `pdftotext`, página por página, y se revisaron las imágenes de cada página para reconstruir el orden de lectura donde las columnas se mezclaban. Los QR se decodificaron con OpenCV.
3. **Inventario:** una fila por unidad, con su destino en el repositorio.
4. **Síntesis:**
   - D25: fichas parafraseadas con todos sus datos.
   - P25: traducción completa, texto original y análisis.
5. **Auditoría:** revisión mecánica y revisión independiente, registradas en [AUDITORIA.md](AUDITORIA.md).
