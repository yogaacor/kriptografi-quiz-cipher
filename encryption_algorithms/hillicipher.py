# hillicipher.py
import numpy as np

def hill_encrypt(plaintext, key):
    key_matrix = np.array(key).reshape(2, 2)
    plaintext = plaintext.upper().replace(' ', '')

    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        vector = np.array([ord(plaintext[i]) - 65, ord(plaintext[i + 1]) - 65])
        encrypted_vector = np.dot(key_matrix, vector) % 26
        ciphertext += chr(encrypted_vector[0] + 65) + chr(encrypted_vector[1] + 65)

    return ciphertext

def hill_decrypt(ciphertext, key):
    key_matrix = np.array(key).reshape(2, 2)
    determinant = int(np.round(np.linalg.det(key_matrix))) % 26

    inv_determinant = pow(determinant, -1, 26)
    adjugate_matrix = np.round(determinant * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_key_matrix = (inv_determinant * adjugate_matrix) % 26

    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        vector = np.array([ord(ciphertext[i]) - 65, ord(ciphertext[i + 1]) - 65])
        decrypted_vector = np.dot(inv_key_matrix, vector) % 26
        plaintext += chr(int(decrypted_vector[0]) + 65) + chr(int(decrypted_vector[1]) + 65)

    return plaintext.replace('X', '')
