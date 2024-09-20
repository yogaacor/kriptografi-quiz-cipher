# Fungsi Hill
import numpy as np

def mod_inv(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)
    matrix_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod) % mod
    return matrix_inv

def create_key_matrix(key_string):
    key_string = ''.join(filter(str.isalpha, key_string)).upper()
    key_numbers = [ord(char) - 65 for char in key_string]
    
    if len(key_numbers) < 9:
        raise ValueError("Kunci harus berupa 9 angka")
    
    key_matrix = np.array(key_numbers[:9]).reshape(3, 3)
    return key_matrix

def encrypt_hill(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    while len(plaintext) % 3 != 0:
        plaintext += "X"

    plaintext_vector = [ord(char) - 65 for char in plaintext]
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, 3)
    key_matrix = np.array(key_matrix).astype(int)
    
    encrypted_matrix = (np.dot(plaintext_matrix, key_matrix) % 26)
    encrypted_text = ''.join([chr(num + 65) for row in encrypted_matrix for num in row])
    return encrypted_text

def decrypt_hill(ciphertext, key_matrix):
    ciphertext_vector = [ord(char) - 65 for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, 3)
    key_matrix = np.array(key_matrix).astype(int)
    
    inverse_key_matrix = mod_inv(key_matrix, 26)
    decrypted_matrix = (np.dot(ciphertext_matrix, inverse_key_matrix) % 26)
    decrypted_text = ''.join([chr(num + 65) for row in decrypted_matrix for num in row])
    return decrypted_text
