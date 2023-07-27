import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def generate_password(length):
    # Define characters for password generation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choices
    password = ''.join(random.choices(characters, k=length))
    
    return password

def generate_and_display_password():
    try:
        # Get the desired length of the password from the entry field
        length = int(length_entry.get())
        
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer.")
        else:
            # Limit the password length to 50 characters
            length = min(length, 50)
            
            # Generate the password
            password = generate_password(length)
            
            # Clear the text widget and display the generated password
            generated_password_text.delete(1.0, tk.END)
            generated_password_text.insert(tk.END, password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid positive integer for password length.")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_text.delete(1.0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Set the background color to #8EE5EE
app.configure(background="#8EE5EE")

# Heading
heading_label = tk.Label(app, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#8EE5EE")
heading_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

# User name input
username_label = tk.Label(app, text="Enter user name:", bg="#8EE5EE")
username_label.grid(row=1, column=0, padx=5, pady=2, sticky="w")
username_entry = tk.Entry(app, width=30, bg="white", bd=2, relief="groove")
username_entry.grid(row=1, column=1, pady=2, padx=5, sticky="ew")

# Password length input
length_label = tk.Label(app, text="Enter Password Length:", bg="#8EE5EE")
length_label.grid(row=2, column=0, padx=5, pady=2, sticky="w")
length_entry = tk.Entry(app, width=30, bg="white", bd=2, relief="groove")
length_entry.grid(row=2, column=1, pady=2, padx=5, sticky="ew")

# Generated password display
generated_password_label = tk.Label(app, text="Generated Password:", bg="#8EE5EE")
generated_password_label.grid(row=3, column=0, padx=5, pady=2, sticky="w")
generated_password_text = ScrolledText(app, width=30, height=3, bg="white", bd=2, relief="groove")
generated_password_text.grid(row=3, column=1, pady=2, padx=5, sticky="ew")

# Buttons with color #FF9912
button_style = {"bg": "#FF9912", "bd": 2, "relief": "groove"}
generate_button = tk.Button(app, text="Generate Password", command=generate_and_display_password, **button_style)
generate_button.grid(row=4, column=0, columnspan=2, pady=5, sticky="n")

accept_button = tk.Button(app, text="Accept", command=reset_fields, **button_style)
accept_button.grid(row=5, column=0, pady=5)

reset_button = tk.Button(app, text="Reset", command=reset_fields, **button_style)
reset_button.grid(row=5, column=1, pady=5)

# Center the window on the screen
app.update_idletasks()
width = app.winfo_width()
height = app.winfo_height()
x_offset = (app.winfo_screenwidth() - width) // 2
y_offset = (app.winfo_screenheight() - height) // 2
app.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

# Start the main event loop
app.mainloop()
