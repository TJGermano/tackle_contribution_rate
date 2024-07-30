import matplotlib.pyplot as plt
import pandas as pd

## Load the data
df = pd.read_csv('tackle_distance_data.csv')

# Filter the DataFrame to include only players with a minimum of 100 plays
df_filtered = df[df['totalPlays'] >= 100]
# Load the data
df = pd.read_csv('tackle_distance_data.csv')

# Filter the DataFrame to include only players with a minimum of 100 plays
df_filtered = df[df['totalPlays'] >= 100].copy()

# Define the calculation for tackle contribution rate using .loc to avoid warnings
df_filtered.loc[:, 'tackle_contribution_rate'] = df_filtered['within_1_yard'] / (df_filtered['within_1_yard'] + df_filtered['totalPlays'])

# Select the top 100 players based on tackle contribution rate
top_100_players = df_filtered.nlargest(100, 'totalTackles')

# Sort the top 100 players by total tackles and total plays
top_100_sorted_by_tackles = top_100_players.sort_values(by=['totalTackles', 'totalPlays'], ascending=[False, False])

# Display the result
print(top_100_sorted_by_tackles[['displayName_x', 'totalTackles', 'within_1_yard', 'totalPlays', 'tackle_contribution_rate']])
