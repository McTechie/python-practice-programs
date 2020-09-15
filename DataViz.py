import seaborn as sns # For plotting
import matplotlib.pyplot as plt # For showing plots

'''
The tips data set is a default data set within Seaborn that allows us
to analyze the size of the tip according to different factors such as
someone's gender, the day of the week, the total bill size, or any other factor
that we maybe interested in.
'''
# Load in the data set
tips_data = sns.load_dataset("tips")

'''Visualizing Tables'''
'''
# Print out the first few rows of the data
print(tips_data.head())
'''
'''Describing Data'''
'''
# Print out the summary statistics for the quantitative variables
print(tips_data.describe())
'''
'''Creating a Histogram'''
'''
# Plot a histogram of the Total Bill
sns.distplot(tips_data["total_bill"], kde = False).set_title("Histogram of Total Bill")
# Python, by deafult in the Seaborn package always includes a density plot.
# This density plot is represented by 'kde' parameter
plt.show()

# Plot a histogram of the Tips only
sns.distplot(tips_data["tip"], kde = False).set_title("Histogram of Total Tip")
plt.show()
'''
'''
# Plot a histogram of both the total bill and the tips'
sns.distplot(tips_data["total_bill"], kde = False)
sns.distplot(tips_data["tip"], kde = False).set_title("Histogram of Both Tip Size and Total Bill")
plt.show()
'''
'''Creating a Boxplot'''
'''
# Create a boxplot of the total bill amounts
sns.boxplot(tips_data["total_bill"]).set_title("Box plot of the Total Bill")
plt.show()
'''
'''
# Create a boxplot of the tips amounts
sns.boxplot(tips_data["tip"]).set_title("Box plot of the Tip")
plt.show()
'''
'''
# Create a boxplot of the tips and total bill amounts - do not do it like this
sns.boxplot(tips_data["total_bill"])
sns.boxplot(tips_data["tip"]).set_title("Box plot of the Total Bill and Tips")
plt.show()
'''
'''Creating Histograms and Boxplots plotted by Groups'''
'''
# Create a boxplot and histogram of the tips grouped by smoking status
sns.boxplot(x = tips_data["tip"], y = tips_data["smoker"])
# 'x' parameter is what you want to plot
# 'y' parameter is what you want to group by
plt.show()
'''
'''
# Create a boxplot and histogram of the tips grouped by time of day
sns.boxplot(x = tips_data["tip"], y = tips_data["time"])
g = sns.FacetGrid(tips_data, row = "time")
g = g.map(plt.hist, "tip")
plt.show()
'''
'''
# Create a boxplot and histogram of the tips grouped by the day
sns.boxplot(x = tips_data["tip"], y = tips_data["day"])
g = sns.FacetGrid(tips_data, row = "day")
g = g.map(plt.hist, "tip")
plt.show()
'''
