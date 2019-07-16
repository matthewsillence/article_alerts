# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:55:30 2019

@author: t026345
"""


with open('Emails_Summary.txt', 'r', encoding='utf-8', newline='\n') as f_in:
    lines = f_in.readlines()
    for line in lines:
        if 'doctoral' in line:
            print(line)
            
