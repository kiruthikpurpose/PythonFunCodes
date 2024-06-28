import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()

# Set up the x-axis
x = np.linspace(0, 2 * np.pi, 200)

# Initialize an empty line object (to be updated)
line, = ax.plot([], [])

# Set axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

# Update function for animation
def update(frame):
    # Clear previous plot
    ax.clear()
    
    # Set axis limits
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.5, 1.5)
    
    # Plot the sine wave
    y = np.sin(x + frame / 10)
    ax.plot(x, y, color='blue')
    
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=range(200), interval=50)

# Show the plot
plt.show()
