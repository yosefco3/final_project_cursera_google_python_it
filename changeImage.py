#!/usr/bin/env python3
from PIL import Image
import os

path = "./supplier-data/images"

for im in os.listdir(path):
    try:
        img = Image.open(os.path.join(path, im))
        img = img.convert("RGB")
        width, height = img.size
        new_width = 600
        new_height = 400
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(os.path.join(path, im.replace(".tiff", ".jpeg")))
    except Exception as e:
        print(e)
