import tkinter as tk
from tkinter import messagebox


# --------------------------
# Caesar Cipher Functions
# --------------------------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# --------------------------
# GUI Class
# --------------------------
class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Encryption & Decryption Tool By ATAMA")
        self.root.geometry("600x450")
        self.root.resizable(True, True)

        # Set dark blue background
        self.root.configure(bg="darkblue")

        # Title
        tk.Label(
            root,
            text="Caesar Cipher Encryption & Decryption",
            font=("Arial", 18, "bold"),
            bg="darkblue",
            fg="white"
        ).pack(pady=15)

        # Text input label
        tk.Label(
            root,
            text="Enter Text:",
            font=("Arial", 12, "bold"),
            bg="darkblue",
            fg="white"
        ).pack()

        # White text input
        self.text_input = tk.Text(
            root,
            height=5,
            width=65,
            wrap="word",
            bg="white",
            fg="black"
        )
        self.text_input.pack(pady=8)

        # Shift value label
        tk.Label(
            root,
            text="Shift Value:",
            font=("Arial", 12),
            bg="darkblue",
            fg="white"
        ).pack()

        # White shift input
        self.shift_entry = tk.Entry(
            root,
            width=10,
            font=("Arial", 12),
            bg="white",
            fg="black"
        )
        self.shift_entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Encrypt Text", width=18,
                  command=self.encrypt_text).pack(pady=4)

        tk.Button(root, text="Decrypt Text", width=18,
                  command=self.decrypt_text).pack(pady=4)

        # Output label
        tk.Label(
            root,
            text="Output:",
            font=("Arial", 12, "bold"),
            bg="darkblue",
            fg="white"
        ).pack(pady=10)

        # White output box
        self.output_box = tk.Text(
            root,
            height=7,
            width=65,
            wrap="word",
            state="disabled",
            bg="white",
            fg="black"
        )
        self.output_box.pack(pady=10)

    # --------------------------
    # Validate shift input
    # --------------------------
    def get_shift_value(self):
        try:
            return int(self.shift_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Shift value must be a number!")
            return None

    # --------------------------
    # Encrypt
    # --------------------------
    def encrypt_text(self):
        shift = self.get_shift_value()
        if shift is None:
            return

        text = self.text_input.get("1.0", "end").strip()
        if not text:
            messagebox.showerror("Empty Input", "Please enter text to encrypt.")
            return

        encrypted = caesar_encrypt(text, shift)
        self.display_output(encrypted)

    # --------------------------
    # Decrypt
    # --------------------------
    def decrypt_text(self):
        shift = self.get_shift_value()
        if shift is None:
            return

        text = self.text_input.get("1.0", "end").strip()
        if not text:
            messagebox.showerror("Empty Input", "Please enter text to decrypt.")
            return

        decrypted = caesar_decrypt(text, shift)
        self.display_output(decrypted)

    # --------------------------
    # Display Output
    # --------------------------
    def display_output(self, content):
        self.output_box.config(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("end", content)
        self.output_box.config(state="disabled")


# --------------------------
# Run App
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    CaesarCipherGUI(root)
    root.mainloop()