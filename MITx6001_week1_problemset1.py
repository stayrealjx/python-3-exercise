#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:40:24 2018

@author: lijixuan
"""

'''Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5'''

numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1

print('numVowels is: ' + str(numVowels))

''' Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''

count = 0
for i in range(len(s) - 2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count += 1
print("Number of times bob occurs is: " + str(count))
