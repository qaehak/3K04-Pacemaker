import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
import time
import database
from modes import Modes
from param import param
import os


db = database.database()
db.startup()


# Initialize data storage for the graph
x_data = []
y_data = []
start_time = time.time()

# Initialize data storage for both graphs
x_data_1, y_data_1 = [], []
x_data_2, y_data_2 = [], []
start_time = time.time()

# Function to update the first graph
def update_graph_1():
    global x_data_1, y_data_1

    # Generate fake data
    current_time = time.time() - start_time
    y_value = random.uniform(-5, 5)

    # Append data to the lists
    x_data_1.append(current_time)
    y_data_1.append(y_value)

    # Keep only the last 100 points
    if len(x_data_1) > 100:
        x_data_1.pop(0)
        y_data_1.pop(0)

    # Update the plot data
    line_1.set_data(x_data_1, y_data_1)

    # Adjust axis limits dynamically
    ax_1.set_xlim(max(0, current_time - 10), current_time + 2)
    ax_1.set_ylim(min(y_data_1) - 2, max(y_data_1) + 2)

    # Redraw the canvas
    canvas_1.draw()

    # Schedule the next update
    graph_frame_1.after(100, update_graph_1)

# Function to update the second graph
def update_graph_2():
    global x_data_2, y_data_2

    # Generate fake data
    current_time = time.time() - start_time
    y_value = random.uniform(-5, 5)

    # Append data to the lists
    x_data_2.append(current_time)
    y_data_2.append(y_value)

    # Keep only the last 100 points
    if len(x_data_2) > 100:
        x_data_2.pop(0)
        y_data_2.pop(0)

    # Update the plot data
    line_2.set_data(x_data_2, y_data_2)

    # Adjust axis limits dynamically
    ax_2.set_xlim(max(0, current_time - 10), current_time + 2)
    ax_2.set_ylim(min(y_data_2) - 2, max(y_data_2) + 2)

    # Redraw the canvas
    canvas_2.draw()

    # Schedule the next update
    graph_frame_2.after(100, update_graph_2)


# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if db.login(username, password):
        # Show a message box and open the Modes home page after it's closed
        messagebox.showinfo("Login Success", f"Welcome back, {username}!")
        root.after(0, open_home_page)  # Use after() to delay opening home page until message box is closed
        # Don't close database here because if you try to relogin (after logging out) it won't let you since you shut db the first time
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def logout(home_window):
    home_window.destroy()
    login_signup_screen()



# Function for sign-up
def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    
    add_result = db.signup(username, password)
    
    if add_result == 1:
        messagebox.showinfo("Sign Up Success", f"User '{username}' added to the database.")
    elif add_result == 2:
        messagebox.showerror("Error", f"Username '{username}' already exists. Try logging in.")
    elif add_result == 0:
        messagebox.showerror("Error", "Database is full. Cannot add more users.")

# Function to open the home page (from modes.py)
def open_home_page():
    # Destroy the login window
    #clear_window(root)
    
    # serena 1234 login to test
    # Create a new window for the home page (from modes.py)
    home_window = tk.Toplevel(root)
    home_window.title("Pacemaker Modes Home Page")
    home_window.minsize(1500,1000)
    home_window['bg'] = "#E0DCFB"
    
    # Create an instance of the param class and pass it to Modes
    pacemaker_params = param()  # Assuming the param class handles pacemaker parameters
   
    # Pass the new window and pacemaker parameters to the Modes class
    app = Modes(home_window, pacemaker_params)
    
    # Configure grid columns to push images to the far right
    for i in range(20):  # Arbitrary high range for flexibility
        home_window.columnconfigure(i, weight=1)
    home_window.columnconfigure(19, weight=10)  # Heavier weight to the last column to fill empty space

    #create logout button
    logout_button  = tk.Button(home_window, text="Logout", command=lambda: logout(home_window))
    logout_button.grid(row=0, column=20, padx=10, pady=10, sticky="nw")
    logout_button['bg'] = "white"

# Place the heart image as a button
    connection_image = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "heart.png"))
    connection_button = tk.Label(home_window, image=connection_image, bg="#E0DCFB")
    connection_button.grid(row=1, column=19, sticky="e")
    connection_button.image = connection_image

    # Embed first real-time graph
    global graph_frame_1, canvas_1, line_1, ax_1
    graph_frame_1 = tk.Frame(home_window, bg="white")
    graph_frame_1.grid(row=8, column=15, sticky="e", padx=20, pady=20)

    fig_1 = Figure(figsize=(5, 4), dpi=100)
    ax_1 = fig_1.add_subplot(111)
    ax_1.set_title("Real-Time Graph 1")
    ax_1.set_xlabel("Time (s)")
    ax_1.set_ylabel("Value")
    ax_1.set_xlim(0, 10)
    ax_1.set_ylim(-10, 10)
    line_1, = ax_1.plot([], [], lw=2, label="Graph 1 Data")
    ax_1.legend()

    canvas_1 = FigureCanvasTkAgg(fig_1, master=graph_frame_1)
    canvas_1.get_tk_widget().pack()

    update_graph_1()

    # Embed second real-time graph
    global graph_frame_2, canvas_2, line_2, ax_2
    graph_frame_2 = tk.Frame(home_window, bg="white")
    graph_frame_2.grid(row=8, column=19, sticky="e", padx=20, pady=20)

    fig_2 = Figure(figsize=(5, 4), dpi=100)
    ax_2 = fig_2.add_subplot(111)
    ax_2.set_title("Real-Time Graph 2")
    ax_2.set_xlabel("Time (s)")
    ax_2.set_ylabel("Value")
    ax_2.set_xlim(0, 10)
    ax_2.set_ylim(-10, 10)
    line_2, = ax_2.plot([], [], lw=2, label="Graph 2 Data")
    ax_2.legend()

    canvas_2 = FigureCanvasTkAgg(fig_2, master=graph_frame_2)
    canvas_2.get_tk_widget().pack()

    update_graph_2()

    home_window.mainloop()



def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def login_signup_screen():   
    clear_window(root)

    # Create the main window for login
    root.title("Login/Sign Up Screen")
    root.geometry("800x600")
    root['bg'] = "#E0DCFB"

    # Create a label for the welcome message
    welcome_label = tk.Label(root, text="Welcome! Please login or sign up", font=("Arial", 16))
    welcome_label.pack(pady=20)
    welcome_label['bg'] = "#E0DCFB"

    global username_entry, password_entry
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


root = tk.Tk()

login_signup_screen()

# Start the GUI main loop
root.mainloop()

db.shutdown() # Close the database connection only when entire program shuts down

