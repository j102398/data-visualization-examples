import matplotlib.pyplot as plt

# Sample data for smartphone brands
brands = ['Apple', 'Samsung', 'Google', 'Huawei', 'OnePlus']
market_share = [40, 30, 10, 15, 5]  # Market share in percentage
customer_ratings = [4.7, 4.5, 4.3, 4.0, 4.6]  # Average customer ratings out of 5
units_sold = [800, 600, 200, 300, 100]  # Number of units sold (in millions)

plt.figure(figsize=(8, 6))  # Create a figure with specified size

# Create a bubble chart
plt.scatter(
    market_share,  # X-axis: Market Share
    customer_ratings,  # Y-axis: Customer Ratings
    s=units_sold,  # Bubble size: Units Sold
    alpha=0.5,  # Transparency of bubbles
    c='blue',  # Bubble color
    edgecolors='black',  # Edge color for bubbles
)

# Labeling
plt.xlabel('Market Share (%)')  # X-axis label
plt.ylabel('Customer Ratings (out of 5)')  # Y-axis label
plt.title('Smartphone Brands Performance')  # Title of the plot
plt.grid(True)  # Display gridlines

# Annotate bubbles with brand names
for i, brand in enumerate(brands):
    plt.text(market_share[i], customer_ratings[i], brand, ha='center', va='center')

plt.show()  # Show the plot
