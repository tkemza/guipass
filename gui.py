import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    lower = "abcdefghijklmnoprstuvwxyz" # All lower letters
    upper = "ABCDEFGHIJKLMNOPRSTUVWXYZ" # All upper letters
    numbers = "0123456789" # All numbers
    symbols = "!@#$%^&*_=?" # Symbols

    all_chars = lower + upper + numbers + symbols
    password = ''.join(random.sample(all_chars, length))
    return password

def on_generate(event=None):
    user_input = entry.get().strip()
    if not user_input.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    length = int(user_input)
    password = generate_password(length)
    result_label.config(text=f"Generated password: {password}")
    # Enable copying to clipboard
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()  # Ensure clipboard content is updated

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("800x600")
root.configure(bg="black")

# Function to handle Enter key press event in entry field
def handle_enter(event):
    on_generate()

# Add a Text widget for the ASCII art logo
text_widget = tk.Text(root, height=10, bg="black", fg="light blue", borderwidth=0, highlightthickness=0, font=("Courier", 12))
text_widget.pack(pady=10)

ascii_art = """
       ___                 ___                          _             
      / _ \\__ _ ___ ___   / _ \\___ _ __   ___ _ __ __ _| |_ ___  _ __ 
     / /_)/ _` / __/ __| / /_\\/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|
    / ___/ (_| \\__ \\__ \\/ /_\\\\  __/ | | |  __/ | | (_| | || (_) | |   
    \\/    \\__,_|___/___/\\____/\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   
"""

# Insert the ASCII art into the Text widget and set its color
text_widget.insert(tk.END, ascii_art)
text_widget.tag_configure("light_blue", foreground="light blue")
text_widget.tag_add("light_blue", "1.0", tk.END)
text_widget.configure(state="disabled")  # Make the Text widget read-only

# Add input label and entry
input_label = tk.Label(root, text="Enter password length:", fg="light blue", bg="black")
input_label.pack(pady=5)
entry = tk.Entry(root, width=20, bg="black", fg="light blue")
entry.pack(pady=5)
entry.bind("<Return>", handle_enter)  # Bind Enter key to handle_enter function

# Add generate button
generate_button = tk.Button(root, text="Generate or click Enter", command=on_generate, bg="black", fg="light blue")
generate_button.pack(pady=22)

# Add result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="light blue", bg="black")
result_label.pack(pady=20)

# Run the application
root.mainloop()
