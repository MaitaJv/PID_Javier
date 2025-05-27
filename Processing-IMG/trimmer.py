import numpy as np
from PIL import Image

def trim_images(image):
    BnW = image.convert("L")
    BnW_arr = np.array(BnW)
    colums_sum = BnW_arr.sum(axis=0)

    index_of_black_colums = np.where(colums_sum < 5000)[0]

    extrems = []

    for i in range(len(index_of_black_colums) - 1):
        if index_of_black_colums[i + 1] - index_of_black_colums[i] > 50:
            extrems.append(index_of_black_colums[i])
            extrems.append(index_of_black_colums[i + 1])
    
    if (image.width - index_of_black_colums[len(index_of_black_colums) - 1]) > 50:
        extrems.append(index_of_black_colums[len(index_of_black_colums) - 1])

    images_trimmeds = []
    print(extrems)
    for i in range(len(extrems)):
        print(i)
        if (i == 0): 
            continue
        if (i % 2 == 0): 
            image_cuted = image.crop((extrems[i - 2], 0, extrems[i - 1], image.height))
            image_cuted.convert("RGB")
            images_trimmeds.append(image_cuted)
    
        if (i == len(extrems) - 1):
            image_cuted = image.crop((extrems[i], 0, image.width, image.height))
            image_cuted.convert("RGB")
            images_trimmeds.append(image_cuted)

    return images_trimmeds