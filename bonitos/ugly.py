#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
#umm boop bop bah duu

files = []

for file in os.listdir():
    if file == "ransom.py" or file == "dict" or file == "ugly.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("dict", "rb") as key:
    secretKey = key.read()

for file in files: 
    with open(file, "rb") as bFiles:
        contents = bFiles.read()
    contents_ugly = Fernet(secretKey).decrypt(contents)
    with open(file, "wb") as bFile:
        bFile.write(contents_ugly)
