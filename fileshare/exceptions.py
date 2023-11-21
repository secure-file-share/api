class EncryptionKeyMismatch(Exception):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)
        self.message = "Encryption Key Mismatch"
