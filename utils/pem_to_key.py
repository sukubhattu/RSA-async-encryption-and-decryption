from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from .encode_to_utf8 import encode_str_utf8

import os
from dotenv import load_dotenv

load_dotenv('.env')

PASSWORD = os.environ.get("PASSWORD")


def read_private_key():
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(), password=encode_str_utf8(str(PASSWORD)), backend=default_backend()
        )
    return private_key


def read_public_key():
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())
    return public_key
