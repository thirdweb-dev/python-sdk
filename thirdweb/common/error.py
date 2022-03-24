class NoSignerException(Exception):
    def __init__(self):
        super().__init__(
            (
                "You need to pass a valid signer to the SDK to use this function."
                "Please use the `update_signer` method of the SDK to set a valid signer."
                "You can create a signer using the `Account.from_key(<private_key>)` method."
            )
        )
