# Práctica DI – RA5
## Informe web de incidencias con FastAPI + Jinja2

La empresa quiere un informe web sencillo sobre incidencias de un sistema. Implementa una app con **FastAPI** y **Jinja2** que:

- Tenga una ruta `/informe` que genere un informe HTML a partir de una lista de incidencias.
- Permita filtrar por:
  - `categoria` (`red` / `hardware` / `software`)
  - `min_gravedad` (número mínimo de `1` a `5`)
- Muestre en el informe:
  - Un resumen (nº incidencias, nº resueltas, % resueltas).
  - Una tabla con las incidencias filtradas.
  - Un gráfico (Chart.js) con incidencias por categoría.
- Use plantillas Jinja2 (`base.html` + `informe.html`).

### Modificación obligatoria de la plantilla
Modifica la plantilla **al menos una vez**:

- añade una nueva sección/columna **o** un segundo gráfico,
- y explica el cambio en la memoria.

## Datos de entrada
Puedes:

- usar una lista en el código (hardcodeada como la anterior), **o**
- cargar un JSON simple.


## Entregables
- `main.py`
- `templates/base.html` y `templates/informe.html`
- Captura del informe con algún filtro aplicado
- Memoria corta explicando:
  - estructura del informe,
  - filtros usados,
  - cálculos de totales,
  - cambio realizado en la plantilla.
  - Subirlo a gh con el readme explicandolo y caps

