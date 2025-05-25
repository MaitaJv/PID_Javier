import sys
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from integrator import pickDate, pickTime,pickNOAA, createInfo, addTexto, Info, Campo

def trim_image(image):
    BnW = image.convert("L")
    BnW_arr = np.array(BnW)
    colums_sum = BnW_arr.sum(axis=0)

    index_of_black_colums = np.where(colums_sum < 5000)[0]

    extrems = []

    for i in range(len(index_of_black_colums) - 1):
        if index_of_black_colums[i + 1] - index_of_black_colums[i] > 50:
            extrems.append(index_of_black_colums[i])
            extrems.append(index_of_black_colums[i + 1])
    
    image_trimmed = image.crop((extrems[0], 0, extrems[1], image.height))
    image_trimmed_rgb = image_trimmed.convert("RGB")

    return image_trimmed_rgb