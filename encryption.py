from Crypto.Cipher import AES
import base64

key = b'1234567890123456'  # 16-byte key

def encrypt(message):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())

    encrypted = cipher.nonce + tag + ciphertext
    return base64.b64encode(encrypted).decode()

def decrypt(encrypted_message):
    data = base64.b64decode(encrypted_message)

    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()