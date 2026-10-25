# Bitácora

## Estado actual

| | |
|---|---|
| Fecha | 25-oct-2026, 13:40 |
| Fase | Fases 1 y 2 completas en primera versión, con verificación de cifras y revisión de consistencia aplicadas. La auditoría de las fuentes de CENTRO quedó con hallazgos menores |
| Publicado | En la rama `claude/sistema-m1-m9` del repositorio, ya privado: `gh api … --jq .visibility` devolvió `private` el 25-oct-2026 a las 13:33. Todo el laboratorio está en la carpeta `laboratorio-sistemico/`, para no chocar con los archivos del equipo en `main` |
| Última verificación | 940 enlaces internos, 0 rotos y ningún archivo que no sea `.md` (`check_links.py`). En D25: 129 de 129 cifras y 968 de 968 nombres propios (`cobertura_d25.py`) |
| Superficie | Claude, en una sesión en la nube con herramientas de Claude Code. Ligada al proyecto «Chilangathon» de claude.ai |

## Tarea en curso

**Laboratorio de futuros de la movilidad de la CDMX al 2040 en Markdown (fases 1 y 2).**

Terminado cuando:

1. ✅ Todo está en `.md`.
2. ⏳ D25 y P25 tienen auditoría independiente hasta COMPLETO.
   - D25: ronda 3 con 32 hallazgos menores, cuyas correcciones están en curso.
   - P25: ronda 4 en curso.
3. ✅ Hay nueve dimensiones con plantilla.
4. ✅ La síntesis está completa (02 a 09) y alineada con la rúbrica del jurado.
5. ✅ Las cifras se verificaron con agentes distintos de quien escribió:
   - dos verificaciones contra fuentes;
   - una revisión de consistencia interna.
6. ✅ El repositorio es privado y el trabajo está en una rama.

**Avance:** el usuario pidió adaptar el trabajo al tiempo del hackatón. Por eso no se abren más rondas de auditoría después de las que ya corren. Las correcciones pendientes se suben como un commit adicional a la misma rama.

## Historial

| Fecha | Hecho | Evidencia |
|---|---|---|
| 25-oct | Estructura de Voros, método, glosario y plantillas | Carpetas 00 a 09 |
| 25-oct | Póster P25: traducción completa, original, análisis crítico e inventario | 43 unidades; auditoría independiente en ronda 4 |
| 25-oct | Diccionario D25: 40 fichas e inventario | 133 unidades; 129 de 129 cifras y 968 de 968 nombres; auditoría en ronda 3 |
| 25-oct | Nueve dimensiones (M1-M9) | 99 señales y 93 indicadores en sus secciones 6 y 12 |
| 25-oct | Mapa sistémico, impacto cruzado y actores | Matriz recalculada por el verificador |
| 25-oct | Tendencias, incertidumbres, cuatro escenarios, futuro preferible, 11 estrategias y monitoreo | 04 a 09 |
| 25-oct | Verificación de cifras contra fuentes | 82 cifras: 63 confirmadas, 15 matizadas, 2 corregidas y 2 no verificables |
| 25-oct | Revisión de consistencia interna | 44 hallazgos atendidos, entre ellos el rediseño del eje 2 |
| 25-oct | Licencias: D25 lleva CC BY-NC-SA y P25 CC BY, ninguna con versión indicada | Imágenes del distintivo |
| 25-oct | Equivalencias con el trabajo del equipo y mapa de este laboratorio contra la rúbrica | `00-marco/equivalencias-con-el-equipo.md` |
| 25-oct | Aportes para la propuesta Trama: línea de trayectoria, respuestas al jurado y corrección de la cifra del Metro | Proyecto de claude.ai, `claude/aportes-sistema-m1-m9.md`, y mensajes al usuario |
| 25-oct | Subida a la rama `claude/sistema-m1-m9` | `git push -u origin claude/sistema-m1-m9` |

## Decisiones

| Decisión | Por qué | Descartado |
|---|---|---|
| Horizonte 2040, visión holística con enfoque en movilidad, todo en `.md`, repositorio privado y fases 1 y 2 | Lo decidió el usuario | — |
| Cuatro arquetipos de Dator | El póster P25 usa cuatro, y los ejes forman cuatro cuadrantes. Las equivalencias explican cómo se relacionan con los tres escenarios del equipo | Reducir a tres sin decisión del usuario |
| El eje 2 mide solo choques externos y los resultados van en un bloque de desempeño | La revisión de consistencia mostró que la escala mezclada no distinguía E3 de E4. Hoy la ciudad queda en (0.20, 0.50): la frontera entre E1 y E2 | Eje mixto, que daba 0.60 |
| Futuro preferible: E4 con elementos de E3 | Juicio de valor declarado | Presentarlo como neutral |
| Laboratorio en `laboratorio-sistemico/` dentro de la rama `claude/sistema-m1-m9`, que sale de `main` | `main` ya tiene `README.md` y `CLAUDE.md` del equipo. Así el gerente puede unir sin conflictos | Subir a la raíz o reemplazar `main` |
| No abrir más rondas de auditoría después de las que corren | El hackatón dura poco; los hallazgos que quedan son menores | Iterar hasta COMPLETO hoy |
| No modificar la carpeta 01 | Regla 7 | Llenarla con la retrospectiva del equipo sin decisión |

## Siguientes pasos

1. 🧑 Decidir con el gerente si la rama se une a `main` tal como está, en `laboratorio-sistemico/`.
2. 🧑 Decidir si la retrospectiva del equipo cuenta como la entrega de históricos de la carpeta 01.
3. Subir las correcciones de la ronda 3 de D25 y el resultado de la ronda 4 de P25 a la misma rama.
4. Después del evento: cerrar las auditorías hasta COMPLETO y verificar los datos de `main` que llenan huecos de 09.
