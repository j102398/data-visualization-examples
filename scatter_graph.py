import matplotlib.pyplot as plt

teams = ['Team A', 'Team B', 'Team C', 'Team D']
points = [60, 55, 50, 48]
wins = [18, 17, 15, 14]

plt.figure(figsize=(8, 5))
plt.scatter(wins, points, color='red')
plt.xlabel('Wins')
plt.ylabel('Points')
plt.title('Wins vs. Points')
for i, team in enumerate(teams):
    plt.text(wins[i], points[i], team)
plt.show()
