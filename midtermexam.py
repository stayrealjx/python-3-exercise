#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:34:33 2018

@author: lijixuan
"""

# =============================================================================
# Problem 3
# 
# Write a simple procedure, myLog(x, b), that computes the logarithm of a number x relative to a base b. For example, if x = 16 and b = 2, then the result is 4 - because 2^4=16. If x = 15 and b = 3, then the result is 2 - because 3^2 is the largest power of 3 less than 15.
# 
# In other words, myLog should return the largest power of b such that b to that power is still less than or equal to x.
# 
# x and b are both positive integers; b is an integer greater than or equal to 2. Your function should return an integer answer.
# =============================================================================

def myLog(x, b):
    n = 2
    result = 0
    if x > b:
        while result <= x:
            result = b**n
            n += 1
        return n - 2
    else:
        return 0

# =============================================================================
# Problem 4
# 
# Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.
# 
# assume L is not empty
# assume 0 < n <= len(L)
# This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.
# 
# Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]
# 
# Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]
# =============================================================================

def getSublists(L, n):
    list = []
    for i in range(0, (len(L)-n+1)):
        list.append(L[i:i+n])
    return list

# =============================================================================
# Problem 5
# 
# Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)
# =============================================================================

def uniqueValues(aDict):
    '''
    Create a set called nondups to hold all the non-duplicate values
    Store the key in the list nondups, For each key and value, if that value only appears once, 
    '''
    result = [k for k,v in aDict.items() if list(aDict.values()).count(v)==1]
    # don't forget to sort the list
    result.sort()
    # returns the sorted list 
    return result

# =============================================================================
# Problem 6
# 
# Write a recursive procedure, called laceStringsRecur(s1, s2), which also laces together two strings. Your procedure should not use any explicit loop mechanism, such as a for or while loop. We have provided a template of the code; your job is to insert a single line of code in each of the indicated places.
# 
# For this problem, you must add exactly one line of code in each of the three places where we specify to write a line of code. If you add more lines, your code will not count as correct.
# =============================================================================

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #PLACE A LINE OF CODE HERE
            return s2
        if s2 == '':
            #PLACE A LINE OF CODE HERE
            return s1
        else:
            #PLACE A LINE OF CODE HERE
            return s1[0] + s2[0] + laceStringsRecur(s1[1:],s2[1:])
    return helpLaceStrings(s1, s2, '')

# =============================================================================
# Problem 7
# 
# def applyF_filterG(L, f, g):
#     """
#     Assumes L is a list of integers
#     Assume functions f and g are defined for you. 
#     f takes in an integer, applies a function, returns another integer 
#     g takes in an integer, applies a Boolean function, 
#         returns either True or False
#     Mutates L such that, for each element i originally in L, L contains  
#         i if g(f(i)) returns True, and no other elements
#     Returns the largest element in the mutated L or -1 if the list is empty
#     """
#     # Your code here
# =============================================================================

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    l = []
    if len(L) > 0:
        for i in L:
            if (g(f(i)) == True):
                l.append(i)
        L[:] = l
        if len(L) > 0:
            return max(L)
        else:
            return -1
    else:
        L[:] = l
        return -1