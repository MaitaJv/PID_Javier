from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar la carpeta "static" para servir archivos como imágenes, CSS, JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Motor de plantillas
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
