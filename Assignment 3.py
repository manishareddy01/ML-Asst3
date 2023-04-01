#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

# Create random vector of size 15 having integers in the range 1-20
vec = np.random.randint(1, 21, size=15)

# Reshape the vector to a 3 by 5 array
arr = vec.reshape(3, 5)

# Print array shape
print("Array shape:", arr.shape)

# Replace the max in each row by 0
arr[np.arange(len(arr)), arr.argmax(axis=1)] = 0

# Print the modified array
print("Modified array:\n", arr)

# Create a 2-dimensional array of size 4 x 3 with 4-byte integer elements
arr_2d = np.zeros((4, 3), dtype=np.int32)

# Print the shape, type and data type of the array
print("Array shape:", arr_2d.shape)
print("Array type:", type(arr_2d))
print("Array data type:", arr_2d.dtype)


# In[9]:


import numpy as np

# Define the square array
A = np.array([[3, -2],
              [1, 0]])

# Compute the eigenvalues and right eigenvectors
eigenvals, eigenvects = np.linalg.eig(A)

# Print the eigenvalues and right eigenvectors
print("Eigenvalues:", eigenvals)
print("Right eigenvectors:\n", eigenvects)


# In[10]:


import numpy as np

# Define the array
arr = np.array([[0, 1, 2],
                [3, 4, 5]])

# Compute the sum of the diagonal elements
diag_sum = np.trace(arr)

# Print the sum of the diagonal elements
print("Sum of the diagonal elements:", diag_sum)


# In[11]:


import numpy as np

# Define the array
arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])

# Reshape the array to a new shape without changing its data
new_shape = arr.reshape(2, 3)

# Print the original array and the new shapes
print("Original array:\n", arr)
print("Reshaped to 2x3:\n", new_shape)


# In[12]:


import matplotlib.pyplot as plt

# Define the programming languages and their popularity
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Set the figure size
plt.figure(figsize=(8, 5))

# Plot the pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%')

# Set the title
plt.title("Popularity of Programming Languages")

# Display the chart
plt.show()


# In[ ]:




