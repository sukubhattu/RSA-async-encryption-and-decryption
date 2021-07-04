from inspect import signature
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def verify_signature1(public_key, signature, message):
    return public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )


def verify_signature(func):
    def inner_wrapper(*args, **kwargs):
        message = kwargs['message']
        signature = kwargs['signature']
        public_key = kwargs['public_key']

        try:
            verify_signature1(public_key, signature, message)
            return func(*args, **kwargs)
        except InvalidSignature:
            print("Invalid signature")

    return inner_wrapper
