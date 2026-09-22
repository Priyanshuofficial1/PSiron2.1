from hashlib import sha256
from pathlib import Path

def hash_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()

def hash_file(path: str | Path) -> str:
    h = sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()
