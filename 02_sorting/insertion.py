# -*- coding: utf-8 -*-

def insertion(a):
    for i in range(1, len(a)):
        nextpos = i
        while (nextpos > 0 and a[nextpos] < a[nextpos-1]):
            a[nextpos], a[nextpos-1] = a[nextpos-1], a[nextpos]
            nextpos = nextpos - 1

# function to insert an element i into an already sorted array
def insert(a, i):
    nextpos = i
    while (nextpos > 0 and a[nextpos] < a[nextpos-1]):
        a[nextpos], a[nextpos-1] = a[nextpos-1], a[nextpos]
        nextpos -= 1

def insertion_recur(a, i):
    if i >= len(a):
        return

    insert(a, i)
    insertion_recur(a, i+1)

a=[2, 3, 1, 0, 0, -1, -2, 1, 2, 33, 2, 1, 0, 0, 2, 23, 21001, 101]
print(a)
#insertion(a)
insertion_recur(a, 0)
print(a)