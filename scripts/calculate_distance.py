import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# Load the data from CSV files
tracking_week_9 = pd.read_csv('tracking_week_9.csv')
plays = pd.read_csv('plays.csv')

# Keep only the relevant columns
tracking_week_9 = tracking_week_9[["gameId", "playId", "nflId", "displayName", "frameId", "time", "club", "playDirection", "x", "y", "s", "a", "dis", "o", "dir", "event"]]
plays = plays[["gameId", "playId", "ballCarrierId", "ballCarrierDisplayName", "possessionTeam", "defensiveTeam"]]

# Convert gameId to string
tracking_week_9['gameId'] = tracking_week_9['gameId'].astype(str)
plays['gameId'] = plays['gameId'].astype(str)

# Merge the dataframes on playId and gameId
merged_data = pd.merge(tracking_week_9, plays, on=['playId', 'gameId'], how='outer')

# Function to calculate Euclidean distance
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Iterate over each playId and frameId to calculate distances
for play_id, frame_id in merged_data[['playId', 'frameId']].drop_duplicates().values:
    # Get the coordinates of the ball carrier for this play and frame
    ball_carrier_rows = merged_data[(merged_data['playId'] == play_id) & (merged_data['frameId'] == frame_id) & (merged_data['nflId'] == merged_data['ballCarrierId'])]
    if not ball_carrier_rows.empty:
        ball_carrier_row = ball_carrier_rows.iloc[0]
        ball_carrier_x = ball_carrier_row['x']
        ball_carrier_y = ball_carrier_row['y']

        # Calculate the distance from each player to the ball carrier
        merged_data.loc[(merged_data['playId'] == play_id) & (merged_data['frameId'] == frame_id), 'distance_to_ball_carrier'] = merged_data[(merged_data['playId'] == play_id) & (merged_data['frameId'] == frame_id)].apply(
            lambda row: calculate_distance(row['x'], row['y'], ball_carrier_x, ball_carrier_y) if row['nflId'] != row['ballCarrierId'] else 0, axis=1)

# Select the desired columns
selected_data = merged_data[['nflId', 'displayName', 'club', 'possessionTeam', 'event', 'distance_to_ball_carrier', 'playId']]

# Filter out rows with NaN in the 'event' column
filtered_data = selected_data[selected_data['event'].notna()]

# Sort the data by playId, event, and distance_to_ball_carrier
sorted_data = filtered_data.sort_values(by=['playId', 'event', 'distance_to_ball_carrier'])

# Print the sorted data
print(sorted_data.head(500))

# Save the merged data to a new CSV file
merged_data.to_csv('week_9_distance.csv', index=False)

# Print the count of total records
print(f"Total records in merged data: {len(merged_data)}")
