from utils.pem_to_key import read_public_key, read_private_key
from utils.encode_to_utf8 import encode_str_utf8
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

message = encode_str_utf8("I love you baby")

public_key = read_public_key()
private_key = read_private_key()


def encrypt_message(message):
    return public_key.encrypt(
        message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )


encrypted_message = encrypt_message(message)


def decrypt_message(encrypted_message):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    ).decode()


print(decrypt_message(encrypted_message))
