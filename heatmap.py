import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
# Example correlation matrix (replace with your actual data)
data = {
    'Wins': [1.0, 0.7, 0.3],
    'Goals Scored': [0.7, 1.0, 0.5],
    'Goal Difference': [0.3, 0.5, 1.0]
}

# Create a DataFrame with the correlation matrix
correlation_matrix = pd.DataFrame(data)

plt.figure(figsize=(6, 4))

# Create the heatmap using seaborn
sns.heatmap(
    correlation_matrix,  # Data for the heatmap
    annot=True,  # Show data values in each cell
    cmap='coolwarm',  # Color map for the heatmap
    fmt='.2f'  # Number format for annotations (two decimal places)
)

plt.title('Correlation Heatmap')  # Set the title of the plot
plt.show()  # Show the heatmap
