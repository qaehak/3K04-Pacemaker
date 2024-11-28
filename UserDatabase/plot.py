import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import random
import time

def show_dynamic_graph():
    # Create a new window for the graph
    graph_window = tk.Toplevel()
    graph_window.title("Dynamic Real-Time Graph")
    graph_window.geometry("800x600")

    # Initialize data storage
    x_data = []
    y_data = []

    # Create a figure for embedding in Tkinter
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Configure the plot
    line, = ax.plot([], [], lw=2, label="Real-Time Data")
    ax.set_title("Real-Time Data Visualization")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Value")
    ax.legend()

    # Set initial axis limits
    ax.set_xlim(0, 100)
    ax.set_ylim(-10, 10)

    # Track start time
    start_time = time.time()

    # Update function for animation
    def update(frame):
        nonlocal x_data, y_data

        # Generate fake data
        current_time = time.time() - start_time
        y_value = random.uniform(-5, 5)

        # Append data to the lists
        x_data.append(current_time)
        y_data.append(y_value)

        # Keep only the last 100 points
        if len(x_data) > 100:
            x_data.pop(0)
            y_data.pop(0)

        # Update line data
        line.set_data(x_data, y_data)

        # Dynamically adjust axis limits
        ax.set_xlim(max(0, current_time - 10), current_time + 2)
        ax.set_ylim(min(y_data) - 2, max(y_data) + 2)

        return line,

    # Initialize animation
    ani = FuncAnimation(fig, update, interval=100)

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.draw()

    # Add a close button
    close_button = tk.Button(graph_window, text="Close", command=graph_window.destroy)
    close_button.pack(side=tk.BOTTOM, pady=10)

    graph_window.mainloop()
