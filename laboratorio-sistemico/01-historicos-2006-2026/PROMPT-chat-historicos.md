# Prompt para el chat de históricos

Copia todo lo que está dentro del bloque y pégalo en el otro chat. Si ese chat tiene acceso al repositorio, adjunta también este archivo y el [README](README.md) de la carpeta.

````text
Necesito una investigación histórica profunda, verificable y ordenada de la MOVILIDAD en la Ciudad de México de 2006 a hoy (octubre de 2026), con visión holística. Es la parte «pasado» de un repositorio de futuros de la movilidad de la CDMX con horizonte 2040 (repositorio privado jose2501106-IA/Laboratorio-de-futuros, carpeta 01-historicos-2006-2026/). Otra parte del equipo ya trabaja el presente (2024-2026) y los escenarios futuros. Tu trabajo es solo lo que pasó.

PARA QUÉ SE VA A USAR
- Dar dirección y ritmo a las tendencias: qué creció, qué cayó, qué tan rápido.
- Explicar por qué el sistema está como está.
- Encontrar rupturas y patrones que se repiten (obras anunciadas y no terminadas, crisis que cambiaron prioridades, políticas que sobrevivieron o no a un cambio de administración).
- Calibrar escenarios: lo que nunca pasó en 20 años necesita más evidencia para considerarse probable.

ALCANCE
Periodo: 1 de enero de 2006 a octubre de 2026. Periodos por administración: Ebrard (dic 2006-dic 2012), Mancera (dic 2012-mar 2018), Amieva (abr-dic 2018), Sheinbaum (dic 2018-jun 2023), Batres (jun 2023-oct 2024), Brugada (oct 2024-hoy). Confirma las fechas exactas.

Ocho dimensiones (usa estos códigos):
- M1 Transporte masivo y trenes: Metro, Metrobús, Trolebús, Tren Ligero, Cablebús, RTP, Tren Suburbano, Tren Interurbano México-Toluca, CETRAM.
- M2 Concesionado, informal y plataformas: microbuses, vagonetas, corredores, chatarrización, mototaxis, taxis, Uber/DiDi y regulación, motocicletas, reparto por apps.
- M3 Movilidad activa, espacio público y seguridad vial: Ecobici, ciclovías, peatonalizaciones, urbanismo táctico, Visión Cero, fotomultas y fotocívicas, siniestralidad.
- M4 Territorio, vivienda y metrópoli: EOD 2007 y 2017, viajes metropolitanos, vivienda, gentrificación, ordenamiento territorial, AIFA.
- M5 Ambiente, energía, clima y riesgos: contingencias, Hoy No Circula, electrificación, inundaciones, hundimiento, sismos (2017), calor, crisis de agua.
- M6 Personas usuarias: tarifas, gratuidades, accesibilidad, mujeres y acoso, delitos en transporte, personas mayores, niñez.
- M7 Gobernanza, finanzas e instituciones: leyes de movilidad (2014 y reformas), creación de SEMOVI, planes de movilidad, presupuestos, deuda, concesiones, coordinación metropolitana, rendición de cuentas (Línea 12).
- M8 Tecnología, datos y logística: tarjeta MI, pago sin contacto, datos abiertos, apps, C5, carga y reparto.
Incluye los eventos de contexto que afectaron la movilidad aunque no sean de movilidad: sismo de 2017, pandemia de 2020-2021, colapso de la Línea 12 (2021), inundaciones, crisis hídrica, megaeventos como el Mundial 2026.

ARCHIVOS A ENTREGAR (todo en Markdown, nada de CSV, PDF ni imágenes)
1. cronologia-general.md: de 60 a 100 hitos clave en una sola tabla.
2. periodos.md: una sección por administración con apuestas, obras, crisis, saldo e indicadores al inicio y al final.
3. hitos-M1-transporte-masivo.md, hitos-M2-concesionado-informal-plataformas.md, hitos-M3-movilidad-activa-espacio-publico.md, hitos-M4-territorio-vivienda-metropoli.md, hitos-M5-ambiente-energia-clima-riesgos.md, hitos-M6-personas-equidad-genero-seguridad.md, hitos-M7-gobernanza-finanzas-instituciones.md, hitos-M8-tecnologia-datos-logistica.md: entre 25 y 60 hitos cada uno.
4. series.md: indicadores anuales 2006-2025, una tabla por indicador (Año | Valor | Unidad | Fuente | Nota). Prioridad: afluencia anual de Metro, Metrobús, Trolebús, Tren Ligero, RTP y Cablebús; viajes de Ecobici y km de ciclovía; autos y motocicletas registrados en circulación en la CDMX (INEGI); muertes y lesiones por siniestros viales; tarifa del Metro nominal y a precios constantes; presupuesto de SEMOVI, Metro, Metrobús, STE y RTP; días con contingencia ambiental; población de la CDMX y la ZMVM; viajes diarios por modo en las EOD 2007 y 2017.
5. rupturas-y-patrones.md: discontinuidades, ciclos que se repiten y lecciones para pensar el futuro.
6. fuentes.md: todas las fuentes numeradas [n]: institución o medio, título, URL, fecha de publicación, fecha de consulta.

FORMATO DE CADA HITO (tabla ordenada por fecha)
| ID | Fecha | Precisión | Hecho | Tipo | Escala | Actores | Dato | Fuente | Confianza |
- ID: H-AAAA-NNN, consecutivo por año y único en toda la carpeta.
- Fecha: AAAA-MM-DD (o AAAA-MM o AAAA si no hay más precisión). Precisión: día, mes o año.
- Hecho: una oración propia con sujeto y verbo.
- Tipo: Política, Norma, Obra, Servicio, Crisis, Evento, Dato, Tecnología o Social.
- Escala: Alcaldía, CDMX, ZMVM, Nacional o Internacional.
- Dato: cifra con unidad, si la hay.
- Fuente: [n], que remite a fuentes.md.
- Confianza: 🟢 fuente primaria o dos fuentes serias; 🟡 una fuente seria; ⚪ sin confirmar.

PUNTOS DE PARTIDA
- Base de Conocimiento sobre Transporte Público (99 hitos de 1991 a 2024 con PESTEL, CIPHER y poder/interés; investigación de José Rubén García Ramírez, CENTRO): https://docs.google.com/spreadsheets/d/16TsvXMkd1KinF_qsaD0rT-OTXRGZ76sRY2mlWniCeh0/edit?usp=sharing . Úsala como semilla, pero verifica cada hito con una fuente propia y quédate solo con los de 2006 en adelante.
- Base de conocimiento de calles y urbanismo táctico: https://docs.google.com/spreadsheets/d/1W5tt8TKHSkUKuT_OoRR8e_meiuPDke4G4zfKlXb-cMY/edit?usp=sharing
- INEGI (EOD 2007 y 2017, vehículos de motor registrados en circulación, accidentes de tránsito terrestre), portal de datos abiertos de la CDMX, afluencias del STC Metro, informes de gobierno, Cuenta Pública, Gaceta Oficial de la Ciudad de México, Congreso de la CDMX, ITDP, WRI México, IMCO, medios serios.

REGLAS
- Español de México, claro y directo.
- No inventes hechos, cifras, fechas ni URLs. Si algo no se puede confirmar, va con confianza ⚪ y la etiqueta [por verificar].
- Cada cifra con fuente y fecha.
- Lo que sea interpretación tuya va marcado [inferencia].
- No escribas escenarios ni futuros: eso lo hace otra parte del equipo.

ENTREGA
- Si tienes acceso al repositorio: trabaja en una rama nueva llamada historicos-2006-2026, escribe solo dentro de 01-historicos-2006-2026/, actualiza la sección «Estado» de su README.md y no toques ninguna otra carpeta.
- Si no tienes acceso: entrega cada archivo completo en Markdown, uno por bloque, con su nombre de archivo encima.

Antes de terminar, revisa: que no haya IDs repetidos, que cada hito tenga fuente, que todas las fuentes citadas existan en fuentes.md y que las series no tengan años sin nota cuando falte el dato.
````
