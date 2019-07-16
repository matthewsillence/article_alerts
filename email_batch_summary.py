# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:55:30 2019

@author: t026345
"""
# Open your 'Emails_Summary.txt' from the Python directory, then read the file, remembering the encoding and reading with the '\n' newline to make the results more legible  
with open('Emails_Summary.txt', 'r', encoding='utf-8', newline='\n') as f_in:
# Using the readlines() function, it returns a list containing each line in the file as a list item
    lines = f_in.readlines()
# Create a for loop that iterates through each line in the list
    for line in lines:
# Create an if statement with the keyword of your choosing to extract just the lines containing that word
        if 'doctoral' in line:
# Print the lines that conform to the if statement above
            print(line)
            
