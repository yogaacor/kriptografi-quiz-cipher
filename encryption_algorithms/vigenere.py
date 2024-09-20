# vigenere.py
def vigenere_encrypt(plaintext, key):
    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            ciphertext += chr(((ord(plaintext[i]) - 65) + (ord(key[i % len(key)]) - 65)) % 26 + 65)
        else:
            ciphertext += plaintext[i]
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    ciphertext = ciphertext.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            plaintext += chr(((ord(ciphertext[i]) - 65) - (ord(key[i % len(key)]) - 65)) % 26 + 65)
        else:
            plaintext += ciphertext[i]
    return plaintext
