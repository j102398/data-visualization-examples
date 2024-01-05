import matplotlib.pyplot as plt

# Assuming you have time series data for a team's performance
time_periods = ['Jan', 'Feb', 'Mar', 'Apr']
points_over_time = [50, 55, 60, 58]  # Example points earned each month

plt.figure(figsize=(8, 5))

# Plotting the line chart
plt.plot(
    time_periods,  # x-axis data (time periods)
    points_over_time,  # y-axis data (points earned)
    marker='x',  # Marker style (x for cross marker)
    linestyle='-',  # Line style (- for solid line)
    color='blue'  # Line color (b for blue)
)

# Labeling and titling the plot
plt.xlabel('Time')
plt.ylabel('Points')
plt.title('Team Performance Over Time')
plt.grid(True)  # Display gridlines
plt.show()  # Show the plot
