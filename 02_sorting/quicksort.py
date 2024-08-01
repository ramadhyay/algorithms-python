# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:35:38 2023

@author: Dhananjay_E
"""

def quick_sort(a, start, end):

    if start-end == 0:
        return

    p = start
    lower = start

    for i in range(start+1, end):
        if a[i] <= a[p]:
            a[i], a[lower+1] = a[lower+1], a[i]
            lower += 1
        
    a[p], a[lower] = a[lower], a[p]
    p = lower

    quick_sort(a, start, p)
    quick_sort(a, p+1, end)


a = [1, 2, 3, 4, 5, 6]
a = [43, 32, 22, 78, 63, 57, 91, 13]
a = [10,9,8,7,6,5,4]



quick_sort(a, 0, len(a))
print(a)