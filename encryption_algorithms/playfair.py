# Fungsi playfair
def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_unique = ""

    for char in key.upper():
        if char not in key_unique and char in alphabet:
            key_unique += char

    for char in alphabet:
        if char not in key_unique:
            key_unique += char

    matrix = [list(key_unique[i:i + 5]) for i in range(0, 25, 5)]
    return matrix

def encrypt_playfair(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    
    if len(plaintext) % 2 != 0:
        plaintext += "X"

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row_a, col_a = divmod(matrix_index(matrix, a), 5)
        row_b, col_b = divmod(matrix_index(matrix, b), 5)

        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b] + matrix[row_b][col_a]

    return ciphertext

def matrix_index(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r * 5 + c
    return -1

def decrypt_playfair(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = divmod(matrix_index(matrix, a), 5)
        row_b, col_b = divmod(matrix_index(matrix, b), 5)

        if row_a == row_b:
            # Geser ke kiri pada baris yang sama
            plaintext += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            # Geser ke atas pada kolom yang sama
            plaintext += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
        else:
            # Tukar kolom pada baris yang sama
            plaintext += matrix[row_a][col_b] + matrix[row_b][col_a]

    return plaintext

