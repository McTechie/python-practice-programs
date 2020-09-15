"""
SciPy provides a large number of functions that operate on numpy arrays
and are useful for different types of scientific and engineering applications

The SciPy.Stats module contains a large number of probability distributions
as well as a growing library of statistical functions such as:
o Continuous and Discrete Distributions (i.e Normal, Uniform, Binomial, etc.)
o Descriptive Statistcs
o Statistical Tests (i.e T-Test)
"""
from scipy import stats
import numpy as np
'''
# Print Normal Random Variables
print(stats.norm.rvs(size = 10))
'''
'''
from pylab import *

# Create some test data
dx = .01
X  = np.arange(-2,2,dx)
Y  = exp(-X**2)

# Normalize the data to a proper PDF - Probability Density Function
Y /= (dx*Y).sum()

# Compute the CDF - Cumulative Density Function
CY = np.cumsum(Y*dx)

# Plot both
plot(X,Y) # Blue line
plot(X,CY,'r--') # Red line

show()
'''
'''
# Compute the Normal CDF of certain values.
print(stats.norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6])))
'''
'''
np.random.seed(282629734)

# Generate 1000 Student’s T continuous random variables.
x = stats.t.rvs(10, size=1000)

# Do some descriptive statistics
print(x.min())   # equivalent to np.min(x)
print("===================================================")
print(x.max())   # equivalent to np.max(x)
print("===================================================")
print(x.mean())  # equivalent to np.mean(x)
print("===================================================")
print(x.var())   # equivalent to np.var(x))
print("===================================================")
print(stats.describe(x))
'''
