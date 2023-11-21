import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def generate_key(key):
    """Generate key for encryption/decryption."""

    # CONVERT THE KEY INTO BYTES
    password = key.encode()

    # SALT FOR SHA256 HASH
    salt = b'SecureFileShare__Lewis2023__AashirwadSatshreeDristi'

    # GENERATE HASH
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    # KEY FOR ENCRYPTION/DECRYPTION
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key


def encipher(message, key):
    """Encrypt"""

    plain_text = message.encode()

    f = Fernet(key)

    cipher = f.encrypt(plain_text)

    return cipher


def decipher(message, key):
    """Decrypt"""
    try:
        cipher_text = message.encode()

        f = Fernet(key)

        plain = f.decrypt(cipher_text)

        return plain
    except:
        return 0
