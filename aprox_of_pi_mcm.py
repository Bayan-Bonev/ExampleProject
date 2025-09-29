import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import time

# --- Set up plot ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Draw the circle
circle = patches.Circle((0.5, 0.5), 0.5, edgecolor='black', facecolor='none')
ax.add_patch(circle)

# Scatter plots (initially empty)
inside_scatter = ax.scatter([], [], c='blue', s=1, label='Inside')
outside_scatter = ax.scatter([], [], c='red', s=1, label='Outside')
ax.legend(loc='upper right')

# Turn on interactive mode
plt.ion()
plt.show()

# --- Data storage ---
inside_x = []
inside_y = []
outside_x = []
outside_y = []

# Simulation variables
inside_count = 0
total_count = 0

try:
    while True:
        x = random.random()
        y = random.random()
        total_count += 1

        # Check if point is inside the circle
        if (x - 0.5)**2 + (y - 0.5)**2 <= 0.25:
            inside_x.append(x)
            inside_y.append(y)
            inside_count += 1
        else:
            outside_x.append(x)
            outside_y.append(y)

        # Update plot every 100 points
        if total_count % 100 == 0:
            inside_scatter.set_offsets(np.column_stack((inside_x, inside_y)))
            outside_scatter.set_offsets(np.column_stack((outside_x, outside_y)))

            pi_est = 4 * inside_count / total_count
            ax.set_title(f"π ≈ {pi_est:.5f} | Total: {total_count}")

            fig.canvas.draw_idle()
            fig.canvas.flush_events()
            time.sleep(0.01)

except KeyboardInterrupt:
    print(f"Final estimate of π: {4 * inside_count / total_count:.5f}")
    plt.ioff()
    plt.show()