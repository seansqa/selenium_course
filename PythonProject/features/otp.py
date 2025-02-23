import base64
import hashlib
import struct
import time
import os

KEY = os.getenv('KEY')

if not KEY:
    raise ValueError('KEY env var was not found')

def totp(key: str) -> str:
    X = 30  # 30-second timeout
    K = base32_decode(key)
    return hotp(K, number_to_bytes(int(time.time() // X)))

def hotp(K: bytes, C: bytes) -> str:
    HS = hashlib.sha1(K + C).digest()
    offset = HS[19] & 0xf
    code = (
        (HS[offset] & 0x7f) << 24 |
        (HS[offset + 1] & 0xff) << 16 |
        (HS[offset + 2] & 0xff) << 8 |
        (HS[offset + 3] & 0xff)
    )
    return str(code % 10 ** 6).zfill(6)

def base32_decode(key: str) -> bytes:
    # Add padding if necessary to make the length a multiple of 8
    padding = len(key) % 8
    if padding:
        key += '=' * (8 - padding)
    return base64.b32decode(key.upper())

def number_to_bytes(n: int) -> bytes:
    return struct.pack('>Q', n)[4:]

print(totp(KEY))