import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv('tackle_distance_data.csv')

# Filter the DataFrame to include only players with a minimum of 100 plays
df_filtered = df[df['totalPlays'] >= 100].copy()

# Calculate the tackle contribution rate
df_filtered['tackle_contribution_rate'] = df_filtered['within_3_yards'] / (df_filtered['within_3_yards'] + df_filtered['totalPlays'])

# Select the top 25 players based on total tackles
top_25_players = df_filtered.nlargest(25, 'totalTackles')
print(top_25_players)
# Calculate averages for the top 25 players
average_tackles = top_25_players['totalTackles'].mean()
average_contribution = top_25_players['tackle_contribution_rate'].mean()

# Create the scatter plot with adjusted axes
plt.figure(figsize=(16, 12))
plt.scatter(top_25_players['totalTackles'], top_25_players['tackle_contribution_rate'], color='blue', edgecolor='k')

# Add player names to the points on the plot with a conditional offset
for i, player in top_25_players.iterrows():
    if player['totalTackles'] > average_tackles:
        plt.text(player['totalTackles'] + 0.5, player['tackle_contribution_rate'], player['displayName_x'], fontsize=9, ha='left')
    else:
        plt.text(player['totalTackles'] - 0.5, player['tackle_contribution_rate'], player['displayName_x'], fontsize=9, ha='right')

# Add lines for the average values
plt.axhline(y=average_contribution, color='r', linestyle='--', linewidth=1)
plt.axvline(x=average_tackles, color='r', linestyle='--', linewidth=1)

# Adjust the limits of the plot to center the axes and zoom in a bit
plt.xlim(top_25_players['totalTackles'].min() - 10, top_25_players['totalTackles'].max() + 10)
plt.ylim(top_25_players['tackle_contribution_rate'].min() - 0.1, top_25_players['tackle_contribution_rate'].max() + 0.1)

# Add labels and title
plt.xlabel('Total Tackles')
plt.ylabel('Tackle Contribution Rate')
plt.title('Top 25 Players by Total Tackles and Tackle Contribution Rate')

# Display the plot
plt.grid(True)
plt.show()

# Export the DataFrame with all players to a CSV file
#df_filtered.to_csv('all_players_3_yard_tackle_contribution.csv', index=False)
