#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:12:39 2019

@author: matthewsillence
"""
# Set the the filenames as variables for the script
F_IN = 'Emails_Summary.txt'
F_OUT = 'Emails_Relevant.txt'

# Open your 'Emails_Summary.txt' from the Python directory, then read the file, remembering the encoding and reading with the '\n' newline to make the results more legible  
with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
# Using the readlines() function, it returns a list containing each line in the file as a list item
    lines = f_in.readlines()
# Open your empty 'Emails_Relevant.txt' from the Python directory, then write to the file, remembering the encoding and reading with the '\n' newline to make the results more legible
with open(F_OUT, 'w', encoding='utf-8', newline='\n') as f_out:
# Create a for loop that iterates through each line in the list
    for line in lines:
# Create an if statement with the keyword of your choosing to extract just the lines containing that word
        if 'doctoral' in line:
# Print the lines that conform to the if statement above
            f_out.write(line + '\n')
# Now check the contents of your 'Emails_Relevant.txt' file, and you should find a list of the titles of articles and their URLs that were on the same line in the original messages
