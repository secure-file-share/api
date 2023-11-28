import os
import base64
from io import BytesIO
from datetime import datetime
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
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


def encrypt_file(key, file_instance):
    """
    Encrypt file. 
    The temporary encryption file is not deleted by this function!
    """

    # ENCRYPTION KEY
    key = generate_key(key)

    # READ FILE
    encoded_data = b64encode(file_instance.read())

    # CREATE FILE NAME TO WRITE
    og_file_name = file_instance.name.split(
        os.path.sep).pop()
    file_name = (og_file_name + ".securefileshare").replace(" ", "_")
    file_path = os.path.join(settings.BASE_DIR, "temp", file_name)

    with open(file_path, "wb") as write_file:
        # WRITE META DATA
        ext = og_file_name.split(".").pop()  # GET FILE EXTENSION
        meta = "{} | Encrypted By SecureFileShare (Lewis 2023) Made by Aashirwad Satshree Dristi, {} | {}".format(
            # FILE EXTENSION
            ext,
            # ENCRYPTED DATE
            parse_date(datetime.now(), format="%b. %m, %Y %H:%M:%S"),
            # ENCRYPT THE KEY WITH BACKUP KEY; used to recover key
            encipher(key.decode("utf-8"),
                     generate_key("BACKUP")).decode("utf-8")
        )
        write_file.write(meta.encode())

        # WRITE SEPARATOR
        write_file.write(SEPARATOR.encode())

        # ENCRYPT DATA
        enc = encipher(encoded_data.decode("utf-8"), key)

        # WRITE ENCRYPTED DATA
        write_file.write(enc)

    # RETURN ENCRYPTED FILE
    encrypted_file = File(file=open(file_path), name=file_name)

    return encrypted_file


def decrypt_file(key, file_instance):
    """
    Decrypt file.
    """

    # DECRYPTION KEY
    key = generate_key(key)

    # READ FILE
    content = file_instance.read().decode("utf-8")

    # READ META INFORMATION
    meta = content.split(SEPARATOR)[0]

    # GET ORIGINAL FILE EXTENSION FROM HEADER
    ext = ".{}".format(
        meta.split(" | ")[0]
    )

    # CREATE ORIGINAL FILE NAME
    file_name = file_instance.name.split(
        os.path.sep).pop().split(".").pop() + ext
    # file_path = settings.BASE_DIR / "temp" / file_name

    # GET FILE CONTENTS
    file_content = content.split(SEPARATOR)[-1].encode()

    # DECRYPT DATA
    dec = decipher(file_content.decode("utf-8"), key)

    if dec == 0:
        # KEY MISMATCH
        raise Exception("Key Mismatch")

    file_contents = BytesIO(b64decode(dec))
    content_file = ContentFile(file_contents.getvalue(), file_name)

    return content_file
