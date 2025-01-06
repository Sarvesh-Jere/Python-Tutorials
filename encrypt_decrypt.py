import base64
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import os, sys
from loguru import logger

try:
    key = "key1"
    iv = "my_username_pass"
    salt = "salt"

    if not (key and iv and salt):
        raise Exception(F"Error while fetching details for key/iv/salt")
except Exception as e:
    logger.error("Error occurred. Details: %s", e)
    sys.exit(0)

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s: s[0:-ord(s[-1:])]

def get_private_key():
    Salt = salt.encode('utf-8')
    kdf = PBKDF2(key, Salt, 64, 1000)
    key32 = kdf[:32]
    return key32


def encrypt(raw):
    raw = pad(raw)
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    return base64.b64encode(cipher.encrypt(raw))


def decrypt(enc):
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    return unpad(cipher.decrypt(base64.b64decode(enc))).decode('utf8')

print(encrypt("manish"))
print(decrypt("U1AMRIQSTYosVJCmmqUHnA=="))