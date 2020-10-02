#! /usr/bin/env python3
import os
import requests

path = "./supplier-data/descriptions/"
url = "http://<username>/fruits/"

for fruit in os.listdir(path):
    if fruit[-3:] == "txt":
        fruit_p = os.path.join(path, fruit)
        with open(fruit_p, "r") as f:
            f = f.read().split("\n")
            f[1] = int(f[1].split(" lbs")[0])
            f = [x for x in f if x != ""]
            d = dict(zip(["name", "weight", "description"], f))
            d["image_name"] = fruit[:-4] + ".jpeg"
            r = requests.post(url, data=d)
            print(r.status_code)
