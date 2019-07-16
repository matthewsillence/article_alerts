#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:12:39 2019

@author: matthewsillence
"""

F_IN = 'Emails_Summary.txt'
F_OUT = 'Emails_Relevant.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    lines = f_in.readlines()

with open(F_OUT, 'w', encoding='utf-8', newline='\n') as f_out:
    for line in lines:
        if 'doctoral' in line:
            f_out.write(line + '\n')
