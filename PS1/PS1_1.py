# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:03:04 2021

@author: Administrator
"""
import random 

# Generating three random ints: a, b, c that are between 0 and 100
a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)

# Generating a function Print_values that sorts a, b, c from largest to smallest
def Print_values(a,b,c):
    if a > b: # a > b
        if b > c: #b > c
            print(a,b,c)
        else: # b <= c
            if a > c: # a > c
                print(a,c,b)
            else: # a <= c
                print(c,a,b)
    else: #a <= b
        if b > c: # b > c
            if a > c: # a > c
                print(b,a,c)
            else: # a <= c
                print(b,c,a)
        else: # b < c
            print(c,b,a)

# Used Print_values for randomly generated a, b, c
Print_values(a,b,c)