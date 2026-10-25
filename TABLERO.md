# Tablero de maniobra · Laboratorio de Futuros · Chilangatón

*Actualizado: 25-oct-2026, 12:40 · Entrega: 14:00*

Este archivo coordina a todos los chats que trabajan en paralelo en el proyecto Chilangathon. **Antes de subir algo al repo, cada chat lee este tablero.**

---

## 1. Qué hay en el repo y en qué orden leerlo

| # | Archivo | Para qué sirve | Estado |
| --- | --- | --- | --- |
| 0 | [CRITERIOS-EVALUACION.md](CRITERIOS-EVALUACION.md) | **La rúbrica del jurado** y cómo vamos en cada criterio | ✅ nuevo: léelo primero |
| 1 | [README.md](README.md) | Puerta de entrada: tesis y hallazgos | ✅ |
| 2 | [senales-tendencias-fuerzas.md](senales-tendencias-fuerzas.md) | Guía fácil: fuerzas, tendencias y señales | ✅ IDs unificados, con salud (SD10) |
| 3 | [retrospectiva-2006-2026.md](retrospectiva-2006-2026.md) | Línea del tiempo 2006–2026 y escenario inercial con aritmética | ✅ unida a `main` |
| 4 | [escenarios-2040.md](escenarios-2040.md) | Tres escenarios: Colapso, Inercial y Transformación | ✅ nuevo |
| 5 | [investigacion.md](investigacion.md) | Investigación completa: 34 fuerzas con fuente, matriz y ruta | ✅ con correcciones de la retrospectiva |
| 6 | [pitch.md](pitch.md) | Guion de unos cuatro minutos y preguntas del jurado | ✅ alineado con el deck de 13 láminas |
| 7 | [img/](img/) | Matriz, cruce y ruta | ✅ |

**Fuera del repo (en Claude, privados):** el documento editable y el deck de 13 láminas. Compártelos desde su menú Compartir si hay que entregarlos.

---

## 2. Quién hace qué

| Chat | Qué hace | Rama | Estado | Siguiente paso |
| --- | --- | --- | --- | --- |
| **Gerente de maniobra** (este) | Integra todo, escenarios, deck y tablero | `main` | Activo | Revisar ramas nuevas y unirlas |
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
| **Decidir la propuesta** (hay una candidata en CRITERIOS-EVALUACION.md); sin ella los criterios 1, 3 y 4 quedan cojos | Equipo | 🔴 Ya |
| Hacer **privado** el repo (GitHub → Settings → Danger Zone → Change visibility) | José | 🔴 Ya |
| Poner el nombre del equipo en la portada y el cierre del deck | Equipo | 🔴 Antes de las 14:00 |
| Compartir el documento y el deck si hay que entregarlos | José | 🔴 Antes de las 14:00 |
| Revisar las cifras de colapso y transformación con la misma aritmética de la retrospectiva | Chat Estudio de futuros | 🟡 |
| Fuente sólida para F9 "el negocio del pasaje" | Chat de transporte | ⚪ |
| Integrar M1–M9 cuando el repo sea privado | Chat Análisis sistémico | ⚪ Después del evento |

---

## 5. Mensajes listos para pegar en cada chat

**Al chat "Estudio de futuros CDMX 2040":**
> Soy el gerente de maniobra. Tu retrospectiva ya está en `main`. Apliqué tus correcciones del cruce con investigacion.md (A4, S2, P1, E4, S3, E7, P5 y E5). Lee `TABLERO.md` y `escenarios-2040.md`. Tu siguiente tarea: revisa las cifras de los escenarios de colapso y transformación con la misma aritmética que usaste para el inercial. Sube los cambios a tu rama `claude/retrospectiva-2006-2026`, rebasada sobre `main`, y avísame. No toques `main`.

**Al chat "Análisis sistémico futuros CDMX":**
> Soy el gerente de maniobra. Lee `TABLERO.md` del repo. Cuando José haga privado el repo, sube tu trabajo a la rama `claude/sistema-m1-m9`, no a `main`, después de `git fetch origin && git rebase origin/main`. Usa los IDs de investigacion.md (S, T, E, A, P) y los tres escenarios de `escenarios-2040.md` (colapso, inercial y transformación). Yo reviso y uno a `main`.

**Al chat "Análisis de transporte público CDMX":**
> Soy el gerente de maniobra. Tu propuesta ya está integrada en `senales-tendencias-fuerzas.md`: la señal SD10, la sección "El viaje también cuesta salud" y la nota de F9 en revisión. Ojo: los IDs de la guía ahora son F, TD y SD. Si consigues una fuente sólida para F9, súbela a la rama `claude/transporte-salud` y avísame.

**Al chat "Mapa sistémico de Ciudad de México":**
> Soy el gerente de maniobra. Lee `TABLERO.md` del repo Laboratorio-de-futuros. Si haces el mapa de movilidad, súbelo a la rama `claude/mapa-movilidad`, con los IDs de investigacion.md. El trabajo de agua queda en el otro repo y no se copia aquí.
