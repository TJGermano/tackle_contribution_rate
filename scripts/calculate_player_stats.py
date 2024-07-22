import pandas as pd
import play_count_exploration

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.2f}'.format)
# Load the data from the CSV files
tackles_data = pd.read_csv('tackles.csv')
players_data = pd.read_csv('players.csv')

# Merge the tackles data with the players data on nflId
merged_data = pd.merge(tackles_data, players_data, on='nflId', how='left')

# Calculate the total tackles, missed tackles, and assists for each player
player_stats = merged_data.groupby(['nflId', 'displayName', 'position']).agg({
    'tackle': 'sum',  # Assuming 'tackle' column is 1 for a tackle and 0 otherwise
    'pff_missedTackle': 'sum',  # Adjusted column name to 'missedTackles'
    'assist': 'sum'  # Assuming 'assist' column is 1 for an assist and 0 otherwise
}).reset_index()

# Rename the columns for clarity
player_stats.columns = ['nflId', 'displayName', 'position', 'totalTackles', 'pff_missedTackle', 'assists']


merged_data = pd.merge(player_stats, play_count_exploration.top_defensive_players_overall, on='nflId', how='inner').sort_values(by='within_1_yard', ascending=False)
print(merged_data[['nflId', 'displayName_x', 'position', 'totalTackles','assists','within_1_yard','within_3_yards','within_5_yards','totalPlays']])

# Save all columns of merged_data to a CSV file
#merged_data.to_csv('tackle_distance_data.csv', index=False)
