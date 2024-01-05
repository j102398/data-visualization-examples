import matplotlib.pyplot as plt

# Sample data for teams and their wins and losses
teams = ['Team A', 'Team B', 'Team C']
wins = [20, 18, 15]  # Sample wins data
losses = [5, 7, 9]  # Sample losses data

plt.figure(figsize=(8, 5))  # Create a figure with specified size

# Create a stacked bar chart
plt.bar(
    teams,  # X-axis: Teams
    wins,  # Height of first set of bars (Wins)
    color='green',  # Color of the first set of bars
    label='Wins'  # Label for the first set of bars
)

# Add the second set of bars (Losses) stacked on top of the first set
plt.bar(
    teams,  # X-axis: Teams
    losses,  # Height of second set of bars (Losses)
    bottom=wins,  # Stack the second set of bars on top of the first set (Wins)
    color='red',  # Color of the second set of bars
    label='Losses'  # Label for the second set of bars
)

# Labeling
plt.xlabel('Teams')  # X-axis label
plt.ylabel('Count')  # Y-axis label
plt.title('Wins and Losses Comparison')  # Title of the plot
plt.legend()  # Display legend for the bars

plt.show()  # Show the plot
