import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.2f}'.format)
# Initialize an empty DataFrame to store the aggregated data for all weeks
all_weeks_data = pd.DataFrame()

# Loop through each week's CSV file
for week in range(1, 10):
    # Load the merged data from the CSV file
    merged_data = pd.read_csv(f'week_{week}_distance.csv')

    # Filter for rows where the event is 'tackle'
    close_tackle_data = merged_data[(merged_data['event'] == 'tackle')].copy()

    # Determine if the player is on offense or defense
    close_tackle_data['side'] = 'Offense'
    close_tackle_data.loc[close_tackle_data['club'] == close_tackle_data['defensiveTeam'], 'side'] = 'Defense'

    # Add columns for distance ranges
    close_tackle_data['within_5_yards'] = close_tackle_data['distance_to_ball_carrier'] <= 5
    close_tackle_data['within_3_yards'] = (close_tackle_data['distance_to_ball_carrier'] > 1) & (
                close_tackle_data['distance_to_ball_carrier'] <= 3)
    close_tackle_data['within_1_yard'] = close_tackle_data['distance_to_ball_carrier'] <= 1

    # Append the data for this week to the aggregated DataFrame for all weeks
    all_weeks_data = pd.concat([all_weeks_data, close_tackle_data])

# Calculate total plays (unique playId) per player across all weeks
total_plays_per_player = all_weeks_data.groupby(['nflId', 'displayName', 'club', 'side'])['playId'].nunique().reset_index()
total_plays_per_player.columns = ['nflId', 'displayName', 'club', 'side', 'totalPlays']

# Group by nflId and side to get the count of plays each player was close to the ball carrier for each distance range across all weeks
overall_player_close_count = all_weeks_data.groupby(['nflId', 'displayName', 'club', 'side']).agg({
    'within_1_yard': lambda x: (x == True).sum(),
    'within_3_yards': lambda x: ((x == True) & (~x.shift(fill_value=False))).sum(),
    'within_5_yards': lambda x: ((x == True) & (~x.shift(fill_value=False))).sum()
}).reset_index()

# Merge total plays data with overall player close count
merged_data = pd.merge(overall_player_close_count, total_plays_per_player, on=['nflId', 'displayName', 'club', 'side'], how='left')

# Filter for defensive players and sort by plays within 1 yard
top_defensive_players_overall = merged_data[merged_data['side'] == 'Defense'].sort_values(by='within_1_yard', ascending=False)

# Print or use the data as needed
#print(top_defensive_players_overall[['displayName', 'club', 'side', 'totalPlays', 'within_1_yard', 'within_3_yards', 'within_5_yards']])
