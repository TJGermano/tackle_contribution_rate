# tackle_contribution_rate
# My Data Analysis Project

## Introduction
This repository contains the scripts and analysis for my data analysis project.

## Data
The raw data used in this project is sourced from Kaggle. Below are the links to the datasets:

- https://www.kaggle.com/competitions/nfl-big-data-bowl-2024/data

## Usage
To use the scripts in this repository, download the datasets from Kaggle and place them in the `data` directory.

## Scripts

### Data Manipulation
- `scripts/calculate_distance.py`: This script reads the raw data from Kaggle, processes it to calculate the distance of each player to the ball carrier for each frame, and outputs the data in a new form suitable for analysis. 

### Player Play Accumulation
- `scripts/accumulate_player_plays.py`: This script aggregates the total number of plays for each player and calculates the number of plays within each distance bucket (1 yard, 3 yards, 5 yards) from the ball carrier during tackle events.

### Player Statistics Calculation
- `scripts/calculate_player_stats.py`: This script merges the tackles and players data, calculates the total tackles, missed tackles, and assists for each player, and merges this with the distance data. It can also export the final dataset to a CSV file.

## Usage

### Steps to Use the Data Manipulation Script:

1. **Download the Script**:
   - Download the `calculate_distance.py` script from this repository.

2. **Download the Data**:
   - Download the raw datasets from Kaggle using the links provided in the [Data](#data) section.
   - Place the downloaded CSV files in a folder named `data`.

3. **Run the Script**:
   - Make sure you have Python installed on your machine.
   - Open a terminal or command prompt.
   - Navigate to the directory where the script and the data folder are located.
   - Run the script using the following command:

     ```sh
     python scripts/calculate_distance.py
     ```

   - The script will process the data and generate a new CSV file with the distances calculated.

### Steps to Use the Player Play Accumulation Script:

1. **Download the Script**:
   - Download the `accumulate_player_plays.py` script from this repository.

2. **Ensure Data Availability**:
   - Ensure you have run the `calculate_distance.py` script for each week of data and have the resulting `week_X_distance.csv` files.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script and the data files are located.
   - Run the script using the following command:

     ```sh
     python scripts/accumulate_player_plays.py
     ```

   - The script will process the data and print the results for defensive players sorted by plays within 1 yard.

### Steps to Use the Player Statistics Calculation Script:

1. **Download the Script**:
   - Download the `calculate_player_stats.py` script from this repository.

2. **Ensure Data Availability**:
   - Ensure you have the `tackles.csv`, `players.csv`, and the results from `accumulate_player_plays.py`.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script and the data files are located.
   - Run the script using the following command:

     ```sh
     python scripts/calculate_player_stats.py
     ```

   - The script will process the data, calculate the player stats, and print the results. You can uncomment the line to save the final dataset to a CSV file if needed.

### Note:
- Ensure you have all the necessary Python libraries installed. You can install them using:

    ```sh
    pip install pandas numpy
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
