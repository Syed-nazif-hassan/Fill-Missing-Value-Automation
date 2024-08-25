# Fill Missing Value Automation Using Python

## This automation project identifies cells with missing values in a DataFrame column and provides options in the terminal to fill these cells using the mean, median, or mode. This project utilizes the Python library, Pandas.

### To run this project-

- Clone the repository
- Set up a Virtual Environment
- Install Pandas

### How to use this automation project-

- Import the `fill_value.py` file into the script where you want to use this project.

```python
import fill_value
```

- The `fill_value.py` file contains three functions: `iterate_over_each_cell`, `full_dataset`, and `specific_columns`. The `iterate_over_each_cell` function is not used directly; instead, you will use `full_dataset` and `specific_columns`.
- The `full_dataset` function takes one argument: the DataFrame. It identifies columns with missing values and prompts you in the terminal to choose how to fill these missing values—using the mean, median, or mode. After making your selection, the function updates the DataFrame and returns the modified DataFrame.

```python
updated_dataframe = fill_value.full_dataset(dataframe)
print(updated_dataframe)
```

- The `specific_columns` function takes two arguments: the DataFrame and a list of column names in which you want to find and fill missing values. You can provide a single column name or multiple column names as needed. The function will prompt you to choose how to fill the missing values in each specified column—using the mean, median, or mode. After making your selections, the function updates the DataFrame and returns the modified DataFrame.

```python
column_names = ['A', 'B', 'C', 'D']
updated_dataframe = fill_value.specific_columns(dataframe, column_names)
print(updated_dataframe)
```

- Type 'off' when prompted for the mean, median, or mode to stop the process.

#### _If you receive an error indicating that a column does not exist in the DataFrame, even though you are certain it does, ensure that there is no leading or trailing whitespace in the column names. Remove any extra whitespace from the column names in the DataFrame and in your list of column names before trying again. You can use the `strip()` method to remove whitespace from column names._

```python
df.columns = df.columns.str.strip()
```

#### _Also, make sure the data types of the column names in your list match the data types of the column names in the DataFrame to prevent errors._
