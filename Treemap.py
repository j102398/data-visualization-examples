import matplotlib.pyplot as plt
import squarify  # Library for treemaps

# Sample data: Hierarchical structure of product categories and their sales proportions
categories = {
    'Electronics': {
        'Phones': 350,
        'Laptops': 500,
        'Accessories': 200
    },
    'Clothing': {
        'Men': 300,
        'Women': 400,
        'Kids': 150
    },
    'Home': {
        'Furniture': 450,
        'Decor': 150
    }
}

# Flatten the hierarchical data into a single list for treemap plotting
sizes = [size for category in categories.values() for size in category.values()]
labels = [f"{top_category}\n{sub_category}" for top_category, subcategories in categories.items() for sub_category in subcategories]

plt.figure(figsize=(8, 6))  # Create a figure with specified size

# Plotting the treemap using squarify
squarify.plot(
    sizes=sizes,  # Sizes of the rectangles
    label=labels,  # Labels for each rectangle
    alpha=0.8,  # Transparency of rectangles
    color=plt.cm.Accent.colors  # Using a color palette for the rectangles
)

# Formatting
plt.axis('off')  # Remove axis labels and ticks
plt.title('Sales Distribution by Product Categories (Treemap)')  # Title of the plot
plt.show()  # Display the treemap
