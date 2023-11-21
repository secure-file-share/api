import os
import base64
from datetime import datetime
from django.conf import settings
from alpha.utilities import parse_date
from base64 import b64encode, b64decode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SEPARATOR = "\n-----\n"


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


def encrypt_file(key, file_name, path):
    """
    Encrypt file. 
    The temporary encryption file is not deleted by this function!
    """

    with open(path, "br") as binary_file:
        # READ FILE
        read_file = binary_file.read()
        encoded_data = b64encode(read_file)

    # CREATE FILE NAME TO WRITE
    file_name += ".securefileshare"
    file_path = settings.BASE_PATH / "temp" / file_name

    with open(file_path, "bw") as write_file:
        # WRITE META DATA
        ext = path.split(os.path.sep).pop().split(".").pop()
        meta = "{} | Encrypted By SecureFileShare (Lewis 2023) Made by Aashirwad Satshree Dristi, {} | {}\n".format(
            ext,
            parse_date(datetime.now(), format="%b. %m, %Y %H:%M:%S"),
            encipher(key, generate_key("BACKUP")).decode("utf-8")
        )
        write_file.write(meta.encode())

        # WRITE SEPARATOR
        write_file.write(SEPARATOR.encode())

        # ENCRYPT DATA
        enc = encipher(encoded_data.decode("utf-8"), key)

        # WRITE ENCRYPTED DATA
        write_file.write(enc)

    return file_path


def decrypt_file(key, file_name, path):
    """
    Decrypt file.
    The temporary decryption file is not deleted by this function!
    """

    with open(path, "r") as read_file:
        # READ FILE
        content = read_file.read()

        # READ META INFORMATION
        meta = content.split(SEPARATOR)[0]

        # GET ORIGINAL FILE EXTENSION FROM HEADER
        ext = ".{}".format(
            meta.split(" | ")[0]
        )

        # CREATE ORIGINAL FILE NAME
        file_name += ext
        file_path = settings.BASE_PATH / "temp" / file_name

        # GET FILE CONTENTS
        file_content = content.split(SEPARATOR)[-1].encode()

    # DECRYPT DATA
    dec = decipher(file_content.decode("utf-8"), key)

    if dec == 0:
        # KEY MISMATCH
        raise Exception("Key Mismatch")

    with open(file_path, "bw") as write_file:

        # WRITE DECRYPTED DATA
        write_file.write(b64decode(dec))

    return file_path
