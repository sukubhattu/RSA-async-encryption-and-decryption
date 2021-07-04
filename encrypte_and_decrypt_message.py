from inspect import signature
from utils.pem_to_key import read_public_key, read_private_key
from utils.encode_to_utf8 import encode_str_utf8
from utils.decorators import verify_signature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

message = encode_str_utf8("I love you baby")

public_key = read_public_key()
private_key = read_private_key()


def encrypt_message(message):
    return public_key.encrypt(
        message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )


def generate_signature(message):
    return private_key.sign(
        message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256()
    )


encrypted_message = encrypt_message(message)
signature = generate_signature(message)

# print(encrypted_message)

"""
    Private key is used to sign message.

    This allows anyone with public key to verify that message was written using that private key.
"""


@verify_signature
def decrypt_message(encrypted_message, **kwargs):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    ).decode()


decrypted_message = decrypt_message(encrypted_message, message=message, signature=signature, public_key=public_key)
print(decrypted_message)
