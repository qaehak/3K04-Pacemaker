import tkinter as tk
from tkinter import messagebox
import database  # Import the database module

db = database.database()
db.startup()

# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if db.login(username, password):
        messagebox.showinfo("Login Success", f"Welcome back, {username}!")
        open_home_page()  # Navigate to the home page after successful login
        db.shutdown()  # Close the database connection
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function for sign-up
def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    
    add_result = db.signup(username, password)
    
    if add_result is True:
        messagebox.showinfo("Sign Up Success", f"User '{username}' added to the database.")
    elif add_result is False:
        messagebox.showerror("Error", f"Username '{username}' already exists. Try logging in.")
    elif add_result is None:
        messagebox.showerror("Error", "Database is full. Cannot add more users.")

# Function to open the home page
def open_home_page():
    # Destroy the login window
    root.destroy()

    # Create a new window for the home page
    home_window = tk.Tk()
    home_window.title("Home Page")
    home_window.geometry("400x300")

    # Create a label for the home page
    home_label = tk.Label(home_window, text="Welcome to the Home Page!", font=("Arial", 16))
    home_label.pack(pady=50)

    # You can add more widgets here for folders, parameters, etc.
    parameters_label = tk.Label(home_window, text="This is where your parameters/folders will go.", font=("Arial", 12))
    parameters_label.pack(pady=20)

    # Start the main loop for the home page
    home_window.mainloop()

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
