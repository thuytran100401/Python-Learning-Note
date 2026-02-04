# load_data.py

import os
import pandas as pd
import random
import math
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_csv(filename):
    """
    Load CSV file safely.
    Returns a pandas DataFrame or None if failed
    """
    file_path = os.path.join(BASE_DIR, filename)

    try:
        df = pd.read_csv(file_path)
        print(f"Loaded '{filename}' successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except pd.errors.EmptyDateError:
        print(f"Error: File '{filename}' is empty.")
        return None
    except pd.error.ParserError:
        print(f"Error: File '{filename}' is invalid or corrupted.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def save_csv(df, filename):
    """
    Save DataFrame safely to CSV.
    """
    if df is None:
        print("No data to save.")
        return
    
    try:
        df.to_csv(filename, index=False)
        print(f"Data saved to '{filename}' successfully.")
    except PermissionError:
        print(f"Permission denied: Cannot write to '{filename}'")
    except Exception as e:
        print(f"Unexpected error: {e}")

def read_txt(filename):
    """
    Read TXT file safely.
    Returns a list of lines or None if failed.
    """
    file_path = os.path.join(BASE_DIR, filename)
    try:
        with open(file_path, "r") as f:
            lines = [line.strip() for line in f]
        print(f"Loaded '{filename}' successfully. {len(lines)} lines.")
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def write_txt(lines, filename):
    """
    Write list of lines to TXT safely.
    """
    try:
        with open(filename, "w") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"TXT saved to '{filename}' successfully.")
    except PermissionError:
        print(f"Permission denied: Cannot write to '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Count lines in file
def count_lines(filename):
    try:
        with open(filename, "r") as f:
            return sum(1 for _ in f)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

# Work with the file system 
# List files in the current project folder
def list_files():
    print("Files in project folder:")
    for file in os.listdir(BASE_DIR):
        print("-", file)

# Randomly sample rows from a DataFrame
def random_sample(df, n=3):
    if df is None:
        print("No data to sample.")
        return None
    
    n = min(n, len(df))
    sample = df.sample(n)
    print(f"Random sample ({n} rows):")
    return sample

# math - Basic Calculations
def average_salary(df):
    if df is None or "salary" not in df.columns:
        print("Salary column not found.")
        return None

    avg = df["salary"].mean()
    print("Average Salary:", math.floor(avg))
    return avg


# Example Usage
if __name__ == "__main__":
    # CSV Example
    df = load_csv("dataset.csv")
    if df is not None: 
        save_csv(df.head(5), "dataset_head.csv")

    # TXT Example
    lines = read_txt("foods.txt")
    if lines:
        lines.append("Ice Cream")
        write_txt(lines, "foods_updated.txt")
        print("Total lines in file:", count_lines("foods_updated.txt"))

    # Test List Files
    list_files()

    # Test Random 
    df = load_csv("dataset.csv")
    sample = random_sample(df, 3)
    print(sample)

    # Test Math
    df = load_csv("dataset.csv")
    average_salary(df)

    # sys - Command Line Arguments
    if len(sys.argv) < 2:
        print("Usage: Python load_data.py <filename>")
        sys.exit()

        filename = sys.argv[1]

        df = load_csv(filename)
        if df is not None:
            list_files()
            random_sample(df, 3)
            average_salary(df)