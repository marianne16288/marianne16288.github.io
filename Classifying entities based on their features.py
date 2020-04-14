#!/usr/bin/env python
# coding: utf-8

# # 2. Classifying entities based on their features

# **Classification** is an important concept in machine learning, as it's something that computers are commonly trained to do. 
# 
# In this exercise, we're going to **classify** whether a person is a ballet dancer or a rugby player based on a set of **features** that describe them. A **feature** is a measurable property or characteristic of an entity. Here, the features are sex, age, weight, height, and the entity is a person. 
# 
# Next week, we will train a machine learning algorithm to do this for us.
# 
# As we go through the exercise, we explain what is happening in the code. Don't worry if you don't understand all of it - the main purpose is to give you an overview of how we can use Python to help us understand data.

# As a first step, let's take a look at the data. The table below shows a sample of people who are either ballet dancers or rugby players. Age, weight and height are represented as numbers. Notice that sex is represented as a number too, because it's easier for the algorithm to work with numbers than letters. Here, we represent **males** as 0 and **females** as 1.

# |Person ID|Sex (0/1)|Age |Weight (Kg)|Height (cm)|
# |------|---------|----|-----------|-----------|
# |     1|        1|  24|         63|        190|
# |     2|        1|  20|         55|        185|
# |     3|        0|  25|         75|        202|
# |     4|        1|  30|         50|        180|
# |     5|        0|  19|         57|        174|
# |     6|        0|  31|         85|        150|
# |     7|        1|  28|         93|        145|
# |     8|        0|  29|         75|        130|
# |     9|        0|  24|         99|        163|
# |    10|        0|  30|        100|        171|

# Before we can perform any analysis, we need to load the data into memory, so that the computer program can access it. To do this, we first `import` the *numpy* package. This provides access to existing Python code that we can use to help us manipulate the data. 

# In[3]:


import numpy as np

#This loads the file 'people.csv' into a variable called 'data' so we can work with it
#CSV files are 'comma separated value' files, which mean that columns are separated by commas, 
#and rows are separated by new line characters
data = np.genfromtxt("data/people.csv", delimiter=",", names=True)


# Now the data is loaded, we can start to explore it.
# 
# Let's print the column names:

# In[4]:


print(data.dtype.names)


# You can print out the data values contained in each of the columns. Run the cell below, then try changing the column name, and re-run it to see the different data.

# In[5]:


print(data["Weight"])


# We can draw a scatter plot of the data. We're using the *matplotlib* package to do this, so we'll `import` this first.

# In[6]:


import matplotlib.pyplot as plt


# Now we specify the data we want to use for the X and Y axes, and draw the plot.

# In[7]:


#Set Age values to be shown on the x axis
x_axis = "Age"

#Set Weight values to be shown on the y axis
y_axis = "Weight"

#Say what the axes represent
plt.scatter(data[x_axis], data[y_axis])

#Set the title
plt.title("Data distribution of %s against %s" % (x_axis, y_axis))

#Label the axes
plt.xlabel(x_axis)
plt.ylabel(y_axis)

#display the graph
plt.show()


# Why is it useful to do this *programmatically*, rather than manually (drawing the graph yourself)? How does it compare with a tool like Excel?

# Try plotting different columns of data against each other by changing the `x_axis` and `y_axis` variables above and rerunning the cell, and try to answer the following questions:
# 
# Which pair of columns gives us two distinct clusters?
# 
# Is "Sex" a useful differentiator for this data?

# In[ ]:




