# PRODIGY_CS_01
This project is a simple yet functional Caesar Cipher Encryption and Decryption Tool built using Python and Tkinter.
Users can input any message along with a shift value to encrypt or decrypt text using the classical Caesar Shift Cipher algorithm.

The GUI is styled with a dark blue interface, while input fields remain clean and white for better readability.

🚀 Features

Encrypt text using the Caesar Shift Cipher

Decrypt text back to original form

User-friendly Tkinter GUI

Dark blue themed interface

Real-time result display

Handles:

Uppercase letters

Lowercase letters

Non-alphabetic characters (left unchanged)

🖼️ Preview of Functionality

Enter your text

Provide a shift value (e.g., 3)

Click Encrypt or Decrypt

The output appears instantly in the results box

🛠️ Requirements

This project works on:

Python 3.x

Standard library only (no external dependencies)

Tkinter comes pre-installed with Python on Windows, Linux, and Mac.

📌 How the Caesar Cipher Works

The Caesar Cipher shifts each letter in a message by a fixed number (the shift value).
Example with shift = 3:

A → D

B → E

X → A

Y → B

Decryption reverses the shift.

▶️ How to Run the Program

Install Python 3 if not installed

Save the script as: caesar_cipher_gui.py
Run it using:python3 caesar_cipher_gui.py
The GUI window will open.

Project Structure
📁 CaesarCipherTool
│── caesar_cipher_gui.py     # Main program with Tkinter GUI
│── README.md                 # Documentation file

🧩 Core Functions Explained
Function	Purpose
encrypt(text, shift)	Applies Caesar Cipher to encrypt text
decrypt(text, shift)	Reverses encryption using the same shift
Tkinter GUI	Takes input, displays output, handles user interaction

