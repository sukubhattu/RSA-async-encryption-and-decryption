from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def read_private_key():
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())
    return private_key


def read_public_key():
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())
    return public_key
