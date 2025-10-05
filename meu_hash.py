import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding, utils
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

meu_hash = hashlib.sha256(b'Minha senha').digest()


chave_privada = rsa.generate_private_key(key_size= 2056, public_exponent=65537)


assinatura = chave_privada.sign(
    meu_hash,
    padding.PSS(
        mgf= padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    utils.Prehashed(hashes.SHA256())
)


chave_publica = chave_privada.public_key()

try:
    chave_publica.verify(
        assinatura,
        meu_hash,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(hashes.SHA256())
    )
    print("Assinatura valida!")
except InvalidSignature:
    print("Assinatura invalida!")