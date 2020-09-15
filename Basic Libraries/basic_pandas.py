"""
Pandas is a very useful tool used to create Data Frames for data analysis
and data manipulation in Python
"""

import pandas as pd

# Show all columns when looking at dataframe
# If not included, we will see continued dots (...) to represent multiple columns and rows
pd.set_option('display.max_columns', 100) # For no. of columns upto 100

# Selecting a file containing the dataset
#url = "car_sales.json"
url = "nhanes_2015_2016.csv"

# The read_xxx() function is used, where xxx refers to any file format
# xxx may be json/csv/etc.
#df = pd.read_json(url)
df = pd.read_csv(url)
'''
# The head() function shows by deafult the first 5 rows of our Data Frame
print(df.head()) # df.head(7) will show first 7 rows
print("===================================================")

# Outputs entire Data Frame
print(df)
print("===================================================")

# To return a tuple consisting of the no. of rows
# and no. of columns in the given data set
print(df.shape)
print("===================================================")

# To see the names of the columns in the Pandas Data Frame
print(df.columns)
print("===================================================")

# To confirm the data types are consistent, with what the variables represent
# Returns the data types of the column names of the data frame
print(df.dtypes)
print("===================================================")
'''
''' SLICING IN PANDAS - '''
'''
# The .loc() takes two argumnets separated by ','
# The first one indicates the rows and the second one indicates columns
print(df.loc[:4]) # Rows 0-4 for all columns
print(df.loc[:,"price"]) # All observations for "price" column
print(df.loc[:9,["price","total_sales"]]) # Rows 0-9 of multiple columns
print("===================================================")

# The .iloc() function is integer slicing and does not take column labels/names
print(df.iloc[:4]) # Rows 0-3 for all columns
print(df.iloc[1:5, 2:4]) # Rows 1-4 for columns 2-3
print(df.iloc[3,:]) # Extracting row 3 from the data set
print("===================================================")
'''
''' REFERRING TO COLUMNS OF THE DATA FRAME - '''
'''
print(df["price"])
print(df.loc[:,"price"])
print(df.price)
print(df.iloc[:,2]) # The "price" column is column no. '2'

# One way to get the column names we want to keep is simply by copying from the above output and storing in a list
keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC','BMXWAIST']
# We can also use list comprehension as [column for column in col_names if 'BMX' in column]
df_BMX = df[keep]
print(df_BMX.head())
print("===================================================")

# The max() function returns the maximum value over all of the column values
print(df.price.max())
print("===================================================")

# The unique() function is used to "list" all the unique values in any column
print(df.id.unique()) # All id are unique here
print("===================================================")

# To check whether the data set has a missing value
print(pd.isnull(df.price)) # Results True for a missing value and vice versa
print(pd.isnull(df.price).sum()) # Returns the total no. of missing values
print("===================================================")

# To check whether the data set does not a missing value
print(pd.notnull(df.price)) # Results True for no missing value and vice versa
print(pd.notnull(df.price).sum()) # Returns the total no. of non-missing values
print("===================================================")

# To split/group the data into groups based on a certain criteria
gk = df.groupby(['price'])
print(gk.first()) # To print the first entries in all the groups formed
print(gk.get_group("$9907.57")) # Finding the values in the $9907.57 group
print("===================================================")

# To first group by 'total_sales'
# Within each total_sales we are gouping by 'price'
gkk = df.groupby(['total_sales','price'])
print(gkk.first())
'''
'''
#The value_counts() method produces a table (Pandas Data Frame) with two columns
#The first column contains all distinct observed values for the variable
#The second column contains the number of times each of these values occurs

print(df.DMDEDUC2.value_counts())
'''
''' NUMERICAL SUMMARIES - '''
'''
print(df.describe())
'''
