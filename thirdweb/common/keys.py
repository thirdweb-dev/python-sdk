import hashlib

def derive_client_id_from_secret_key(secret_key: str) -> str:
    hashed = hashlib.sha256(secret_key.encode()).hexdigest()
    return hashed[:32]