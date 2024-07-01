#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "key.key" or file == "decrypt.py":
        pass
    else:
        if os.path.isfile(file):
            files.append(file)

print(files)

with open("key.key", "rb") as k:
    key = k.read()

for file in files:
    with open(file, "rb") as f:
        contents = f.read()
        contents_decrypted = Fernet(key).decrypt(contents)

    with open(file, "wb") as f:
        f.write(contents_decrypted)

print("Your files has been decrypted")

