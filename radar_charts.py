import numpy as np
import matplotlib.pyplot as plt

# Data for the radar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 2, 5, 4]  # Example values for each category

# Number of variables/categories
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop
values += values[:1]
angles += angles[:1]

# Create the figure and polar plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot data on radar chart
ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)  # Change linewidth for line thickness

# Add labels
ax.set_yticklabels([])  # Hide radial labels (you can show actual values if needed)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Show the radar chart
plt.show()
