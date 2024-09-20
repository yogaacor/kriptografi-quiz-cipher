import tkinter as tk
from tkinter import filedialog
from encryption_algorithms.vigenere import encrypt_vigenere, decrypt_vigenere
from encryption_algorithms.playfair import encrypt_playfair, decrypt_playfair
from encryption_algorithms.hillicipher import encrypt_hill, decrypt_hill

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            plaintext_box.delete("1.0", tk.END)
            plaintext_box.insert(tk.END, file.read())

def encrypt_text():
    plaintext = plaintext_box.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    selected_ciphers = [cipher for cipher, var in cipher_vars.items() if var.get()]

    if len(key) < 12:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "minimal 12 karakter!")
        return

    ciphertext = ""
    for cipher in selected_ciphers:
        if cipher == "Vigenere":
            ciphertext += encrypt_vigenere(plaintext, key) + "\n"
        elif cipher == "Playfair":
            ciphertext += encrypt_playfair(plaintext, key) + "\n"
        elif cipher == "Hill":
            ciphertext += encrypt_hill(plaintext, key) + "\n"

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, ciphertext)

def decrypt_text():
    ciphertext = plaintext_box.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    selected_ciphers = [cipher for cipher, var in cipher_vars.items() if var.get()]

    if len(key) < 12:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "minimal 12 karakter!")
        return

    plaintext = ""
    for cipher in selected_ciphers:
        if cipher == "Vigenere":
            plaintext += decrypt_vigenere(ciphertext, key) + "\n"
        elif cipher == "Playfair":
            plaintext += decrypt_playfair(ciphertext, key) + "\n"
        elif cipher == "Hill":
            plaintext += decrypt_hill(ciphertext, key) + "\n"

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, plaintext)

# Setup GUI
window = tk.Tk()
window.title("Cipher Kriptografi")

plaintext_label = tk.Label(window, text="Plaintext")
plaintext_label.pack()

name_label = tk.Label(window, text="by Yoga Yudha Tama")  
name_label.pack(pady=5)

plaintext_box = tk.Text(window, height=5, width=50)
plaintext_box.pack()

open_button = tk.Button(window, text="Open File", command=open_file)
open_button.pack()

cipher_label = tk.Label(window, text="Choose Ciphers")
cipher_label.pack()

# Create a frame for checkbuttons
cipher_frame = tk.Frame(window)
cipher_frame.pack(pady=10)

# Cipher options with checkboxes
cipher_vars = {
    "Vigenere": tk.IntVar(),
    "Playfair": tk.IntVar(),
    "Hill": tk.IntVar()
}

for cipher, var in cipher_vars.items():
    cb = tk.Checkbutton(cipher_frame, text=cipher, variable=var)
    cb.pack(anchor=tk.CENTER)

key_label = tk.Label(window, text="Key at least 12 characters")
key_label.pack()

key_entry = tk.Entry(window)
key_entry.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text, width=10)
encrypt_button.pack(side=tk.LEFT, padx=10)

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text, width=10)
decrypt_button.pack(side=tk.LEFT)

result_label = tk.Label(window, text="Ciphertext")
result_label.pack()

result_box = tk.Text(window, height=5, width=50)
result_box.pack()

# Start GUI loop
window.mainloop()
