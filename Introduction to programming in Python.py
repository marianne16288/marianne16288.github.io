#!/usr/bin/env python
# coding: utf-8

# ## 1. Introduction to Programming using a Jupyter Notebook
# 
# ### 1.1. What is a programming language?
# 
# A programming language allows us to give a series of instructions to a computer in a way that it understands.
# 
# In this short introductory exercise, we will use the Python programming language, which is widely used in science and technology applications.
# 
# The exercise is provided in a *Jupyter notebook*. The notebook runs in a web browser, and allows you to create and run small pieces of code, and see the results. Notebooks are commonly used in teaching, and provide a supportive environment for introducing people to the basics of programming.
# 
# As part of this lab, you will be working with two types of cells: Markdown cells, which contain text, and code cells, which allow you to perform operations (such as adding or subtracting) on data.

# ### 1.2. Markdown cells
# 
# These cells enable you to add, modify, or remove text. This is a Markdown cell. If you click on it, it will be highlighted in blue.
# 
# Try modifying the Markdown cell below to greet yourself. To do that, double-click the cell below (it will then be highlighted in green), replace X with your name, and press the "▶| Run" button in the menu at the top (or **shift** + **enter**).
# 

# Hello, Marianne!

# ### 1.3 Code cells
# 
# Now that you've written a greeting using Markdown, let's try to *execute* (run) a code cell. The program below uses the Python programming language to tell the computer to show a greeting on the screen. 
# 
# Execute the program by clicking on the cell to activate it (it will be highlighted with green), press "▶| Run" or **shift** + **enter**. Notice how "Hello, World!" is printed on the screen underneath the code cell. This is the *result* of the computation we've just performed. 

# In[3]:


print ("Hello, World!")


# The text we used to say 'Hello World' above is fixed, or *static*. This means we can't change it after we've written the program, and every time the program is run it will stay the same. This might be ok for printing a greeting message, but it doesn't work very well for most computer programs, where we want to be able to make changes to the information (or perform *operations* on it - explained below) in the program while it is running.
# 
# To store information inside computer programs we use *variables*. In the cell below, we are using two variables, `greeting` to store the first word, and `my_name` to store the second. 
# 
# Try executing the code as it is, and then change the value of the variables to make the program execute a different greeting (e.g. Good morning, Sarah!).

# In[4]:


# Assign value to variables
greeting = "Hello"
my_name = "World"

print ("good morning, Marianne!")


# You may have noticed the code contains some additional explanatory information, known as a *comment*. You can add a comment by preceding text with a `#`. Anything written after a `#` will have no effect on the program, but is useful for helping the programmer to understand the code either they, or someone else, has written. It is good practice to write clear comments when programming. You should also always read comments, as they will help you to understand what the code is doing.

# ### 1.3 Performing operations inside a program 

# If we want our program to have real value, we need it to actually do something, or perform *operations*. An example of an operation is adding two values together (e.g. `13 + 9`). An *operand* is an item of data to be manipulated (i.e. 13, 9) and an *operator* is the construct used to do the manipulation (i.e. `+`).

# You can find out more about the many different types of operators here: [https://www.tutorialspoint.com/python/python_basic_operators.htm](https://www.tutorialspoint.com/python/python_basic_operators.htm). 

# Let's try using variables and operators within our code. We'll start by *assigning* some initial values to the variables we are going to use. To do this in Python, we use the `=` sign. This sets the value of the variable on the left to whatever is on the right.

# To set the values of the two variables we have defined above, we need to excecute the cell; so do that now.
# 
# Now let's work out the combined ages of the animals by executing the cell below, and printing the result.

# In[1]:


combined_ages = 8+ 10

print(combined_ages)


# We can use variables for *reasoning* about data. In the example below we use the *conditional statements* `if` and `else` to display information about which animal is older. Execute the cell below to find out which animal is older.

# In[ ]:



    age_elephant=1
    age_tiger=10
    if int(age of elephant)>int(age_tiger):
        print("the elephaant is older than the tiger")
        else:
            print("the tiget is older than the elephant")
        
    print("The elephant and the tiger are the same age")


# To finish off the exercise, try the following:
# 
# 1. Change the ages, to check that the program works. You need to execute the cells again to re-run each bit of code with the new values.
# 2. Add comments, explaining what is happening on each line.
# 3. As well as displaying which animal is older, see if you can say by how much (optional).

# In[ ]:





# In[ ]:





# In[ ]:




