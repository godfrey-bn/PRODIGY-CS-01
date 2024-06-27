from tkinter import *
from tkinter import messagebox

def caesar_encrypt(text, shift):
    """Encrypts text using the Caesar Cipher with a given shift."""
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decrypt(text, shift):
    """Decrypts text using the Caesar Cipher with a given shift."""
    return caesar_encrypt(text, -shift)

def encrypt_message():
    message = entry_message.get(1.0, END).strip()
    try:
        shift = int(entry_shift.get(1.0, END).strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer shift value.")
        return
    result = caesar_encrypt(message, shift)
    text_result.config(state=NORMAL)
    text_result.delete(1.0, END)
    text_result.insert(END, f"Encrypted message: {result}")
    text_result.config(state=DISABLED)

def decrypt_message():
    message = entry_message.get(1.0, END).strip()
    try:
        shift = int(entry_shift.get(1.0, END).strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer shift value.")
        return
    result = caesar_decrypt(message, shift)
    text_result.config(state=NORMAL)
    text_result.delete(1.0, END)
    text_result.insert(END, f"Decrypted message: {result}")
    text_result.config(state=DISABLED)

# GUI Setup
root = Tk()
root.geometry("400x300")
root.title("Caesar Cipher Tool")
root.config(background ='brown')

Label(root, text="Enter Message:").place(x=50, y=20)
entry_message = Text(root, height=5, width=40)
entry_message.place(x=50, y=50)

Label(root, text="Enter Shift:").place(x=50, y=140)
entry_shift = Text(root, height=1, width=10)
entry_shift.place(x=150, y=140)

b1 = Button(root, text="Encrypt", command=encrypt_message)
b1.place(x=100, y=180)

b2 = Button(root, text="Decrypt", command=decrypt_message)
b2.place(x=200, y=180)

text_result = Text(root, height=5, width=40, state=DISABLED)
text_result.place(x=50, y=220)

root.mainloop()