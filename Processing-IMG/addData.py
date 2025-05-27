import sys
import os
from PIL import Image, ImageDraw, ImageFont
from integrator import integrate_to_image, Campo
from trimmer import trim_images

#Creo los campos
time = Campo.TIME
date = Campo.DATE
noaa = Campo.NOAA

# recibe del argumento el nombre del archivo
img_path = sys.argv[1]

# lo convierto es un ImageFile para trabajarlo
crud_image = Image.open(img_path)

images = trim_images(crud_image)
print(images)

processed_images = []

for img in images:
    processed_image = integrate_to_image(img, img_path)
    processed_images.append(processed_image)
    
os.makedirs("processed-images/", exist_ok=True)

count = 0
while count < len(processed_images):
    new_path = "processed-images/" + sys.argv[1][:38] + f"_processed_0{count}.png"
    #imagen.show()
    processed_images[count].save(new_path)
    count += 1


