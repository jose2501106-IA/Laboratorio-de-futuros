# Herramientas de verificación

> El repositorio es solo Markdown, así que los scripts que se usaron para generar tablas y verificar la cobertura se guardan aquí como bloques de código. Para usarlos, copia cada bloque en un archivo `.py` **fuera del repositorio** y córrelo con Python 3.
> Ninguno modifica las fuentes originales. Los que escriben en el repositorio solo reemplazan el contenido entre marcadores `<!-- …:INICIO -->` y `<!-- …:FIN -->`, o regeneran un inventario.

## Orden recomendado después de cambiar fichas o dimensiones

1. `gen_d25.py`, si cambió alguna ficha del diccionario.
2. `cobertura_d25.py`: debe dar todas las cifras y todos los nombres presentes.
3. `gen_tableros.py`: regenera el tablero de señales y la lista de indicadores.
4. `check_links.py`: 0 enlaces rotos y 0 archivos que no sean `.md`.

| Script | Qué hace | Uso |
|---|---|---|
| [check_links.py](#check_linkspy) | Revisa todos los `.md`: enlaces internos, anclas con el formato de GitHub y que no haya archivos de otro tipo. | `python3 check_links.py RUTA_DEL_REPO` |
| [cobertura_d25.py](#cobertura_d25py) | Revisión mecánica de D25: cada cifra y cada nombre propio de cada página debe aparecer en su ficha. Necesita el texto de cada página, que se extrae del PDF con `pdftotext -layout -f N -l N`. | `python3 cobertura_d25.py RUTA_DEL_REPO CARPETA_CON_D25-pNN.txt` |
| [gen_d25.py](#gen_d25py) | Regenera las tablas del README del diccionario (entre sus marcadores), el inventario `fuentes/inventarios/D25.md` y `fichas_d25.json`, y verifica las anclas. | `python3 gen_d25.py RUTA_DEL_REPO` |
| [extraer_dimensiones.py](#extraer_dimensionespy) | Extrae las señales (sección 6) y los indicadores (sección 12) de las dimensiones como JSON. | `python3 extraer_dimensiones.py RUTA_DEL_REPO > dimensiones.json` |
| [gen_tableros.py](#gen_tablerospy) | Regenera el tablero de señales de `03-senales/README.md` y la lista completa de indicadores de `09-monitoreo/README.md`, y verifica los enlaces que genera. | `python3 gen_tableros.py RUTA_DEL_REPO fichas_d25.json` |

## check_links.py

Revisa todos los `.md`: enlaces internos, anclas con el formato de GitHub y que no haya archivos de otro tipo.

Uso: `python3 check_links.py RUTA_DEL_REPO`

````python
#!/usr/bin/env python3
"""Revisa enlaces internos y anclas de todos los .md de un repo, y que no haya archivos que no sean .md.
Uso: python3 check_links.py REPO"""
import re, sys
from pathlib import Path

repo = Path(sys.argv[1]).resolve()


def slug(h):
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)  # texto de enlaces
    h = re.sub(r"[*`]", "", h)
    s = h.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


cache = {}


def anchors(p):
    if p not in cache:
        t = p.read_text(encoding="utf-8")
        t = re.sub(r"(`{3,})[^\n]*\n.*?\n\1", "", t, flags=re.S)
        seen, out = {}, set()
        for m in re.finditer(r"^#{1,6} (.+?)\s*#*\s*$", t, re.M):
            s = slug(m.group(1))
            n = seen.get(s, 0)
            out.add(s if n == 0 else f"{s}-{n}")
            seen[s] = n + 1
        out |= set(re.findall(r'<a (?:name|id)="([^"]+)"', t))
        cache[p] = out
    return cache[p]


broken, total = [], 0
for md in sorted(repo.rglob("*.md")):
    if ".git" in md.parts:
        continue
    t = md.read_text(encoding="utf-8")
    t_nocode = re.sub(r"(`{3,})[^\n]*\n.*?\n\1", "", t, flags=re.S)
    t_nocode = re.sub(r"`[^`\n]*`", "", t_nocode)
    for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", t_nocode):
        dest = m.group(1)
        if re.match(r"^(https?|mailto|computer):", dest):
            continue
        total += 1
        path, _, anc = dest.partition("#")
        tgt = md if not path else (md.parent / path).resolve()
        if not tgt.exists():
            broken.append((str(md.relative_to(repo)), dest, "no existe"))
            continue
        if anc and tgt.is_file() and tgt.suffix == ".md" and anc not in anchors(tgt):
            broken.append((str(md.relative_to(repo)), dest, "ancla"))
otros = [str(p.relative_to(repo)) for p in repo.rglob("*") if p.is_file() and ".git" not in p.parts and p.suffix != ".md"]
print(f"Enlaces internos: {total}; rotos: {len(broken)}")
for b in broken:
    print("  ", b)
print(f"Archivos que no son .md: {len(otros)}")
for o in otros:
    print("  ", o)
sys.exit(1 if broken or otros else 0)
````

## cobertura_d25.py

Revisión mecánica de D25: cada cifra y cada nombre propio de cada página debe aparecer en su ficha. Necesita el texto de cada página, que se extrae del PDF con `pdftotext -layout -f N -l N`.

Uso: `python3 cobertura_d25.py RUTA_DEL_REPO CARPETA_CON_D25-pNN.txt`

````python
#!/usr/bin/env python3
"""Revisión mecánica de cobertura de D25: cada cifra y cada nombre propio de la página
debe aparecer en su ficha. Uso: python3 cobertura_d25.py REPO PAGINAS_TXT"""
import re, sys, unicodedata, glob
from pathlib import Path

repo, txtdir = Path(sys.argv[1]), Path(sys.argv[2])
fichas_dir = repo / "03-senales" / "diccionario-2025"

STOP = set("""Diccionario Señales Tendencias Qué Por Esta Este Estos Estas Este Ese Esa Así Además También Sin
Aunque Asimismo Ante Para Con Los Las Del Una Uno Unos Unas Otro Otra Otros Otras Desde Entre Durante Cada Cuando
Como Donde Hoy Mientras Pese Tras Según Tanto Incluso Quizás Estas Sobre Todo Todas Todos Hablamos Dicho Dichos
Esto Eso Ello Ellas Ellos Este Algunos Algunas Muchas Muchos Diversas Diversos Solo Sólo Ahí Allí Aquí Bajo Hasta
Hacia Frente Persona Por Porque Pues Sino Bien Nuevas Nuevos Lo La El En Es Se Su Sus Al Le Les Un Ya Ni No Más
Es Son Fue Han Hay Ser Era Fueron Puede Pueden Debe Deben Resulta Representa Importante Relevante Cambio Cambios
Cuál Cuáles Cómo Dónde Quién Quiénes Además Otro Mientras Tal Tales Dichas Estos Esos Esas Aquellas Aquellos
Igualmente Finalmente Entretanto Actualmente Posteriormente Recientemente Tradicionalmente Hoy Sin Embargo Obstante
Ejemplo Ejemplos Caso Casos Otro Otra Uno Dos Tres
Programas Basado Podemos Integrar Tuvo Resultado Internacionalmente""".split())

def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.lower()

def clean_page(text):
    lines = [l for l in text.splitlines()
             if l.strip() and not l.strip().startswith("Diccionario de Señales")
             and not re.fullmatch(r"\d{1,2}", l.strip())]
    return " ".join(lines)

total_n = total_p = miss_n = miss_p = 0
rows = []
for p in range(7, 47):
    nn = f"{p:02d}"
    src = clean_page((txtdir / f"D25-p{nn}.txt").read_text(encoding="utf-8"))
    files = sorted(glob.glob(str(fichas_dir / f"D25-{nn}-*.md")))
    if not files:
        rows.append((nn, "SIN FICHA", [], []))
        continue
    ficha = files[0]
    tgt = norm(Path(ficha).read_text(encoding="utf-8"))
    tgt_nospace = tgt.replace(" ", "").replace(",", "")
    nums = set(re.findall(r"\d+(?:[.,]\d+)?", src))
    nums = {n for n in nums if not (len(n) <= 1 and n in "123456789")}  # ignora dígitos sueltos 1-9
    props = set()
    for m in re.finditer(r"(?<![\w])([A-ZÁÉÍÓÚÑ][\wáéíóúñü'’\-]{3,})", src):
        w = m.group(1)
        if w in STOP:
            continue
        props.add(w)
    mn = [n for n in sorted(nums) if n.replace(",", "") not in tgt_nospace and n not in tgt]
    mp = [w for w in sorted(props) if norm(w) not in tgt]
    total_n += len(nums); total_p += len(props); miss_n += len(mn); miss_p += len(mp)
    rows.append((nn, Path(ficha).name, mn, mp))

print(f"Cifras: {total_n - miss_n}/{total_n} presentes · Nombres propios: {total_p - miss_p}/{total_p} presentes")
for nn, f, mn, mp in rows:
    if f == "SIN FICHA" or mn or mp:
        print(f"p.{nn} {f}\n   cifras faltantes: {mn}\n   nombres faltantes: {mp}")
````

## gen_d25.py

Regenera las tablas del README del diccionario (entre sus marcadores), el inventario `fuentes/inventarios/D25.md` y `fichas_d25.json`, y verifica las anclas.

Uso: `python3 gen_d25.py RUTA_DEL_REPO`

````python
#!/usr/bin/env python3
"""Genera, a partir de las 40 fichas D25: la tabla de fichas y la lectura de conjunto del README
del diccionario, el inventario fuentes/inventarios/D25.md y devuelve las filas para el tablero.
Uso: python3 gen_d25.py REPO"""
import re, sys, glob, json, collections
from pathlib import Path

repo = Path(sys.argv[1])
fd = repo / "03-senales" / "diccionario-2025"

def slug(h):
    h = h.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")

def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    d = {}
    if not m:
        return d
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip().strip('"')
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip('"') for x in v[1:-1].split(",") if x.strip()]
            d[k.strip()] = v
    return d

def valor(text, etiqueta):
    for line in text.splitlines():
        if line.startswith("|") and etiqueta.lower() in line.lower():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                return cells[1]
    return ""

def una_linea(text):
    m = re.search(r"\*\*En una línea:\*\*\s*(.+)", text)
    return m.group(1).strip() if m else ""

fichas = []
for f in sorted(glob.glob(str(fd / "D25-[0-9][0-9]-*.md"))):
    t = Path(f).read_text(encoding="utf-8")
    fm = frontmatter(t)
    fichas.append({
        "file": Path(f).name, "id": fm.get("id", ""), "titulo": fm.get("titulo", ""),
        "pagina": fm.get("pagina", ""), "alcance": fm.get("alcance_geografico", ""),
        "relevancia": fm.get("relevancia_movilidad", ""), "dims": fm.get("dimensiones_movilidad", []),
        "steep": fm.get("steep", []), "clas": fm.get("clasificacion_propia", ""),
        "par": fm.get("par_tematico", ""),
        "impacto": valor(t, "Impacto en la movilidad"), "evidencia": valor(t, "Solidez de la evidencia"),
        "plazo": valor(t, "Plazo de impacto"), "direccion": valor(t, "| Dirección"),
        "linea": una_linea(t),
    })

def lst(x):
    return ", ".join(x) if isinstance(x, list) else str(x)

# Tabla de fichas (README del diccionario)
rows = ["| ID | Título | Alcance | Relevancia para la movilidad | Dimensiones | Par |", "|---|---|---|---|---|---|"]
for x in fichas:
    rows.append(f"| [{x['id']}]({x['file']}) | {x['titulo']} | {x['alcance']} | {x['relevancia']} | {lst(x['dims'])} | {x['par']} |")
tabla = "\n".join(rows)

# Lectura de conjunto (conteos)
def contar(key, split=False):
    c = collections.Counter()
    for x in fichas:
        v = x[key]
        if isinstance(v, list):
            for i in v: c[i] += 1
        else:
            c[v.split("(")[0].strip() if split else v] += 1
    return c
rel = contar("relevancia"); dims = contar("dims")
alc = collections.Counter("Otro lugar o escala global" if x["alcance"].startswith("Otro") else x["alcance"] for x in fichas)
conteo = ["| Relevancia para la movilidad | Señales |", "|---|---|"] + [f"| {k} | {v} |" for k, v in rel.most_common()]
conteo += ["", "| Dimensión | Señales que la tocan |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(dims.items())]
conteo += ["", "| Alcance geográfico | Señales |", "|---|---|"] + [f"| {k} | {v} |" for k, v in alc.most_common()]

readme = fd / "README.md"
r = readme.read_text(encoding="utf-8")
def entre(texto, ini, fin, contenido):
    a = texto.index(ini) + len(ini); b = texto.index(fin)
    return texto[:a] + "\n" + contenido + "\n" + texto[b:]
r = entre(r, "<!-- TABLA-FICHAS:INICIO -->", "<!-- TABLA-FICHAS:FIN -->", tabla)
r = entre(r, "<!-- CONTEOS:INICIO -->", "<!-- CONTEOS:FIN -->", "\n".join(conteo))
readme.write_text(r, encoding="utf-8")

# Inventario D25
def anchors(path):
    return {slug(re.sub(r"^#+\s*", "", l)) for l in Path(path).read_text(encoding="utf-8").splitlines() if l.startswith("#")}
inv = ["# Inventario · D25", "",
       "Fuente: CENTRO (2025). *Diccionario de Señales y Tendencias 2025*. Eds. Karla Paniagua y Francesca Tur. Centro de diseño y comunicación, S.C., 2024. Licencia Creative Commons BY-NC-SA, sin versión indicada (p. 2).",
       "Destinos: `README` = [03-senales/diccionario-2025/README.md](../../03-senales/diccionario-2025/README.md); las fichas están en la misma carpeta.", "",
       "| ID | Unidad | Pág. | Destino |", "|---|---|---|---|"]
R = "../../03-senales/diccionario-2025/"
inv += [
 f"| D25.PRE.01 | Portada | 1 | [README#ficha-de-la-publicación]({R}README.md#ficha-de-la-publicación) |",
 f"| D25.PRE.02 | Créditos: institución, autorxs, editoras, derechos | 2 | [README#ficha-de-la-publicación]({R}README.md#ficha-de-la-publicación) |",
 f"| D25.PRE.03 | Índice | 3-4 | [README#índice-corregido]({R}README.md#índice-corregido) |",
 f"| D25.PRE.04 | Licencia Creative Commons BY-NC-SA | 2 | [README#ficha-de-la-publicación]({R}README.md#ficha-de-la-publicación) |",
 f"| D25.ENS.01 | Ensayo de Francesca Tur | 5 | [README#ensayos-de-apertura]({R}README.md#ensayos-de-apertura) |",
 f"| D25.ENS.02 | Ensayo de Karla Paniagua | 6 | [README#ensayos-de-apertura]({R}README.md#ensayos-de-apertura) |",
 f"| D25.MET | Método declarado (Dragt, cursos, bases de conocimiento, DALL-E) | 6 | [README#método-declarado]({R}README.md#método-declarado) |",
]
for x in fichas:
    nn = x["id"].split("-")[1]
    inv.append(f"| D25.SEN.{nn} | Señal «{x['titulo']}» | {nn} | [{x['file']}]({R}{x['file']}) |")
for x in fichas:
    nn = x["id"].split("-")[1]
    inv.append(f"| D25.QR.{nn} | Código QR de la p. {nn} | {nn} | [{x['file']}]({R}{x['file']}) (frontmatter) y [README#bases-de-conocimiento]({R}README.md#bases-de-conocimiento) |")
for x in fichas:
    nn = x["id"].split("-")[1]
    t_f = (fd / x["file"]).read_text(encoding="utf-8")
    if "Ilustración" in t_f:
        inv.append(f"| D25.IMG.{nn} | Ilustración de la p. {nn} (generada con DALL-E) | {nn} | [{x['file']}]({R}{x['file']}#fuente) (descripción) |")
    else:
        inv.append(f"| D25.IMG.{nn} | Ilustración de la p. {nn} | {nn} | N/A: imagen generada con DALL-E, sin datos; se documenta en [README#ficha-de-la-publicación]({R}README.md#ficha-de-la-publicación) |")
for i in range(1, 6):
    inv.append(f"| D25.ERR.0{i} | Errata {i} de la publicación | 2-4 | [README#erratas-de-la-publicación-fuera-de-las-señales]({R}README.md#erratas-de-la-publicación-fuera-de-las-señales) |")
inv.append(f"| D25.CON | Contraportada: título, miniatura de la portada y logotipo «centro.» | 47 | [README#ficha-de-la-publicación]({R}README.md#ficha-de-la-publicación) |")
n_total = len([l for l in inv if l.startswith("| D25.")])
n_na = len([l for l in inv if "| N/A" in l])
inv += ["", f"**Total:** {n_total} unidades; {n_total - n_na} con destino; {n_na} en N/A con razón."]
(repo / "fuentes" / "inventarios" / "D25.md").write_text("\n".join(inv) + "\n", encoding="utf-8")

# Verificación de destinos
fallas = []
for l in inv:
    for m in re.finditer(r"\]\(([^)]+)\)", l):
        target = m.group(1)
        path, _, anc = target.partition("#")
        p = (repo / "fuentes" / "inventarios" / path).resolve()
        if not p.exists():
            fallas.append(f"no existe {path}")
        elif anc and anc not in anchors(p):
            fallas.append(f"ancla inexistente {target}")
print(json.dumps({"fichas": len(fichas), "unidades": n_total, "na": n_na, "fallas": sorted(set(fallas))}, ensure_ascii=False, indent=1))
json.dump(fichas, open(Path(sys.argv[0]).with_name("fichas_d25.json"), "w"), ensure_ascii=False, indent=1)
````

## extraer_dimensiones.py

Extrae las señales (sección 6) y los indicadores (sección 12) de las dimensiones como JSON.

Uso: `python3 extraer_dimensiones.py RUTA_DEL_REPO > dimensiones.json`

````python
#!/usr/bin/env python3
"""Extrae de las dimensiones M1-M8 las tablas de señales (§6) y de indicadores a vigilar (§12).
Uso: python3 extraer_dimensiones.py REPO  -> imprime JSON con señales e indicadores."""
import re, sys, json, glob
from pathlib import Path

repo = Path(sys.argv[1])
dims = sorted(glob.glob(str(repo / "02-sistema-movilidad" / "dimensiones" / "M[1-8]-*.md")))

def seccion(texto, numero):
    m = re.search(rf"^## {numero}\. .*?$(.*?)(?=^## \d+\. |\Z)", texto, re.S | re.M)
    return m.group(1) if m else ""

def filas(tabla_txt):
    out = []
    for line in tabla_txt.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append(cells)
    return out

senales, indicadores = [], []
for f in dims:
    t = Path(f).read_text(encoding="utf-8")
    code = Path(f).name.split("-")[0]
    rows = filas(seccion(t, 6))
    for r in rows[1:]:
        if r and r[0].startswith("S-"):
            senales.append({"dim": code, "file": Path(f).name, "id": r[0], "senal": r[1] if len(r) > 1 else "",
                            "cipher": r[2] if len(r) > 2 else "", "porque": r[3] if len(r) > 3 else "",
                            "fecha": r[-1] if len(r) > 5 else ""})
    rows = filas(seccion(t, 12))
    for r in rows[1:]:
        if len(r) >= 5:
            indicadores.append({"dim": code, "file": Path(f).name, "indicador": r[0], "base": r[1],
                                "umbral": r[2], "fuente": r[3], "frecuencia": r[4]})
print(json.dumps({"senales": senales, "indicadores": indicadores}, ensure_ascii=False, indent=1))
````

## gen_tableros.py

Regenera el tablero de señales de `03-senales/README.md` y la lista completa de indicadores de `09-monitoreo/README.md`, y verifica los enlaces que genera.

Uso: `python3 gen_tableros.py RUTA_DEL_REPO fichas_d25.json`

````python
#!/usr/bin/env python3
"""Genera las tablas del tablero de señales (03-senales/README.md) y la lista completa
de indicadores (09-monitoreo/README.md) a partir de las dimensiones y de fichas_d25.json.
Uso: python3 gen_tableros.py REPO FICHAS_JSON
Reemplaza el contenido entre marcadores y verifica que los enlaces internos existan."""
import re, sys, json, glob, collections
from pathlib import Path

repo = Path(sys.argv[1])
fichas = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
DIMDIR = repo / "02-sistema-movilidad" / "dimensiones"
ESC = repo / "06-escenarios-2040"


def slug(h):
    s = h.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def headings(path):
    return {slug(m.group(2)) for m in re.finditer(r"^(#{1,6}) (.+?)\s*$", path.read_text(encoding="utf-8"), re.M)}


def seccion(texto, numero):
    m = re.search(rf"^## {numero}\. .*?$(.*?)(?=^## \d+\. |\Z)", texto, re.S | re.M)
    return m.group(1) if m else ""


def titulo_seccion(texto, numero):
    m = re.search(rf"^## ({numero}\. .*?)\s*$", texto, re.M)
    return m.group(1) if m else None


def filas(tabla_txt):
    out = []
    for line in tabla_txt.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            out.append([c.strip() for c in line.strip().strip("|").split("|")])
    return out


# --- Dimensiones ---
dims = {}
for f in sorted(glob.glob(str(DIMDIR / "M[1-8]-*.md"))):
    p = Path(f)
    t = p.read_text(encoding="utf-8")
    code = p.name.split("-")[0]
    title = re.search(r"^# (.+)$", t, re.M).group(1).strip()
    s6 = titulo_seccion(t, 6)
    s12 = titulo_seccion(t, 12)
    sen = []
    for r in filas(seccion(t, 6))[1:]:
        if r and r[0].startswith("S-"):
            sen.append({"id": r[0], "senal": r[1], "cipher": r[2], "porque": r[3], "fecha": r[-1]})
    ind = []
    for r in filas(seccion(t, 12))[1:]:
        if len(r) >= 5:
            ind.append({"indicador": r[0], "base": r[1], "umbral": r[2], "fuente": r[3], "frecuencia": r[4]})
    dims[code] = {"file": p.name, "title": title, "a6": slug(s6) if s6 else None,
                  "a12": slug(s12) if s12 else None, "sen": sen, "ind": ind}

# --- Escenarios: qué señales cita cada uno en «Señales de hoy que apuntan aquí» ---
apunta = collections.defaultdict(list)
for e in ["E1", "E2", "E3", "E4"]:
    f = next(ESC.glob(f"{e}-*.md"))
    t = f.read_text(encoding="utf-8")
    m = re.search(r"^## Señales de hoy que apuntan aquí\s*$(.*?)(?=^## |\Z)", t, re.S | re.M)
    bloque = m.group(1) if m else ""
    for sid in sorted(set(re.findall(r"\b(?:S-M\d-\d{2}|D25-\d{2})\b", bloque))):
        apunta[sid].append(e)
ESC_FILES = {e: next(ESC.glob(f"{e}-*.md")).name for e in ["E1", "E2", "E3", "E4"]}


def apunta_txt(sid, base):
    es = apunta.get(sid, [])
    return ", ".join(f"[{e}]({base}06-escenarios-2040/{ESC_FILES[e]})" for e in es) if es else "—"


links = []  # (archivo_origen, destino_relativo)


def L(origen, texto, destino):
    links.append((origen, destino))
    return f"[{texto}]({destino})"


def cap(s):
    s = s.strip()
    return s[:1].upper() + s[1:] if s else s


# --- 03-senales/README.md ---
O3 = repo / "03-senales" / "README.md"
ORDEN_REL = {"Directa": 0, "Indirecta": 1, "Contexto": 2}


def num(x):
    try:
        return int(str(x).strip()[:1])
    except Exception:
        return 0


fichas_ord = sorted(fichas, key=lambda f: (ORDEN_REL.get(f["relevancia"], 3), -num(f["impacto"]) * num(f["evidencia"]), f["id"]))
out = []
# Resumen
tot_s = sum(len(d["sen"]) for d in dims.values())
out.append(f"Total: **{len(fichas)} señales del diccionario D25** y **{tot_s} de la investigación 2026** (S-Mx).\n")
out.append("| Dimensión | D25: fichas que la tocan | S-Mx: señales de la dimensión |")
out.append("|---|---|---|")
for code, d in dims.items():
    n25 = sum(1 for f in fichas if code in (f["dims"] if isinstance(f["dims"], list) else [f["dims"]]))
    out.append(f"| {L(O3, code + ' · ' + d['title'].split('·', 1)[-1].strip(), '../02-sistema-movilidad/dimensiones/' + d['file'])} | {n25} | {len(d['sen'])} |")
out.append("")
cip = collections.Counter(s["cipher"] for d in dims.values() for s in d["sen"])
out.append("| Tipo CIPHER (S-Mx) | Señales |")
out.append("|---|---|")
for k, v in cip.most_common():
    out.append(f"| {k} | {v} |")
out.append("")
esc_count = collections.Counter(e for sid, es in apunta.items() for e in es)
out.append("| Escenario | Señales que lo anticipan hoy |")
out.append("|---|---|")
for e in ["E1", "E2", "E3", "E4"]:
    out.append(f"| {L(O3, e, '../06-escenarios-2040/' + ESC_FILES[e])} | {esc_count.get(e, 0)} |")
out.append("")
out.append("### Señales prioritarias del diccionario para la movilidad\n")
out.append("Relevancia directa o indirecta, ordenadas por impacto × solidez (valoración propia ➕).\n")
out.append("| ID | Señal | En una línea | Relevancia | Impacto | Solidez | Plazo | Apunta a |")
out.append("|---|---|---|---|---|---|---|---|")
for f in fichas_ord:
    if f["relevancia"] in ("Directa", "Indirecta"):
        out.append(f"| {L(O3, f['id'], 'diccionario-2025/' + f['file'])} | {f['titulo']} | {cap(f['linea'])} | {f['relevancia']} | {f['impacto']} | {f['evidencia']} | {f['plazo']} | {apunta_txt(f['id'], '../')} |")
out.append("")
out.append("### Diccionario D25: las 40 señales\n")
out.append("| ID | Señal | Relevancia | Dimensiones | Impacto | Solidez | Plazo | Dirección | Apunta a |")
out.append("|---|---|---|---|---|---|---|---|---|")
for f in sorted(fichas, key=lambda f: f["id"]):
    dd = ", ".join(f["dims"]) if isinstance(f["dims"], list) else f["dims"]
    out.append(f"| {L(O3, f['id'], 'diccionario-2025/' + f['file'])} | {f['titulo']} | {f['relevancia']} | {dd} | {f['impacto']} | {f['evidencia']} | {f['plazo']} | {f['direccion']} | {apunta_txt(f['id'], '../')} |")
out.append("")
out.append("### Investigación 2026: señales por dimensión\n")
for code, d in dims.items():
    out.append(f"#### {d['title']}\n")
    out.append(f"Detalle y fuentes: {L(O3, code + ', sección 6', '../02-sistema-movilidad/dimensiones/' + d['file'] + '#' + d['a6'])}.\n")
    out.append("| ID | Señal | Tipo | Por qué es señal | Fecha | Apunta a |")
    out.append("|---|---|---|---|---|---|")
    for s in d["sen"]:
        out.append(f"| {s['id']} | {s['senal']} | {s['cipher']} | {s['porque']} | {s['fecha']} | {apunta_txt(s['id'], '../')} |")
    out.append("")
esc_dir = repo / "03-senales" / "escaneo-2026"
nuevas = sorted(p.name for p in esc_dir.glob("S-*.md"))
out.append("### Escaneo 2026: fichas nuevas\n")
if nuevas:
    for n in nuevas:
        out.append(f"- {L(O3, n[:-3], 'escaneo-2026/' + n)}")
else:
    out.append("Todavía no hay fichas nuevas. Para agregar una, sigue " + L(O3, "escaneo-2026/README.md", "escaneo-2026/README.md") + ".")
tablero = "\n".join(out).rstrip() + "\n"

# --- 09-monitoreo/README.md ---
O9 = repo / "09-monitoreo" / "README.md"
out = []
tot_i = 0
for code, d in dims.items():
    out.append(f"### {d['title']}\n")
    out.append(f"Detalle: {L(O9, code + ', sección 12', '../02-sistema-movilidad/dimensiones/' + d['file'] + '#' + d['a12'])}.\n")
    out.append("| Indicador | Línea base | Umbral de alerta | Fuente | Frecuencia |")
    out.append("|---|---|---|---|---|")
    for i in d["ind"]:
        out.append(f"| {i['indicador']} | {i['base']} | {i['umbral']} | {i['fuente']} | {i['frecuencia']} |")
        tot_i += 1
    out.append("")
lista = f"Total: {tot_i} indicadores en {len(dims)} dimensiones.\n\n" + "\n".join(out).rstrip() + "\n"


def reemplazar(path, ini, fin, contenido):
    t = path.read_text(encoding="utf-8")
    a, b = t.index(ini), t.index(fin)
    path.write_text(t[: a + len(ini)] + "\n" + contenido + t[b:], encoding="utf-8")


reemplazar(O3, "<!-- TABLERO:INICIO -->", "<!-- TABLERO:FIN -->", tablero)
reemplazar(O9, "<!-- INDICADORES:INICIO -->", "<!-- INDICADORES:FIN -->", lista)

# --- Verificación de enlaces generados ---
malos = []
for origen, dest in links:
    ruta, _, ancla = dest.partition("#")
    tgt = (origen.parent / ruta).resolve()
    if not tgt.exists():
        malos.append((origen.name, dest, "no existe"))
    elif ancla and ancla not in headings(tgt):
        malos.append((origen.name, dest, "ancla inexistente"))
print(f"Tablero: {len(fichas)} D25 + {tot_s} S-Mx; señales con escenario: {len(apunta)}; indicadores: {tot_i}")
print(f"Enlaces generados: {len(links)}; rotos: {len(malos)}")
for m in malos:
    print("  ROTO", m)
sys.exit(1 if malos else 0)
````
