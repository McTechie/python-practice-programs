"""
https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDEDUC2
Go through basic_pandas.py
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")

'''
DMDEDUC2 variable reflects a person's level of educational attainment
BMXWT variable reflects body weight
BPXSY1 variable reflects the 1st (out of 3) of systolic blood pressure measurements taken
BPXDI1 variable reflects the 1st (out of 3) of diastolic blood pressure measurements taken
'''

"""FREQUENCY TABLES"""

'''
The value_counts() method produces a table (Pandas Data Frame) with two columns
The first column contains all distinct observed values for the variable
The second column contains the number of times each of these values occurs
'''

print(da.DMDEDUC2.value_counts())
# Different from .unique() function - which returns a list of all unique values

'''
The value_counts() method excludes missing values
'''
# To calculate the sum of the no. of times the distinct values appear
print(da.DMDEDUC2.value_counts().sum())
# Note : da.DMDEDUC2.sum() gives the sum of all the values of that column

# To verify that value_counts() does not take missing values
print(da.shape) # Shows a tuple ~ (rows,columns)
print(pd.isnull(da.DMDEDUC2).sum())

'''Replacing integer codes with a text label'''

# To create a new variable that is recoded with text labels
da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College",
                                       7: "Refused", 9: "Don't know"})
# Generating frequency distribution
print(da.DMDEDUC2x.value_counts())

da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})

x = da.DMDEDUC2x.value_counts()  # x is just a name to hold this value temporarily
print(x / x.sum())

# Creating a new category called "Missing", and assign all missing values using .fillna()
da["DMDEDUC2x"] = da.DMDEDUC2x.fillna("Missing")
x = da.DMDEDUC2x.value_counts()
print(x / x.sum())

"""Numerical Summaries"""

# We drop missing values using the .dropna() method
print(da.BMXWT.dropna().describe())

x = da.BMXWT.dropna()  # Extract all non-missing values of BMXWT into a variable called 'x'
print(x.mean()) # Pandas method
print(np.mean(x)) # Numpy function

print(x.median())
print(np.percentile(x, 50))  # 50th percentile, same as the median
print(np.percentile(x, 75))  # 75th percentile
print(np.percentile(x, 25))  # 25th percentile
print(x.quantile(0.75)) # Pandas method for quantiles, equivalent to 75th percentile

# Calculate the proprotion of the NHANES sample who would be considered to have pre-hypertension.
print(np.mean((da.BPXSY1 >= 120) & (da.BPXSY2 <= 139))) # based on systolic bp
print(np.mean((da.BPXDI1 >= 80) & (da.BPXDI2 <= 89))) # based on diastolic bp

a = (da.BPXSY1 >= 120) & (da.BPXSY2 <= 139)
b = (da.BPXDI1 >= 80) & (da.BPXDI2 <= 89)
print(np.mean(a | b))

'''
Blood pressure measurements are affected by a phenomenon called
"white coat anxiety", in which a subject's bood pressure may be slightly
elevated if they are nervous when interacting with health care providers.
Typically this effect subsides if the blood pressure is measured several times in sequence.
'''

# Calculate the extent to which white coat anxiety is present in the
# NHANES data by looking a the mean difference between the first two systolic
# or diastolic blood pressure measurements.

sns.distplot(da.BMXWT.dropna())
plt.show()

sns.distplot(da.BPXSY1.dropna())
plt.show()

bp = sns.boxplot(data=da.loc[:, ["BPXSY1", "BPXSY2", "BPXDI1", "BPXDI2"]])
_ = bp.set_ylabel("Blood pressure in mm/Hg")
plt.show()

'''Stratification'''

da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80]) # Create age strata based on these cut points
plt.figure(figsize=(12, 5))  # Make the figure wider than default (12cm wide by 5cm tall)
sns.boxplot(x="agegrp", y="BPXSY1", data=da)  # Make boxplot of BPXSY1 stratified by age group
plt.show()

da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
plt.figure(figsize=(12, 5))
sns.boxplot(x="agegrp", y="BPXSY1", hue="RIAGENDRx", data=da)
plt.show()

da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
plt.figure(figsize=(12, 5))
sns.boxplot(x="RIAGENDRx", y="BPXSY1", hue="agegrp", data=da)
plt.show()

print(da.groupby("agegrp")["DMDEDUC2x"].value_counts())

dx = da.loc[~da.DMDEDUC2x.isin(["Don't know", "Missing"]), :]  # Eliminate rare/missing values
dx = dx.groupby(["agegrp", "RIAGENDRx"])["DMDEDUC2x"]
dx = dx.value_counts()
dx = dx.unstack() # Restructure the results from 'long' to 'wide'
dx = dx.apply(lambda x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
print(dx.to_string(float_format="%.3f"))  # Limit display to 3 decimal places
