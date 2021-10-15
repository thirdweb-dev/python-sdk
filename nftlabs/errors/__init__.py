
class NoSignerException(Exception):
    def __init__(self):
        super().__init__("No signer (private key) supplied to SDK")
