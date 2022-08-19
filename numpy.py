#!/usr/bin/env python
# coding: utf-8

# # NumPy 
# numpy is used for working with arrays.

# In[1]:


#NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
#The array object in NumPy is called ndarray


# # np.array

# In[3]:


import numpy as np

# np.array : creat a array
# ndim : dimension of array
#3-D arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr.ndim) 


# In[10]:


# creat 5 dimension of array
arr = np.array([1, 2, 3, 4], ndmin=5)


# In[13]:


#access 2 D array

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1]) 

# negative index
print('Last element from 2nd dim: ', arr[1, -1]) 


# In[11]:


#access 3 D array

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


# In[15]:


# numpy array slicing : [start:end:step]
print(arr[0:3:2])


# In[21]:


#Slice elements from index 4 to the end of the array:
arr = [5,6,7,8,9,4,3,2]
print(arr[4:])


# In[22]:


#Slice elements from the beginning to index 4 (not included)
print(arr[:4])


# In[29]:


print(arr[-4:-1])


# In[30]:


#Return every other element from the entire array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])


# In[31]:


#slicing 2 D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) 


# # np.shape 
# The shape of an array is the number of elements in each dimension.

# In[34]:


arr = np.array([[1, 2, 3, 4], [5, 6, 7,5]])
print(arr.shape)


# # np.reshape

# In[35]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr) 


# # Iterating Arrays
# Iterating means going through elements one by one.

# In[41]:


#Iterate on the elements of the following 1-D array
arr = np.array([1,2,3])
for i in arr:
    print(i)


# In[38]:


arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)


# In[39]:


arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y) 


# # np.nditer
# iterating Arrays Using nditer()

# In[43]:


for x in np.nditer(arr):
    print(x)


# # np.concatenate
# joining array

# In[45]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)


# In[50]:


arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

arr3 = np.concatenate((arr1, arr2))
arr4 = np.concatenate((arr1, arr2), axis = 1)

print(arr3)
print(arr4)


# # np.array_split
# splitting numpy array

# In[52]:


arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)
print(newarr)


# # np.where
# searching arrays
# You can search an array for a certain value, and return the indexes that get a match

# In[58]:


arr = np.array([1,2,5,7,9,4])
x = np.where (arr == 4)
print(x)

#indexes where the values are even
print( np.where (arr%2 == 0))


# # np.sort

# In[59]:


arr = np.array([[11,2],[8,7]])
print(np.sort(arr))


# # filter
# In NumPy, you filter an array using a boolean index list

# In[63]:


arr = np.array([5,8,7,9])
x = [True, True, False, False]

print(arr[x])


# In[64]:


# common use is to create a filter array based on conditions.

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr) 


# # np.add/ np.subtract

# In[82]:


a = np.array([11,2,5])
b = np.array([8,7,6])

print("sum of 2 arrays:", np.add(a,b))

print("subtract of 2 arrays:", np.subtract(a,b))


# In[ ]:




