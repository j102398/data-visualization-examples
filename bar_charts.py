import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 35, 30, 25]  # Example values for each category

# Create a bar chart
plt.figure(figsize=(8, 6))  # Adjust the figure size if needed
plt.bar(categories, values, color='skyblue',width=0.1)

#Width adjuts width of bar

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Example Bar Chart')

# Show the bar chart
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout for better appearance
plt.show()
