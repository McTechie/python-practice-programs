import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

da = pd.read_csv("nhanes_2015_2016.csv")

''' In a scatterplot with more than around 100 points, "overplotting" becomes
    an issue. One way to mitigate overplotting is to use an "alpha" channel
    to make the points semi-transparent, as done below '''

sns.regplot(x="BMXLEG", y="BMXARML", data=da, fit_reg=False, scatter_kws={"alpha": 0.3})

''' Another way to avoid overplotting is to make a plot of the "density" of
    points. In the plots below, darker colors indicate where a greater number
    of points fall. The two plot margins show the densities for the arm lengths
    and leg lengths separately, while the plot in the center shows their
    density jointly. '''

sns.jointplot(x="BMXLEG", y="BMXARML", kind='kde', data=da).annotate(stats.pearsonr)

''' Another example with slightly different behavior, we see that systolic and
    diastolic blood pressure (essentially the maximum and minimum blood
    pressure between two consecutive heart beats) are more weakly correlated
    than arm and leg length, with a correlation coefficient of 0.32 '''

sns.jointplot(x="BPXSY1", y="BPXDI1", kind='kde', data=da).annotate(stats.pearsonr)

''' Next we look at two repeated measures of systolic blood pressure, taken
    a few minutes apart on the same person. These values are very highly
    correlated, with a correlation coefficient of around 0.96 '''

jp = sns.jointplot(x="BPXSY1", y="BPXSY2", kind='kde', data=da).annotate(stats.pearsonr)

''' Another situation that commonly arises in data analysis is when we wish
    to analyze bivariate data consisting of one quantitative and one categorical
    variable. To illustrate methods that can be used in this setting, we
    consider the relationship between marital status and age in the NHANES data '''

da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College",
                                       7: "Refused", 9: "Don't know"})
da["DMDMARTLx"] = da.DMDMARTL.replace({1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "Never married",
                                      6: "Living w/partner", 77: "Refused"})
db = da.loc[(da.DMDEDUC2x != "Don't know") & (da.DMDMARTLx != "Refused"), :]

plt.figure(figsize=(12, 4))
a = sns.boxplot(db.DMDMARTLx, db.RIDAGEYR)

''' When we have enough data, a "violinplot" gives a bit more insight into the
    shapes of the distributions compared to a traditional boxplot. The
    violinplot below is based on the same data as the boxplot above. We can
    see quite clearly that the distributions with low mean (living with
    partner, never married) are strongly right-skewed, while the distribution
    with high mean (widowed) is strongly left-skewed. The other distributions
    have intermediate mean values, and are approximately symmetrically
    distributed. Note also that the never-married distribution has a long
    shoulder, suggesting that this distributions includes many people who are
    never-married because they are young, and have not yet reached the ages
    when people typically marry, but also a substantial number of people will
    marry for the first time anywhere from their late 30's to their mid-60's '''

plt.figure(figsize=(12, 4))
a = sns.violinplot(da.DMDMARTLx, da.RIDAGEYR)

plt.show()
