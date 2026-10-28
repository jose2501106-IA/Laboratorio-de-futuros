# Tablero de maniobra · Laboratorio de Futuros · Chilangatón

> **Evento cerrado.** 🏆 **La Chilangonería del futuro** ganó el primer lugar del Laboratorio de Futuros. Ficha: [RECONOCIMIENTO.md](RECONOCIMIENTO.md).
>
> Este tablero queda como registro del día. Los pendientes "antes de las 14:00" cerraron con el evento.

*Actualizado: 27-oct-2026 · Entrega: 25-oct-2026, 14:00*

Este archivo coordina a todos los chats que trabajan en paralelo en el proyecto Chilangathon. **Antes de subir algo al repo, cada chat lee este tablero.**

---

## 1. Qué hay en el repo y en qué orden leerlo

| # | Archivo | Para qué sirve | Estado |
| --- | --- | --- | --- |
| 🏆 | [RECONOCIMIENTO.md](RECONOCIMIENTO.md) | **Primer lugar**: el evento, qué presentamos y cómo lo hicimos | ✅ nuevo |
| 0 | [CRITERIOS-EVALUACION.md](CRITERIOS-EVALUACION.md) | **La rúbrica del jurado** y cómo vamos en cada criterio | ✅ léelo primero |
| 0b | [CLAUDE.md](CLAUDE.md) | **Todo el contexto** para cualquier chat o para Claude Code: reglas, IDs, metas, cifras y la arquitectura de Trama | ✅ nuevo |
| 0c | [PROPUESTA.md](PROPUESTA.md) | **La propuesta: Trama · la red que cuida tu tiempo**, mapeada a la rúbrica | ✅ nuevo |
| 0d | [app/](app/) y [datos/sinteticos/](datos/sinteticos/) | Prototipo de Trama y datos **SINTÉTICOS** calibrados | ✅ nuevo |
| 1 | [README.md](README.md) | Puerta de entrada: tesis y hallazgos | ✅ |
| 2 | [senales-tendencias-fuerzas.md](senales-tendencias-fuerzas.md) | Guía fácil: fuerzas, tendencias y señales | ✅ IDs unificados, con salud (SD10) |
| 3 | [retrospectiva-2006-2026.md](retrospectiva-2006-2026.md) | Línea del tiempo 2006–2026 y escenario inercial con aritmética | ✅ unida a `main` |
| 4 | [escenarios-2040.md](escenarios-2040.md) | Tres escenarios (Colapso, Inercial y Transformación) y **las 11 metas** | ✅ con metas |
| 5 | [investigacion.md](investigacion.md) | Investigación completa: 34 fuerzas con fuente, matriz y ruta | ✅ con correcciones de la retrospectiva |
| 6 | [pitch.md](pitch.md) | Guion de unos cuatro minutos y preguntas del jurado | ✅ alineado con el deck de 13 láminas |
| 7 | [img/](img/) | Matriz, cruce y ruta | ✅ |

**Fuera del repo (en Claude, privados):** el documento editable, el deck de 16 láminas (unos 4 min 45 s) y el prototipo **Trama** (https://claude.ai/artifact/2iSsL5bfDTXz1RaxGKurfY). Compártelos desde su menú Compartir si hay que entregarlos.

---

## 2. Quién hace qué

| Chat | Qué hace | Rama | Estado | Siguiente paso |
| --- | --- | --- | --- | --- |
| **Gerente de maniobra** (este) | Integra todo: escenarios, metas, propuesta Trama, CLAUDE.md, prototipo, datos sintéticos, deck y tablero | `main` | Activo | Subir el prototipo y el deck con la propuesta |
| **Estudio de futuros 2006–2040** | Línea del tiempo y escenario inercial | `claude/retrospectiva-2006-2026` | ✅ Unida a `main` | Revisar las cifras de colapso y transformación |
| **Análisis sistémico** | Estructura M1–M9, diccionario de señales de CENTRO y póster | Local, sin subir | ⏸️ Espera repo privado | Subir a su rama cuando el repo sea privado |
| **Análisis de transporte** | Salud y estrés en el traslado | — | ✅ Integrado en la guía (SD10) | Buscar fuente sólida para F9 |
| **Mapa sistémico** | Antes agua (archivado); ahora mapa de movilidad | — | Por confirmar | Subir a su rama |

---

## 3. Reglas para todos los chats

0. **Todo se revisa contra [CRITERIOS-EVALUACION.md](CRITERIOS-EVALUACION.md):** antes de subir algo, di a qué criterio le suma.
1. **Nadie sube directo a `main`, salvo el gerente.** Cada chat trabaja en su rama `claude/<tema>` y avisa al terminar.
2. **Antes de subir:** `git fetch origin && git rebase origin/main`.
3. **IDs (una sola convención):**
   - [investigacion.md](investigacion.md): **S1–S7, T1–T5, E1–E9, A1–A7, P1–P6**. Son los IDs oficiales.
   - [senales-tendencias-fuerzas.md](senales-tendencias-fuerzas.md): **F1–F8** (fuerzas), **TD1–TD10** (tendencias) y **SD1–SD10** (señales).
   - Escenarios: **Colapso, Inercial y Transformación**, como en [escenarios-2040.md](escenarios-2040.md).
4. **Cada cifra lleva enlace a su fuente.** Las proyecciones y cálculos del equipo se marcan con ➕.
5. **Nada de texto copiado:** se parafrasea. El diccionario de CENTRO no se sube mientras el repo sea público.
6. **Español de México, fácil de leer:** frases cortas, una idea por párrafo y ejemplos concretos.

---

## 4. Pendientes con dueño

| Pendiente | Dueño | Urgencia |
| --- | --- | --- |
| ~~Decidir la propuesta~~ → **Trama**, en [PROPUESTA.md](PROPUESTA.md) | Equipo | ✅ 13:05 |
| Abrir el prototipo y ensayar el "Recorrido" (`#recorrido`, unos 34 s) para el pitch | Equipo | 🔴 Antes de las 14:00 |
| Compartir el **prototipo Trama**, el deck y el documento desde su menú Compartir | José | 🔴 Antes de las 14:00 |
| Si un chat tiene su propio CLAUDE.md, moverlo a su carpeta (por ejemplo `sistema/CLAUDE.md`): en la raíz solo va uno | Chat Análisis sistémico | 🟡 |
| Cambiar los datos sintéticos por datos reales (encuesta del piloto) | Equipo, después del evento | ⚪ |
| Hacer **privado** el repo (GitHub → Settings → Danger Zone → Change visibility). **Decidido el 27-oct: privado** | José | 🔴 Falta hacerlo |
| ~~Poner el nombre del equipo en la portada y el cierre del deck~~ → **La Chilangonería del futuro** | Equipo | ✅ Nombre definido |
| Compartir el documento y el deck si hay que entregarlos | José | 🔴 Antes de las 14:00 |
| Revisar las cifras de colapso y transformación con la misma aritmética de la retrospectiva | Chat Estudio de futuros | 🟡 |
| Fuente sólida para F9 "el negocio del pasaje" | Chat de transporte | ⚪ |
| Integrar M1–M9 cuando el repo sea privado | Chat Análisis sistémico | ⚪ Después del evento |

---

## 5. Mensajes listos para pegar en cada chat

**Al chat "Estudio de futuros CDMX 2040":**
> Soy el gerente de maniobra. Tu retrospectiva ya está en `main`. Apliqué tus correcciones del cruce con investigacion.md (A4, S2, P1, E4, S3, E7, P5 y E5). Lee `TABLERO.md` y `escenarios-2040.md`. Tu siguiente tarea: revisa las cifras de los escenarios de colapso y transformación con la misma aritmética que usaste para el inercial. Sube los cambios a tu rama `claude/retrospectiva-2006-2026`, rebasada sobre `main`, y avísame. No toques `main`.

**Al chat "Análisis sistémico futuros CDMX":**
> Soy el gerente de maniobra. Lee `TABLERO.md` y `CLAUDE.md` del repo. Cuando José haga privado el repo, sube tu trabajo a la rama `claude/sistema-m1-m9`, no a `main`, después de `git fetch origin && git rebase origin/main`. Usa los IDs de investigacion.md (S, T, E, A, P) y los tres escenarios de `escenarios-2040.md` (colapso, inercial y transformación). Ojo: ya hay un `CLAUDE.md` en la raíz; si tienes uno propio, guárdalo como `sistema/CLAUDE.md`. Las metas se llaman "Meta 1" a "Meta 11" para no chocar con tus M1–M9. Yo reviso y uno a `main`.

**A cualquier chat que quiera ayudar con el prototipo:**
> Lee `CLAUDE.md` y `PROPUESTA.md`. El prototipo de Trama está en `app/` y los datos sintéticos en `datos/sinteticos/`. Toma un punto del backlog (§12 de CLAUDE.md), trabaja en tu rama `claude/trama-<tema>` y avísame. Todo número sintético dice SINTÉTICO.

**Al chat "Análisis de transporte público CDMX":**
> Soy el gerente de maniobra. Tu propuesta ya está integrada en `senales-tendencias-fuerzas.md`: la señal SD10, la sección "El viaje también cuesta salud" y la nota de F9 en revisión. Ojo: los IDs de la guía ahora son F, TD y SD. Si consigues una fuente sólida para F9, súbela a la rama `claude/transporte-salud` y avísame.

**Al chat "Mapa sistémico de Ciudad de México":**
> Soy el gerente de maniobra. Lee `TABLERO.md` del repo Laboratorio-de-futuros. Si haces el mapa de movilidad, súbelo a la rama `claude/mapa-movilidad`, con los IDs de investigacion.md. El trabajo de agua queda en el otro repo y no se copia aquí.
