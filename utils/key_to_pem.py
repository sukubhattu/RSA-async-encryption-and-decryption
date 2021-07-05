from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from .encode_to_utf8 import encode_str_utf8

import os
from dotenv import load_dotenv

load_dotenv('.env')

PASSWORD = os.environ.get("PASSWORD")

private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)  # default backend is used automatically. RSABackend is optional backend
public_key = private_key.public_key()


def write_private_key():
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(encode_str_utf8(str(PASSWORD))),
    )


def write_public_key():
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


with open('private_key.pem', 'wb') as f:
    f.write(write_private_key())


with open('public_key.pem', 'wb') as f:
    f.write(write_public_key())
