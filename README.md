# Recommendation System for Predicting Ratings

This project is a recommendation system implemented in Python that predicts ratings for new users based on similarities with existing users. It uses collaborative filtering techniques, calculating similarities between users and predicting ratings for items that the new users haven't rated yet. The system is built using Python and leverages Pandas and NumPy for data manipulation and mathematical operations.

## Features

- *Collaborative Filtering*: Uses user-based collaborative filtering to find similar users and predict ratings for new users.
- *Similarity Calculation*: Calculates the similarity between existing and new users using Pearson correlation.
- *Prediction*: Predicts the rating of items for new users based on the ratings of similar existing users.
- *Data Handling*: Handles missing data by replacing it with zeros and ensures proper numerical calculations.

## Prerequisites

Before running the script, ensure that you have Python installed along with the required libraries:

1. [Python](https://www.python.org/downloads/) (version 3.7 or higher recommended)
2. Required Python libraries:
   - [Pandas](https://pandas.pydata.org/)
   - [NumPy](https://numpy.org/)
   
You can install the required libraries using pip:

bash
pip install pandas numpy


## How It Works

1. *Data Loading*:
   - The script reads a .csv file containing user-item ratings. The first 20 rows correspond to existing users (U1 to U20), and the last 5 rows correspond to new users (NU1 to NU5).

2. *Similarity Calculation*:
   - The script calculates the similarity between each new user and all existing users using the Pearson correlation formula.
   
3. *Nearest Neighbors Selection*:
   - The script selects the top-k similar users for each new user, which are used to predict the ratings for unrated items.

4. *Prediction*:
   - The system predicts ratings for items that the new users have not rated based on the ratings of the most similar users.

5. *Display Results*:
   - The predicted rating with the highest value for each new user is displayed.

## Usage

### Step 1: Prepare the Dataset

Ensure you have a .csv file named RecomendationDataSet.csv with the following structure:

- *Rows 0-19*: Existing users (U1 to U20) with their ratings for various items (columns 1-9).
- *Rows 20-25*: New users (NU1 to NU5) with their ratings (or lack thereof).

Each row represents a user, and each column represents a different item or book.

### Step 2: Run the Script

1. Place the dataset (RecomendationDataSet.csv) in the same directory as the script.
2. Run the main.py script to execute the recommendation system:

   bash
   python main.py
   

### Step 3: View Results

- The script will print the predicted highest rating and the corresponding item for each new user.

## Script Overview

### Main Functions

1. **read_csv(path)**: Reads the dataset from the specified path, processes the data, and returns the users' data as NumPy arrays and DataFrames.
2. **sim(a_person, b_person)**: Calculates the similarity matrix between existing and new users using Pearson correlation.
3. **n_sim(k, sim_matrix)**: Selects the top-k similar users for each new user and returns a DataFrame with the similarities.
4. **pred(persons_U, persons_NU, df_NU)**: Predicts ratings for items not rated by the new users based on similar users' ratings.
5. **calc_maxPoint(pred)**: Finds and displays the item with the highest predicted rating for each new user.
6. **display(key, book_name, point)**: Prints the results in a user-friendly format.

### Example Output

NU1:
Book_5 : 4.3

NU2:
Book_7 : 3.8

NU3:
Book_2 : 4.1
