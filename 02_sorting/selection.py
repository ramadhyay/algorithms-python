# -*- coding: utf-8 -*-
# Time complexity: O(n^2)

def selection(a):
    for i in range(len(a)):
        minpos=i
        for j in range(i, len(a)):
            if a[j] < a[minpos]:
                minpos = j
            a[i], a[minpos] = a[minpos], a[i]

def selection_recur(a, i, n):
    if i >= n:
        return
    else:
        minpos=i
        for j in range(i+1, n):
            if a[j] < a[minpos]:
                minpos = j
        a[i], a[minpos] = a[minpos], a[i]
 
        selection_recur(a, i+1, n)

# Slicing + Recursion is a double whammy of un desirability in python.
