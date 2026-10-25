# 01 · Históricos 2006-2026

> **Reservado.** Esta carpeta la llena otro chat con el prompt de [PROMPT-chat-historicos.md](PROMPT-chat-historicos.md). Aquí queda el formato para que lo que entregue encaje con el resto del repositorio sin rehacer nada.

## Estado

- [ ] Pendiente: se pidió a otro chat.

## Para qué sirve

- Dar dirección y ritmo a las tendencias de [04-tendencias-impulsores](../04-tendencias-impulsores/README.md).
- Explicar por qué el sistema está como está ([02-sistema-movilidad](../02-sistema-movilidad/README.md)).
- Encontrar rupturas y patrones que se repiten: obras que se anuncian y no se terminan, crisis que cambian prioridades, políticas que sobreviven o no a un cambio de administración.
- Calibrar los escenarios de [06-escenarios-2040](../06-escenarios-2040/README.md). Lo que nunca ha pasado en 20 años necesita más evidencia para entrar en un escenario probable.

## Alcance

- **Periodo:** del 1 de enero de 2006 a octubre de 2026.
- **Tema:** la movilidad de la Ciudad de México con visión holística, en las dimensiones M1 a M8 (ver [00-marco/metodo.md](../00-marco/metodo.md)), más los eventos de contexto que la afectaron (sismos, pandemia, crisis de agua, inundaciones, crisis fiscales, megaeventos).
- **Frontera con el resto del repositorio:** aquí va lo que pasó. El presente (2024-2026) y el futuro se trabajan en las demás carpetas. Un hecho de 2024-2026 puede aparecer aquí como hito y en una dimensión como parte del estado actual.

## Periodos por administración

| Periodo | Jefatura de Gobierno |
|---|---|
| dic 2006 – dic 2012 | Marcelo Ebrard Casaubon |
| dic 2012 – mar 2018 | Miguel Ángel Mancera Espinosa |
| abr 2018 – dic 2018 | José Ramón Amieva Gálvez (sustituto) |
| dic 2018 – jun 2023 | Claudia Sheinbaum Pardo |
| jun 2023 – oct 2024 | Martí Batres Guadarrama |
| oct 2024 – | Clara Brugada Molina |

## Archivos esperados

```
01-historicos-2006-2026/
├── README.md                        este archivo; el otro chat actualiza «Estado»
├── PROMPT-chat-historicos.md        instrucción para el otro chat
├── cronologia-general.md            de 60 a 100 hitos clave en una sola tabla
├── periodos.md                      una sección por administración
├── hitos-M1-transporte-masivo.md
├── hitos-M2-concesionado-informal-plataformas.md
├── hitos-M3-movilidad-activa-espacio-publico.md
├── hitos-M4-territorio-vivienda-metropoli.md
├── hitos-M5-ambiente-energia-clima-riesgos.md
├── hitos-M6-personas-equidad-genero-seguridad.md
├── hitos-M7-gobernanza-finanzas-instituciones.md
├── hitos-M8-tecnologia-datos-logistica.md
├── series.md                        indicadores anuales 2006-2025
├── rupturas-y-patrones.md           discontinuidades, ciclos y lecciones
└── fuentes.md                       todas las fuentes numeradas
```

## Formato de hitos

Cada archivo `hitos-Mx-….md` lleva una tabla ordenada por fecha:

| ID | Fecha | Precisión | Hecho | Tipo | Escala | Actores | Dato | Fuente | Confianza |
|---|---|---|---|---|---|---|---|---|---|
| H-2021-001 | 2021-05-03 | día | (Ejemplo de formato) Colapsa un tramo elevado de la Línea 12 del Metro entre las estaciones Tezonco y Olivos | Crisis | CDMX | STC Metro; Gobierno de la CDMX | 26 personas fallecidas | [n] | 🟢 |

| Campo | Regla |
|---|---|
| ID | H-AAAA-NNN, consecutivo por año, único en toda la carpeta |
| Fecha | AAAA-MM-DD; si no se sabe el día, AAAA-MM; si no, AAAA |
| Precisión | día, mes o año |
| Hecho | Una oración propia, con sujeto y verbo |
| Tipo | Política, Norma, Obra, Servicio, Crisis, Evento, Dato, Tecnología o Social |
| Escala | Alcaldía, CDMX, ZMVM, Nacional o Internacional |
| Dato | Cifra con unidad, si la hay |
| Fuente | [n], que remite a `fuentes.md` |
| Confianza | 🟢 fuente primaria o dos fuentes serias; 🟡 una fuente seria; ⚪ sin confirmar |

## Formato de series

`series.md` lleva una tabla por indicador:

| Año | Valor | Unidad | Fuente | Nota |
|---|---|---|---|---|

Indicadores sugeridos, en este orden de prioridad:

1. Afluencia anual del Metro, Metrobús, Trolebús, Tren Ligero, RTP y Cablebús.
2. Viajes en Ecobici y kilómetros de ciclovía.
3. Vehículos de motor registrados en circulación en la CDMX: autos y motocicletas (INEGI).
4. Muertes y lesiones por siniestros viales.
5. Tarifa del Metro, nominal y a precios constantes.
6. Presupuesto ejercido por SEMOVI, STC Metro, Metrobús, STE y RTP.
7. Días con contingencia ambiental.
8. Población de la CDMX y de la ZMVM.
9. Viajes diarios por modo según las EOD 2007 y 2017.

## Puntos de partida

- **KB-TP · Base de Conocimiento sobre Transporte Público:** 99 hitos de 1991 a 2024 con PESTEL, CIPHER y poder/interés. Ligada a D25-23, D25-31 y P25: https://docs.google.com/spreadsheets/d/16TsvXMkd1KinF_qsaD0rT-OTXRGZ76sRY2mlWniCeh0/edit?usp=sharing
- **Base de conocimiento de calles y urbanismo táctico** (D25-13 y D25-20): https://docs.google.com/spreadsheets/d/1W5tt8TKHSkUKuT_OoRR8e_meiuPDke4G4zfKlXb-cMY/edit?usp=sharing
- Encuestas Origen-Destino 2007 y 2017 (INEGI), portal de datos abiertos de la CDMX, afluencias del STC Metro, informes de gobierno, Cuenta Pública y Gaceta Oficial de la Ciudad de México.
