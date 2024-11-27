import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time

# Initialize data storage
x_data = []
y_data = []

# Initialize the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, label="Real-Time Data")

# Set axis labels and title
ax.set_title("Real-Time Data Visualization (Fake Data)")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Value")
ax.legend()

# Set initial axis limits
ax.set_xlim(0, 100)
ax.set_ylim(-10, 10)

# Update function for the animation
start_time = time.time()

def update(frame):
    global x_data, y_data

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

# Display plot
plt.show()
