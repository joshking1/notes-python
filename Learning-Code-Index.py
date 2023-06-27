#!/usr/bin/python3

# This is the use of count method.
x = " i like to study python and I should be able to do well" 
print(x.count('STUDY'))
print(x.count("python"))

# Let us see the usage of the index 
print(x.index('I',28))  # you can start from index 29 skipping the rest. It will give an error
print(len(x))

# This introduce us to find method 

print(x.find('I'))

print(x.find('I',29))  # Find is better compared to index

# Practice: Display given string at left/right/center of a line in title format
given_type = input("Enter the name of your favorite animal: ")
print(given_type) # It is important to note that python is displaying the name elephant on the left hand side. 
# In windows I can get the number of columns using the mode
print(given_type.center(99))
print(given_type.ljust(99))
print(given_type.rjust(99))
