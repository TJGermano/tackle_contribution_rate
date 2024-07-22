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
Here is a list of scripts included in this repository:

### Data Manipulation
- `scripts/calculate_distance.py`: This script reads the raw data from Kaggle, processes it to calculate the distance of each player to the ball carrier for each frame, and outputs the data in a new form suitable for analysis. 
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

### Note:
- This script needs to be run separately for each week of tracking data. Update the script to load the appropriate week's data file before running it.
- Ensure you have all the necessary Python libraries installed. You can install them using:

    ```sh
    pip install pandas numpy
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
