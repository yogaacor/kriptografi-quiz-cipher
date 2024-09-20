import tkinter as tk
from tkinter import filedialog
from encryption_algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from encryption_algorithms.playfair import playfair_encrypt, playfair_decrypt
from encryption_algorithms.hillicipher import hill_encrypt, hill_decrypt

# Fungsi File
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            plaintext_box.delete("1.0", tk.END)
            plaintext_box.insert(tk.END, file.read())

# Fungsi Encrypt Text
def encrypt_text():
    plaintext = plaintext_box.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    selected_ciphers = [cipher for cipher, var in cipher_vars.items() if var.get()]

    if len(key) < 12:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Minimal 12 karakter!")
        return

    ciphertext = ""
    for cipher in selected_ciphers:
        if cipher == "Vigenere":
            ciphertext += vigenere_encrypt(plaintext, key) + "\n"
        elif cipher == "Playfair":
            ciphertext += playfair_encrypt(plaintext, key) + "\n"
        elif cipher == "Hill":
            ciphertext += hill_encrypt(plaintext, key) + "\n"

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, ciphertext)

# Fungsi Decrypt Text
def decrypt_text():
    ciphertext = plaintext_box.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    selected_ciphers = [cipher for cipher, var in cipher_vars.items() if var.get()]

    if len(key) < 12:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Minimal 12 karakter!")
        return

    plaintext = ""
    for cipher in selected_ciphers:
        if cipher == "Vigenere":
            plaintext += vigenere_decrypt(ciphertext, key) + "\n"
        elif cipher == "Playfair":
            plaintext += playfair_decrypt(ciphertext, key) + "\n"
        elif cipher == "Hill":
            plaintext += hill_decrypt(ciphertext, key) + "\n"

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, plaintext)

# Setup GUI
window = tk.Tk()
window.title("Cipher Kriptografi")
window.configure(bg="#f0f4f7")

label_fg_color = "#34495e"
button_bg_color = "#3498db"
button_fg_color = "#ffffff"

plaintext_label = tk.Label(window, text="Text Input", fg=label_fg_color, bg="#f0f4f7", font=("Arial", 12, "bold"))
plaintext_label.pack()

name_label = tk.Label(window, text="by Yoga Yudha Tama", fg=label_fg_color, bg="#f0f4f7")
name_label.pack(pady=5)

plaintext_box = tk.Text(window, height=5, width=50, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 10), highlightthickness=1, highlightcolor="#3498db", highlightbackground="#34495e")
plaintext_box.pack()

open_button = tk.Button(window, text="Open File", command=open_file, bg=button_bg_color, fg=button_fg_color)
open_button.pack(pady=5)

key_label = tk.Label(window, text="Key (min 12 characters)", fg=label_fg_color, bg="#f0f4f7")
key_label.pack()

key_entry = tk.Entry(window, width=52, bg="#ecf0f1", fg="#2c3e50")
key_entry.pack(pady=5)

cipher_vars = {
    "Vigenere": tk.BooleanVar(),
    "Playfair": tk.BooleanVar(),
    "Hill": tk.BooleanVar()
}

for cipher in cipher_vars:
    checkbox = tk.Checkbutton(window, text=cipher, variable=cipher_vars[cipher], bg="#f0f4f7", fg=label_fg_color)
    checkbox.pack(anchor=tk.W)

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text, bg=button_bg_color, fg=button_fg_color)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text, bg=button_bg_color, fg=button_fg_color)
decrypt_button.pack(pady=5)

result_label = tk.Label(window, text="Result", fg=label_fg_color, bg="#f0f4f7", font=("Arial", 12, "bold"))
result_label.pack()

result_box = tk.Text(window, height=10, width=50, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 10), highlightthickness=1, highlightcolor="#3498db", highlightbackground="#34495e")
result_box.pack()

window.mainloop()

