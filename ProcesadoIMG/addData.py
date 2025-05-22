import sys
import os
from PIL import Image, ImageDraw, ImageFont
from utils import conseguirFecha, conseguirHora,conseguirNOAA, crearInfo, agregarTexto, Info, Campo

#Creo los campos
hora = Campo.HORA
fecha = Campo.FECHA
noaa = Campo.NOAA

# recibe del argumento el nombre del archivo
img_path = sys.argv[1]

# lo convierto es un ImageFile para trabajarlo
imagen = Image.open(img_path)
#print(imagen.mode)

# Defino fuente a utilizar y creo Draw
draw = ImageDraw.Draw(imagen)
font = ImageFont.truetype("DejaVuSans.ttf", size=20)

data_hora = crearInfo(draw, img_path, font, hora)
agregarTexto(draw, font, imagen, data_hora, hora)

data_fecha = crearInfo(draw, img_path, font, fecha)
agregarTexto(draw, font, imagen, data_fecha, fecha)

data_noaa = crearInfo(draw, img_path, font, noaa)
agregarTexto(draw, font, imagen, data_noaa, noaa)

# Agregar logo
logo = Image.open("logo3.png").convert("RGBA")
logo = logo.resize((200, 100))
imagen.paste(logo, (imagen.width - 280, 10), logo)

os.makedirs("imagenesProcesadas/", exist_ok=True)
nuevo_path = "imagenesProcesadas/" + sys.argv[1][:38] + "_procesada.png"

#imagen.show()
imagen.save(nuevo_path)
