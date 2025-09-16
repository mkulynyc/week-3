import seaborn as sns
import pandas as pd
import numpy as np

"""
Exercise 1: Recursive Fibonacci Function

This fib(n) function recursively calculates the nth Fibonacci number.

Arguments:
- n: An integer representing the position in the Fibonacci sequence.

Returns:
- The nth Fibonacci number.
"""

def fibonacci(n):
    # Return 0 if n is 0
    if n <= 0:
        return 0
    
    # Return 1 if n is 1 (1st Fibonacci number)
    elif n == 1:
        return 1
    
    # Otherwise, return the sum of the 2 preceding Fibonacci numbers recursively
    else:
        return fib(n - 1) + fib(n - 2)
    

"""
Exercise 2: Integer to Binary conversion

This to_binary(x) function recursively converts an integer to binary

Arguments: 
- x: An integer to be converted to binary.

Returns:
- A string representing the binary equivalent of the integer.
"""

def to_binary(x):
    # Base case 1: if x is 0, return 0
    if x == 0:
        return "0"
    
    # Base case 2: if x is 1, return 1
    elif x == 1:
        return "1"
    
    # Recursive case: integer divide x by 2 and append the remainder of x divided by 2
    else:
        return to_binary(x // 2) + str(x % 2)
    

""" Exercise 3 """
def task_1():
    """
    This function returns a list of the column names in the dataframe 
    sorted by the number of missing values (NA) in each column, from least to most.
    It first fixes the issue in the gender column on how missing data was stored.

    Arguments:
    - None

    Returns:
    - A sorted list of column names based on the number of missing values.
    
    """
    # Load the dataset
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)


    # Filter for the rows where gender should be missing
    gender_filter = (df_bellevue['gender'] == '?') | \
                    (df_bellevue['gender'] == 'g') | \
                    (df_bellevue['gender'] == 'h') 

    # Replace the incorrect values with NaN
    df_bellevue.loc[gender_filter, 'gender'] = np.nan

    # Get the NA counts per column, then create a sorting filter
    na_counts = df_bellevue.isna().sum()
    missing_sort = na_counts.sort_values()

    # Apply this to the dataframe, then return a list of columns names
    df_bellevue = df_bellevue[missing_sort.index]
    cols = df_bellevue.columns.tolist()
    print("Missing gender data was stored as ?, g, or h. These have been replaced with NaN")
    return cols


def task_2():
    """
    This function returns a dataframe with two columns: year and count.
    The year column contains the years found in the date_in column of the 
    dataset, and the count column contains the number of entries for each year.
    The years had to be extracted first.
    

    Arguments:
    - None

    Returns:
    - A dataframe with two columns: year and count.
    
    """
    # Load the dataset
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)

    # Get the years in the date_in column
    df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce')
    print("Dates were stored in YYYY-MM-DD format. I extracted the year using pandas.")

    # Count the number of entries for each year
    year_counts = df_bellevue['date_in'].dt.year.value_counts().sort_index()

    # Return as a dataframe
    year_df = pd.DataFrame({
        "year": year_counts.index,
        "total_admissions": year_counts.values
    })
    return(year_df)


def task_3():
    """
    This function returns a series with the average age for each gender listed in the dataset.
    It first groups the data by gender, then calculates the mean age for each group.

    Arguments:
    - None

    Returns:
    - A series with the average age for each gender.

    """

    # Load the dataset
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)

    # Group the DF by gender and calculate the mean age for each    
    avg_ages = df_bellevue.groupby('gender')['age'].mean()
    print("I utilized the pandas groupby function to group the data by the gender, " \
            "then calculated the mean for each")
    return(avg_ages)


def task_4():
    """
    This function returns a list of the 5 most common professions in the dataset.

    Arguments:
    - None

    Returns:
    - A list with the 5 most common professions.
    """
    # Load the dataset
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)

    # Get the 5 most common professions return as a list
    prof_counts = df_bellevue['profession'].value_counts().head(5)
    prof_list = prof_counts.index.tolist()
    return(prof_list)


