# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:41:13 2023

@author: Dhananjay_E
"""

# combining sorted lists
def merge(a, b):
    i, j = 0, 0
    c = []
    while (i < len(a) or j < len(b)):
        if (i < len(a) and j < len(b) and a[i] <= b[j]) or (i < len(a) and j == len(b)):
            c.append(a[i])
            i += 1

        if (i < len(a) and j < len(b) and a[i] > b[j]) or (j < len(b) and i == len(a)):
            c.append(b[j])
            j += 1
    return c            

def merge_sort(a, start, end):
    if end==start:
        return [a[start]]

    mid = (end+start)//2
    left = merge_sort(a, start, mid)
    right = merge_sort(a, mid+1, end)
    return merge(left, right)    

a=[1,2,3,4,5,6,7,8,9]    
b=[1,4,5]
merge(a, b)

c=[1,2,0,3,1,2,23,2,1,232,1,232,1,123,53,56,1,-1]
print(c)
c=merge_sort(c, 0, len(c)-1)
print(c)