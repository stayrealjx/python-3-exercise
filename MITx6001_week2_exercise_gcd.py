#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:19:00 2018

@author: lijixuan
"""

"""Exercise: gcd iter"""

## The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder.
## Method 1 using iteration

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    k = min(a, b)
    while k > 0:
        if a % k == 0 and b % k == 0:
            return k
        else:
            k -= 1

## Method 2 using recursion

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)