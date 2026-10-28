# Instrucciones para trabajar en este repositorio

Repositorio privado de futuros de la movilidad en la Ciudad de México, con visión holística y horizonte 2040. Antes de cambiar algo, lee [README.md](README.md) y [00-marco/metodo.md](00-marco/metodo.md).

## Reglas

1. **Idioma:** español de México, claro y directo.
2. **Solo Markdown:** todo va en `.md`. Nada de PDF, CSV, hojas de cálculo, imágenes ni scripts. Los datos van en tablas y los diagramas en Mermaid.
3. **Estructura:** las carpetas siguen el proceso de Voros (ver el método). No crees carpetas nuevas sin actualizar el README y el método.
4. **IDs y etiquetas:** usa los del método (D25-NN, P25, S-Mx-NN, H-AAAA-NNN, E1-E4; [supuesto], [inferencia], [por verificar], ➕, ⚠, 🟢🟡⚪).
5. **Fuentes:**
   - Cada cifra lleva su fuente numerada [n] y su fecha.
   - No se inventan cifras, citas ni enlaces.
   - Lo que no se pudo confirmar se marca [por verificar].
6. **Derechos de autor:**
   - El diccionario D25 lleva aviso © de CENTRO y licencia Creative Commons BY-NC-SA, sin versión indicada (p. 2).
     - Se atribuye siempre y no se usa con fines comerciales.
     - Lo que se derive de D25 se comparte con la misma licencia.
     - Por prudencia, se parafrasea y solo se citan frases cortas.
   - El póster P25 tiene licencia CC BY: se puede reproducir con atribución.
7. **Históricos:** la carpeta `01-historicos-2006-2026/` la llena otro chat con su prompt. No la modifiques salvo que te lo pidan.
8. **Señales nuevas:** usa [00-marco/plantillas/ficha-senal.md](00-marco/plantillas/ficha-senal.md), guárdalas en `03-senales/escaneo-2026/` y agrégalas al tablero.
9. **Dimensiones:** siguen [00-marco/plantillas/dimension.md](00-marco/plantillas/dimension.md).
10. **Antes de dar algo por terminado:**
    - Verifica las cifras con un agente o una persona distinta de quien escribió.
    - Corre la auditoría de cobertura si cambió una fuente ingerida.
    - Registra el resultado en [fuentes/AUDITORIA.md](fuentes/AUDITORIA.md) y lo hecho en [BITACORA.md](BITACORA.md).
11. **Commits:** en español; dicen qué cambió y, si aplica, el resultado de la verificación.

## Recursos

| Recurso | Qué es | Herramienta | Fecha |
|---|---|---|---|
| https://github.com/jose2501106-IA/Laboratorio-de-futuros | Repositorio remoto. Privado desde el 25-oct-2026 (13:33) | `gh api repos/jose2501106-IA/laboratorio-de-futuros --jq .visibility` | 2026-10-25 |
| Rama `main` del remoto | Trabajo del equipo del Chilangatón: `README.md`, `TABLERO.md`, `investigacion.md`, `escenarios-2040.md`, `retrospectiva-2006-2026.md`, `senales-tendencias-fuerzas.md`, `pitch.md` e `img/`. No comparte historia con este laboratorio | `git fetch origin '+refs/heads/*:refs/remotes/origin/*'` | 2026-10-25 |
| Rama `claude/sistema-m1-m9` | Rama de este laboratorio, que `TABLERO.md` le asigna. Sale de `main` y pone todo el laboratorio en `laboratorio-sistemico/`, para no chocar con el `README.md` ni el `CLAUDE.md` del equipo | `git push -u origin claude/sistema-m1-m9` | 2026-10-25 |
| Rama `claude/retrospectiva-2006-2026` | Retrospectiva del equipo, ya unida a `main` | `git ls-remote --heads origin` | 2026-10-25 |
| Proyecto «Chilangathon» en claude.ai | Documentos de coordinación de los chats: `claude/tablero-maniobra.md`, `claude/escenarios-2040.md`, `claude/senales-tendencias-fuerzas.md`, `claude/estado-mapa-movilidad.md` | Projects (`project_info`) | 2026-10-25 |
| KB-TP | Base de conocimiento sobre transporte público de CENTRO: https://docs.google.com/spreadsheets/d/16TsvXMkd1KinF_qsaD0rT-OTXRGZ76sRY2mlWniCeh0/edit?usp=sharing | Hoja de cálculo pública | 2026-10-25 |
| Base de calles y urbanismo táctico | Base de conocimiento de D25-13 y D25-20: https://docs.google.com/spreadsheets/d/1W5tt8TKHSkUKuT_OoRR8e_meiuPDke4G4zfKlXb-cMY/edit?usp=sharing | Hoja de cálculo pública | 2026-10-25 |
| Herramientas de verificación | `cobertura_d25.py`, `gen_d25.py`, `extraer_dimensiones.py`, `gen_tableros.py` y `check_links.py`, guardadas como bloques de código en [fuentes/herramientas.md](fuentes/herramientas.md) porque el repo es solo Markdown | Python 3 | 2026-10-25 |
