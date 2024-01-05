import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Create a line graph
plt.figure(figsize=(8, 5))  # Adjust the figure size if needed
plt.plot(x_values, y_values, marker='x', linestyle='-', color='b', label='Example Line')


#The linestyle determines type of line. Currentlly set to - for solid line.
#The marker determines the shape of the line. Currently set to x for a cross.
#The color determines the color of the line. Currently set to b for blue.
#The label determines the name of the line. Currently set to Example Line.


# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Example Line Graph')

# Add gridlines
plt.grid(True)

# Add legend
plt.legend()

# Show plot
plt.show()
