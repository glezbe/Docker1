from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

print("ESTOY EN EL MAIN NUEVO ✅")


app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

#cambio tareas por incidencias
INCIDENCIAS = [
    {"id": 1, "titulo": "Caída intermitente de la red WiFi", "categoria": "red", "gravedad": 4, "resuelta": False},
    {"id": 2, "titulo": "Disco duro con sectores defectuosos", "categoria": "hardware", "gravedad": 5, "resuelta": True},
    {"id": 3, "titulo": "Error al iniciar sesión en el ERP", "categoria": "software", "gravedad": 3, "resuelta": False},
    {"id": 4, "titulo": "Latencia alta en VPN", "categoria": "red", "gravedad": 2, "resuelta": True},
    {"id": 5, "titulo": "Actualización falla por dependencias", "categoria": "software", "gravedad": 4, "resuelta": True},
    {"id": 6, "titulo": "Fuente de alimentación inestable", "categoria": "hardware", "gravedad": 3, "resuelta": False},
]



@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "contenido": "<p>Ve a <a href='/informe'>/informe</a> para ver el informe.</p>",
        },
    )


@app.get("/informe", response_class=HTMLResponse)
async def informe(
    request: Request,
    categoria: Optional[str] = Query(None, description="Filtrar por categoria"),
    min_gravedad: int = Query(1, ge=1, le=5, description="Gravedad minima"),
):
    categorias_validas = {"red", "hardware", "software"}

    if categoria is not None:
        categoria = categoria.strip().lower()

    if not categoria or categoria not in categorias_validas:
        categoria = None

    incidencias_filtradas = []
    for incidencia in INCIDENCIAS:
        if categoria is not None and incidencia["categoria"] != categoria:
           continue
        if incidencia["gravedad"] < min_gravedad:
            continue
        incidencias_filtradas.append(incidencia)

    total_incidencias = len(incidencias_filtradas)
    resueltas = sum(1 for incidencia in incidencias_filtradas if incidencia["resuelta"])
    porcentaje_resueltas = (resueltas / total_incidencias * 100) if total_incidencias > 0 else 0

    resumen = {
        "total": total_incidencias,
        "resueltas": resueltas,
        "porcentaje_resueltas": round(porcentaje_resueltas, 2),
    }

    categorias_posibles = ["red", "hardware", "software"]
    labels = categorias_posibles
    values = [sum(1 for inc in incidencias_filtradas if inc["categoria"] == c) for c in categorias_posibles]

    gravedades = [1, 2, 3, 4, 5]
    labels_gravedad = gravedades
    values_gravedad = [sum(1 for inc in incidencias_filtradas if inc["gravedad"] == g)for g in gravedades]

    
    return templates.TemplateResponse(
        "informe.html",
        {
            "request": request,
            "incidencias": incidencias_filtradas,
            "resumen": resumen,
            "labels": labels,
            "values": values,
            "labels_gravedad": labels_gravedad,
            "values_gravedad": values_gravedad,
            "categoria": categoria,
            "min_gravedad": min_gravedad,
        },
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
