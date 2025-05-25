import sys
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from integrator import pickDate, pickTime, pickNOAA, createInfo, addTexto, Info, Campo
from trimmer import trim_image

#Creo los campos
time = Campo.TIME
date = Campo.DATE
noaa = Campo.NOAA

# recibe del argumento el nombre del archivo
img_path = sys.argv[1]

# lo convierto es un ImageFile para trabajarlo
crud_image = Image.open(img_path)

image = trim_image(crud_image)

# Defino fuente a utilizar y creo Draw
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("DejaVuSans.ttf", size=20)

data_time = createInfo(draw, img_path, font, time)
addTexto(draw, font, image, data_time, time)

data_date = createInfo(draw, img_path, font, date)
addTexto(draw, font, image, data_date, date)

data_noaa = createInfo(draw, img_path, font, noaa)
addTexto(draw, font, image, data_noaa, noaa)

# Agregar logo
logo = Image.open("logo3.png").convert("RGBA")
logo = logo.resize((200, 100))
image.paste(logo, (image.width - 280, 10), logo)

os.makedirs("processed-images/", exist_ok=True)
new_path = "processed-images/" + sys.argv[1][:38] + "_processed.png"

#imagen.show()
image.save(new_path)
