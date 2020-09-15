import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe

# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")

print(df.head())

# get columns names
col_names = df.columns
print(col_names)

''' One way to get the column names we want to keep is simply by
    copying from the above output and storing in a list '''

keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC','BMXWAIST']
# OR by list comprehension
keep = [column for column in col_names if 'BMX' in column]

# use [] notation to keep columns
df_BMX = df[keep]
print(df_BMX.head())

print(df.loc[:, keep].head())

index_bool = np.isin(df.columns, keep)
print(df.iloc[:,index_bool].head()) # Indexing with boolean list

''' Lets only look at rows who 'BMXWAIST' is larger than the median '''

waist_median = pd.Series.median(df_BMX['BMXWAIST']) # get the median of 'BMXWAIST'
print(waist_median)
print(df_BMX[df_BMX['BMXWAIST'] > waist_median].head())

''' Lets add another condition, that 'BMXLEG' must be less than 32 '''

condition1 = df_BMX['BMXWAIST'] > waist_median
condition2 = df_BMX['BMXLEG'] < 32
print(df_BMX[condition1 & condition2].head())
# Note: can't use 'and' instead of '&'

print(df_BMX.loc[condition1 & condition2, :].head())
# note that the conditiona are describing the rows to keep

''' Lets make a small dataframe and give it a new index so can more clearly
    see the differences between .loc and .iloc '''

tmp = df_BMX.loc[condition1 & condition2, :].head()
tmp.index = ['a', 'b', 'c', 'd', 'e']
print(tmp)
print(tmp.loc[['a', 'b'],'BMXLEG'])
print(tmp.iloc[[0,1],3])

''' We can use the .loc and .iloc methods to change values
    within the dataframe '''
tmp.iloc[0:3,2] = [0]*3
print(tmp.iloc[:,2])

tmp.loc['a':'c','BMXBMI'] = [1]*3
print(tmp.loc[:,'BMXBMI'])

''' We can use the [] method when changing all the values of a column '''

tmp['BMXBMI'] = range(0, 5)
print(tmp)
