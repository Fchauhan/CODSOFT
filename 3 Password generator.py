import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_label.config(text="Invalid length")
        return
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    password_label.config(text="Generated Password: " + password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create labels and entry fields
length_label = tk.Label(root, text="Enter password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position of the messagebox
x = (screen_width - 300) // 2  # Width of the messagebox is 300 pixels
y = (screen_height - 200) // 2 # Height of the messagebox is 200 pixels

# Set the position of the window
root.geometry(f"300x200+{x}+{y}")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
