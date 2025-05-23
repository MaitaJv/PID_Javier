from dataclasses import dataclass
from enum import Enum
from PIL import Image, ImageDraw, ImageFont

#Estructuras

@dataclass
class Info:
    size: tuple[float, float]
    text: str

class Campo(Enum):
    TIME = 0,
    DATE = 1,
    NOAA = 2

def pickTime(fileName):
    parts = fileName.split("_")
    time = parts[4][:6]
    
    return time[:2] + ":" + time[2:4] + ":" + time[4:]

def pickDate(fileName):
    parts = fileName.split("_")
    date = parts[3][:8]
    
    return date[:4] + "/" + date[4:6] + "/" + date[6:]

def pickNOAA(fileName):
    parts = fileName.split("_")
    
    return parts[0] + " " + parts[1]

def createInfo(draw, img_path, font, campo):
    if campo == Campo.TIME: text = "Hora de captura: " + pickTime(img_path)
    if campo == Campo.DATE: text = "Fecha de captura: " + pickDate(img_path)
    if campo == Campo.NOAA: text = "Capturado por: " + pickNOAA(img_path)

    bbox = draw.textbbox((0, 0), text, font=font)
    text_size = (bbox[2] - bbox[0], bbox[3] - bbox[1])
    
    return Info(size = text_size, text = text)

def addTexto(draw, font, image, data_hora, campo):

    if campo == Campo.TIME: height = image.height - 20
    if campo == Campo.DATE: height = image.height - 50
    if campo == Campo.NOAA: height = image.height - 80

    draw.rectangle([(80, height), (80 + data_hora.size[0] + 5, height + data_hora.size[1] + 5)], fill=(0,0,0))
    draw.text((80, height), data_hora.text, fill="white", font=font)