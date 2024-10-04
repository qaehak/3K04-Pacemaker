import tkinter as tk
from tkinter import messagebox
import database  # Import the database module

# Function to validate the login or add to the database
# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if database.login(username, password):
        messagebox.showinfo("Login Success", f"Welcome back, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function for sign-up
def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    
    add_result = database.signup(username, password)
    
    if add_result is True:
        messagebox.showinfo("Sign Up Success", f"User '{username}' added to the database.")
    elif add_result is False:
        messagebox.showerror("Error", f"Username '{username}' already exists. Try logging in.")
    elif add_result is None:
        messagebox.showerror("Error", "Database is full. Cannot add more users.")


# Create the main window
root = tk.Tk()
root.title("Login/Sign Up Screen")
root.geometry("400x300")

# Create a label for the welcome message
welcome_label = tk.Label(root, text="Welcome! Please login or sign up", font=("Arial", 16))
welcome_label.pack(pady=20)

# Create labels and entry widgets for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")  # Hide password input
password_entry.pack(pady=5)

# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Create a sign-up button
signup_button = tk.Button(root, text="Sign Up", command=sign_up)
signup_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()