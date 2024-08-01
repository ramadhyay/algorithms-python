#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:06:13 2023

@author: ram
"""
G = {
   1 : [2, 3, 4],
   2 : [1, 3],
   3 : [2, 1],
   4 : [1, 5, 8],
   5 : [4, 6, 7],
   6 : [5, 7, 8, 9],
   7 : [5, 6, 9],
   8 : [4, 6, 9],
   9 : [6, 8, 10],
   10 : []
  }

visited = []
pre={}
post={}
counter=0
def dfs(G, v):
    global counter

    print(v, '-> ', end='')
    
    pre[v] = counter
    counter += 1

    visited.append(v)
    for u in G:
        if u not in visited:
            dfs(G, u)

    post[v] = counter
    counter += 1

dfs(G, 4)