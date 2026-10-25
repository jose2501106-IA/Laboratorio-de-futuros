"""Arma app/dist/trama.html: un solo archivo con la app, la red real y los datos sintéticos.

Uso: python3 app/build.py
- Quita el envoltorio de desarrollo (<!--DEV:START--> … <!--DEV:END-->): el artifact pone su propio <html>/<head>/<body>.
- Mete adentro data/red.js y data/sintetico.js. Si falta sintetico.js, la app usa su respaldo mínimo (también SINTÉTICO).
"""
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
html = (AQUI / "index.html").read_text(encoding="utf-8")
html = re.sub(r"<!--DEV:START-->.*?<!--DEV:END-->", "", html, flags=re.S)

def inline(nombre):
    ruta = AQUI / "data" / nombre
    etiqueta = f'<script src="data/{nombre}"></script>'
    if ruta.exists():
        js = ruta.read_text(encoding="utf-8").replace("</script", "<\\/script")
        return html.replace(etiqueta, f"<script>\n{js}\n</script>"), True
    return html.replace(etiqueta, f"<!-- falta data/{nombre}: se usa el respaldo -->"), False

html, ok_red = inline("red.js")
html, ok_sint = inline("sintetico.js")
salida = AQUI / "dist" / "trama.html"
salida.parent.mkdir(exist_ok=True)
salida.write_text(html.strip() + "\n", encoding="utf-8")
print(f"{salida} · {salida.stat().st_size/1024:.0f} KB · red.js: {'sí' if ok_red else 'NO'} · sintetico.js: {'sí' if ok_sint else 'NO (respaldo)'}")
