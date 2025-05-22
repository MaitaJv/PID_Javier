from dataclasses import dataclass
from enum import Enum
from PIL import Image, ImageDraw, ImageFont

#Estructuras

@dataclass
class Info:
    tamanio: tuple[float, float]
    text: str

class Campo(Enum):
    HORA = 0,
    FECHA = 1,
    NOAA = 2

def conseguirHora(cadena):
    partes = cadena.split("_")
    hora = partes[4][:6]
    
    return hora[:2] + ":" + hora[2:4] + ":" + hora[4:]

def conseguirFecha(cadena):
    partes = cadena.split("_")
    fecha = partes[3][:8]
    
    return fecha[:4] + "/" + fecha[4:6] + "/" + fecha[6:]

def conseguirNOAA(cadena):
    partes = cadena.split("_")
    
    return partes[0] + " " + partes[1]

def crearInfo(draw, img_path, font, campo):
    if campo == Campo.HORA: texto = "Hora de captura: " + conseguirHora(img_path)
    if campo == Campo.FECHA: texto = "Fecha de captura: " + conseguirFecha(img_path)
    if campo == Campo.NOAA: texto = "Capturado por: " + conseguirNOAA(img_path)

    bbox = draw.textbbox((0, 0), texto, font=font)
    tam_texto = (bbox[2] - bbox[0], bbox[3] - bbox[1])
    
    return Info(tamanio = tam_texto, text = texto)

def agregarTexto(draw, font, imagen, data_hora, campo):

    if campo == Campo.HORA: altura = imagen.height - 20
    if campo == Campo.FECHA: altura = imagen.height - 50
    if campo == Campo.NOAA: altura = imagen.height - 80

    draw.rectangle([(80, altura), (80 + data_hora.tamanio[0] + 5, altura + data_hora.tamanio[1] + 5)], fill=(0,0,0))
    draw.text((80, altura), data_hora.text, fill="white", font=font)