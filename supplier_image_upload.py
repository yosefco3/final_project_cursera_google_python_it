#!/usr/bin/env python3
import requests
import os


path = "./supplier-data/images"
url = "http://<username>/upload/"
for img in os.listdir(path):
    if img[-4:] == "jpeg":
        print(img)
        with open(os.path.join(path, img), "rb") as opened:
            r = requests.post(url, files={"file": opened})
            print(r.status_code)
