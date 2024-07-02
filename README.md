# Word Count Processing Project

## Project Overview

This project processes text data from a CSV file, counts the frequency of words while ignoring common words, and stores the results in an SQLite database. The project also includes functionality to clean text by removing numbers and emojis.

## Project Structure

The project consists of the following files:

- **`main.py`**: The main script that processes the CSV file.
- **`pre_processing.py`**: Read and write data, from raw input CSV file to clean data to process futher.
- **`processing.py`**: Create table if it doesn't exist, does word counting and Moves the processed file to processed_data folder.
- **`helpers.py`**: Utils functions, which removes numbers or emojis if there any
- **`config.json`**: Contains file, folder path and common words.
- **`raw_data/`**: Directory where raw file (source/input) CSV files are.
- **`raw_data.csv`**: The input data CSV file.
- **`word_count.db`**: The SQLite database where the word count data is stored.
- **`processed_data/`**: Directory where processed CSV files are moved.
- **`clean_data.csv`**: The CSV file with cleaned text data.


## Setup Instructions

## To run the application, follow these steps:
> Clone the Repository: git clone https://github.com/madlearner/Word_Count_Project.git

> Set Up Virtual Environment: 
1. Create a virtual environment (optional but recommended): python -m venv .env
2. Activate the virtual environment: .env\Scripts\activate
3. Install the required dependencies: pip install -r requirements.txt

# Usage

- Change directory and Excute the main.py program
>> py main.py

- To check the data in the SQL Table:
Change the directory to word_frequency/ and then run the command
>> sqlite3 word_frequency.db
>> .headers on
>> .mode column
>> SELECT * FROM word_frequency;

(Note: If you want to provide any csv file of the structure (“id”, “source”, “original_text”), then drop the file in raw_data/ folder)
