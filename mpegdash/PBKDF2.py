import hashlib
import os
import uuid
import binascii

# === PARAMETERS ===
password = b"DRMExample"             # Use a strong password
salt = os.urandom(16)                          # Generate 16-byte random salt
iterations = 100000
key_length = 16                                # 16 bytes = 128-bit key for AES-128

# === PBKDF2 KEY DERIVATION ===
key = hashlib.pbkdf2_hmac(
    hash_name='sha256',
    password=password,
    salt=salt,
    iterations=iterations,
    dklen=key_length
)

# === GENERATE KID ===
kid = uuid.uuid4().bytes                       # Random 128-bit key ID

# === OUTPUT ===
print("KID (hex):", binascii.hexlify(kid).decode())
print("Key (hex):", binascii.hexlify(key).decode())
print("Salt (hex):", binascii.hexlify(salt).decode())
