# playfair.py
def create_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used_chars = set()

    for char in key:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)

    for i in range(65, 91):
        if chr(i) not in used_chars and chr(i) != 'J':
            matrix.append(chr(i))

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def prepare_text_playfair(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    prepared = ""
    i = 0
    while i < len(text):
        prepared += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared += 'X'
        else:
            if i + 1 < len(text):
                prepared += text[i + 1]
        i += 2
    return prepared

def find_index_playfair(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i * 5 + row.index(char)
    return -1

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = prepare_text_playfair(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row_a, col_a = divmod(find_index_playfair(matrix, a), 5)
        row_b, col_b = divmod(find_index_playfair(matrix, b), 5)

        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = divmod(find_index_playfair(matrix, a), 5)
        row_b, col_b = divmod(find_index_playfair(matrix, b), 5)

        if row_a == row_b:
            plaintext += matrix[row_a][(col_a - 1) % 5]
            plaintext += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += matrix[(row_a - 1) % 5][col_a]
            plaintext += matrix[(row_b - 1) % 5][col_b]
        else:
            plaintext += matrix[row_a][col_b]
            plaintext += matrix[row_b][col_a]

    return plaintext.replace('X', '')
