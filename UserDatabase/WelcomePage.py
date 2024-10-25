import tkinter as tk
from tkinter import messagebox
import database  # Import the database module
from modes import Modes  # Import the Modes class from modes.py
from param import param  # Import the param class from param.py


db = database.database()
db.startup()


# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if db.login(username, password):
        # Show a message box and open the Modes home page after it's closed
        messagebox.showinfo("Login Success", f"Welcome back, {username}!")
        root.after(0, open_home_page)  # Use after() to delay opening home page until message box is closed
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

# Function to open the home page (from modes.py)
def open_home_page():
    # Destroy the login window
    root.destroy()
    
    # serena 1234 login to test
    # Create a new window for the home page (from modes.py)
    home_window = tk.Tk()
    home_window.title("Pacemaker Modes Home Page")
    home_window.minsize(1500,1000)
    home_window['bg'] = "#E0DCFB"
    
    # Create an instance of the param class and pass it to Modes
    pacemaker_params = param()  # Assuming the param class handles pacemaker parameters
   
    # Pass the new window and pacemaker parameters to the Modes class
    app = Modes(home_window, pacemaker_params)
    
    #place graph
    egram = tk.PhotoImage(file="heart.png")
    egram_label = tk.Label(home_window, image=egram)
    egram_label.grid(row=1,column = 10)
    egram_label['bg'] = "#E0DCFB"
    

    home_window.mainloop()

# Create the main window for login
root = tk.Tk()
root.title("Login/Sign Up Screen")
root.geometry("800x600")
root['bg'] = "#E0DCFB"

# Create a label for the welcome message
welcome_label = tk.Label(root, text="Welcome! Please login or sign up", font=("Arial", 16))
welcome_label.pack(pady=20)
welcome_label['bg'] = "#E0DCFB"

# Create labels and entry widgets for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_label['bg'] = "#E0DCFB"
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_label['bg'] = "#E0DCFB"
password_entry = tk.Entry(root, show="*")  # Hide password input
password_entry.pack(pady=5)

# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)
login_button['bg'] = "white"

# Create a sign-up button
signup_button = tk.Button(root, text="Sign Up", command=sign_up)
signup_button.pack(pady=10)
signup_button['bg'] = "white"

# Start the GUI main loop
root.mainloop()
