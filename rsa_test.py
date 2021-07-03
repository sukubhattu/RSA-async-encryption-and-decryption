# asymmetric using rsa

# Steps
# 1. generate private key
# 2. generate public key from that private key
# 3. generate private.pem and public.pem
# 4. generate signature to sign a message
# 5. verify signature

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from utils.encode_to_utf8 import encode_str_utf8


def generate_private_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )  # returns instance of RSAPrivateKey


def generate_public_key(private_key):
    return private_key.public_key()  # returns instance of RSAPublicKey


private_key = generate_private_key()
public_key = generate_public_key(private_key)

# print(private_key)
# print(public_key)


def generate_private_pem_key():
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(encode_str_utf8("my private password")),
    )


def generate_public_pem_key():
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


private_pem = generate_private_pem_key()
public_pem = generate_public_pem_key()


# sign message with your private key
message = encode_str_utf8('I love you baby')
signature = private_key.sign(
    message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256()
)
# print(signature)


# verify signature with public key. Verify if original person with private key has written that message.
def verify_signature(signature):
    return public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )


# print(verify_signature(signature))


""" 
Now real encryption starts here
"""

message = encode_str_utf8("I love you baby. This message should be encrypted")


def encrypt_message(message):
    return public_key.encrypt(
        message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )


def decrypt_message(encrypted_message):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    ).decode()


encrypted_message = encrypt_message(message)
decrypted_message = decrypt_message(encrypted_message)

print(decrypted_message)
