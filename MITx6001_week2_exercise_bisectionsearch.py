#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 12:14:47 2018

@author: lijixuan
"""

import math    
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == "":
        return False
    
    if len(aStr) == 1:
        return char == aStr
        
    midindex = math.ceil(len(aStr)/2)
    midchar = aStr[midindex]
    if char == midchar:
        return True     
    elif char < midchar:
        return isIn(char, aStr[:midindex])
    else:
        return isIn(char, aStr[midindex+1:])