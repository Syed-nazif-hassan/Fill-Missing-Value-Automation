import pandas as pd


def iterate_over_each_cell(dataframe, column):

    for index, value in dataframe[column].items():
        # Check if the current cell is NaN (missing value)
        if pd.isna(value):
            while True:
                method = input(f"How would you like to fill this missing value in column '{
                               column}' at index {index}? (mean/median/mode): ").strip().lower()
                if method in ['mean', 'median', 'mode']:
                    if method == 'mean':
                        fill_value = dataframe[column].mean()
                    elif method == 'median':
                        fill_value = dataframe[column].median()
                    elif method == 'mode':
                        fill_value = dataframe[column].mode()[0]
                    # Fill the missing value in the specific cell
                    dataframe.at[index, column] = fill_value
                    break
                elif method == 'off':
                    exit()
                else:
                    print("Invalid input. Please choose 'mean', 'median', or 'mode'.")


# Find missing values from whole dataset
def full_dataset(dataframe):

    # Find columns with missing values
    columns_with_missing = dataframe.columns[dataframe.isnull().any()]

    if columns_with_missing.empty:
        print("No columns have missing values in the dataframe.\n\nFinished")
        return dataframe

    # Loop through each column with missing values
    for column in columns_with_missing:
        print(f"\nColumn {column}")
        # Iterate over each cell in the column
        iterate_over_each_cell(dataframe, column)

    # Return the DataFrame after filling missing values
    print("\nFinished")
    return dataframe


# Find missing values in specific columns
def specific_columns(dataframe, columns):

    # Check if the list is empty
    if not columns:
        print("\nList is empty.")
        return

    # Loop through each column provided in the arguments
    for column in columns:
        # Check if the column exists in the dataframe
        if column in dataframe.columns:
            # Check if the column has missing values
            if dataframe[column].isnull().any():
                print(f"\nColumn {column}")
                iterate_over_each_cell(dataframe, column)
            else:
                print(f"\nColumn {column} has no missing values.")
        else:
            print(f"\nColumn {column} does not exist in the dataframe.")

    # Return the DataFrame after filling missing
    print("\nFinished")
    return dataframe
