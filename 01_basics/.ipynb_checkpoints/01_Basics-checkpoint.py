# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:05:52 2023

@author: Dhananjay_E
"""

def maxval(a):
    val = a[0]
    for i in a:
        if i > val:
            val = i
    return val