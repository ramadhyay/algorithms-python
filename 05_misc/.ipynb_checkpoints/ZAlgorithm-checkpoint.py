# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:19:09 2023

@author: Dhananjay_E
"""
text = "aaxxxxxxxxxxaaxxaaa"
pattern = "aa"


def naive(text, pattern):
    occurence = 0
    count =  0
    for i in range(0 , len(text)):
        count = 0
        for j in range(0, len(pattern)):
            if i+j < len(text) and pattern[j] == text[i+j]:
                count += 1
            else:
                break
                
        if count == len(pattern):
            occurence += 1
    
    return occurence

print(naive(text, pattern))