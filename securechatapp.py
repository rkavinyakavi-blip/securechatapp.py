import socket
from encryption import encrypt

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

while True:
    message = input("You: ")

    encrypted_message = encrypt(message)

    print("Encrypted:", encrypted_message)

    client.send(encrypted_message)