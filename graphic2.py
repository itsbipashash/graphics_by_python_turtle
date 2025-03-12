import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)

# Define initial values
x, y = 0, 0
angle = 0
lines = []  # Store line segments
num_frames = 100  # Number of animation frames

# Get a smooth color gradient
cmap = plt.get_cmap("hsv")
colors = [cmap(i / num_frames) for i in range(num_frames)]


# Function to update animation frame
def update(frame):
    global x, y, angle

    # Compute next point
    x_new = x + (frame * 3) * np.cos(np.radians(angle))
    y_new = y + (frame * 3) * np.sin(np.radians(angle))

    # Draw line segment
    line, = ax.plot([x, x_new], [y, y_new], color=colors[frame], linewidth=frame / 30 + 0.5)
    lines.append(line)

    # Update current position
    x, y = x_new, y_new
    angle += 137.5  # Golden angle

    return line,


# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.show()
