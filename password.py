import os
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join([characters[byte % len(characters)] for byte in os.urandom(length)])

    return password


length = int(input("Enter the length of the password: "))
password = generate_password(length)
print("Generated Password:", password)
