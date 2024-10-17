import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.animation as animation

# Generate dummy data representing 52 weeks and 7 days (1 year of contributions)
data = np.random.randint(0, 5, size=(52, 7))

# Create a figure for the heatmap
fig, ax = plt.subplots(figsize=(10, 4))

# Function to update the heatmap for each frame
def update(frame):
    ax.clear()
    ax.set_title(f"GitHub Contributions Animation - Week {frame + 1}")
    
    # Update the heatmap with frame-specific data
    heatmap_data = np.random.randint(0, 5, size=(52, 7))  # Simulating new data
    cax = ax.imshow(heatmap_data, cmap='Greens', aspect='auto')

    # Add color bar
    plt.colorbar(cax, ax=ax)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=52, interval=500)

# Save the animation as a GIF
ani.save('contribution_heatmap.gif', writer='imagemagick', fps=1)

# Optionally, save a static version as well
plt.savefig('contribution_heatmap.png')
