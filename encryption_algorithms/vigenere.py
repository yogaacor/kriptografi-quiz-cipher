# Fungsi Vigenere
def encrypt_vigenere(plaintext, key):
    key = key.upper()
    result = ""
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            shift = (ord(char) - offset + ord(key[key_index]) - ord('A')) % 26
            result += chr(shift + offset)
            key_index = (key_index + 1) % key_length
        else:
            result += char

    return result

def decrypt_vigenere(ciphertext, key):
    key = key.upper()
    result = ""
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            shift = (ord(char) - offset - (ord(key[key_index]) - ord('A'))) % 26
            result += chr(shift + offset)
            key_index = (key_index + 1) % key_length
        else:
            result += char

    return result

