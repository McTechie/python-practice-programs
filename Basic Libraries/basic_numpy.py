"""
Numpy is the fundamental package to work with arrays in Python
and to perform scientific calculations
"""

import numpy as np

'''
# Create a 3x1 numpy array
a = np.array([1,2,3])

# Print object type - Numpy array
print(type(a))
print("===================================================")

# Print shape - tuple of integers giving the size along each dimension
print(a.shape)
print("===================================================")

# Print some values in a
print(a[0], a[1], a[2])
print("===================================================")

# Create a 2x2 numpy array
b = np.array([[1,2],[3,4]])

print(b.shape)
print("===================================================")

# Print values of b
print(b[0,0], b[0,1], b[1,0],b[1,1])
print("===================================================")
'''
'''
# 2x3 zero array
d = np.zeros((2,3))
print(d)
print("===================================================")

# 4x2 array of ones
e = np.ones((4,2))
print(e)
print("===================================================")

# 2x2 constant array - filled with 9
f = np.full((2,2), 9)
print(f)
print("===================================================")

# 3x3 random array
g = np.random.random((3,3))
print(g)
print("===================================================")
'''
'''
# Create 3x4 array
h = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(h)
print("===================================================")

# Slice array 'h' to make a 2x2 sub-array
i = h[:2, 1:3] # Take first 2 rows and columns 1-2
print(i)
print("===================================================")

# Modify the slice
i[0,0] = 1738

# Print to show how modifying the slice also changes the base object
print(i)
print(h)
print("===================================================")
'''
'''
# Integer type array
j = np.array([1, 2])
print(j.dtype)
print("===================================================")

# Float type array
k = np.array([1.0, 2.0])
print(k.dtype)
print("===================================================")

# Force Data Type on the array
# The float value is "floored" to the integer value
l = np.array([1.0, 2.0], dtype=np.int64)
print(l)
print(l.dtype)
print("===================================================")
'''
'''
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

# Elementwise sum
print(x + y)
print(np.add(x, y))
print("===================================================")

# Elementwise difference
print(x - y)
print(np.subtract(x, y))
print("===================================================")

# Elementwise product
print(x * y)
print(np.multiply(x, y))
print("===================================================")

# Elementwise division
print(x / y)
print(np.divide(x, y))
print("===================================================")

# Elementwise square root
print(np.sqrt(x))
print("===================================================")

# Sum of all elements
print(np.sum(x))
print("===================================================")

# Compute sum of each column - downwards sum
print(np.sum(x, axis=0))
print("===================================================")

# Compute sum of each row - sideways sum
print(np.sum(x, axis=1))
print("===================================================")

# Dot Product - Actual multiplication of matrices / vectors
print(np.dot(x,y))
print("===================================================")
'''
