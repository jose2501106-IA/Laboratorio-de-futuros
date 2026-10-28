# Plantilla · Dimensión del sistema de movilidad

Cada dimensión (M1 a M8) se documenta con esta estructura. M9, la dimensión transversal, tiene su propia estructura descrita en su archivo.

Reglas:

- Español de México, claro y directo.
- Cada cifra lleva su fuente numerada [n] y su fecha. No se inventan cifras, citas ni enlaces.
- Etiquetas: **[supuesto]** para valores propuestos, **[inferencia]** para conclusiones propias y **[por verificar]** para datos que no se pudieron confirmar.
- Presente = 2024 a 2026. El pasado solo se usa para dar dirección y ritmo a una tendencia; las cronologías van en `01-historicos-2006-2026/`.
- Horizonte 2040, con cortes en 2027, 2030, 2035 y 2040.

## Estructura

```markdown
# Mx · Nombre de la dimensión

> Resumen en 5 líneas: qué está pasando, hacia dónde va y qué está en juego.

## 1. Alcance
Qué cubre esta dimensión y qué queda en otras (con su código).

## 2. Estado actual (2024-2026)
Texto breve y tabla de indicadores clave.

| Indicador | Valor | Año | Fuente |
|---|---|---|---|

## 3. Actores
| Actor | Rol | Poder (alto/medio/bajo) | Interés (alto/medio/bajo) | Postura |
|---|---|---|---|---|

## 4. Impulsores de cambio (STEEP)
| Impulsor | Tipo STEEP | Evidencia [n] | Dirección | Fuerza (1-5) |
|---|---|---|---|---|

## 5. Tendencias
Cada tendencia con su dirección, su ritmo y los datos que la sostienen.

## 6. Señales emergentes (2025-2026)
| ID | Señal | Tipo CIPHER | Por qué es señal | Fuente [n] | Fecha |
|---|---|---|---|---|---|
CIPHER: Contradicción, Inflexión, Práctica nueva, Hackeo, Extremo, Rareza.
IDs: S-Mx-01, S-Mx-02…

## 7. Incertidumbres críticas
Entre 3 y 5. Para cada una: por qué importa y sus dos extremos plausibles al 2040.

## 8. Comodines
Entre 3 y 5 eventos de baja probabilidad y alto impacto, con su efecto en la movilidad.

## 9. Conexiones sistémicas
| Variable A | → Variable B | Signo (+/−) | Demora (corta/media/larga) | Dimensión de B | Evidencia [n] o [inferencia] |
|---|---|---|---|---|---|
Al menos 8, varias con otras dimensiones (M1 a M8).

## 10. Futuros oficiales y metas
Qué prometen los planes vigentes para 2030-2040 en esta dimensión y qué tan creíble es cada meta.

## 11. Escenarios 2040 de la dimensión (arquetipos de Dator)
### Continuidad (tendencial)
### Colapso
### Disciplina
### Transformación
Para cada uno: narrativa de 120 a 180 palabras, de 3 a 5 indicadores con su valor en 2040 [supuesto] y las señales de hoy que apuntan hacia ahí.

## 12. Qué vigilar
| Indicador | Línea base | Umbral de alerta | Fuente de datos | Frecuencia |
|---|---|---|---|---|

## 13. Preguntas abiertas y datos faltantes

## 14. Fuentes
[n] Institución o medio. *Título*. URL. Fecha de publicación. Consultado el AAAA-MM-DD.
```
