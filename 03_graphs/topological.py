#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:17:11 2023

@author: ram
"""
G = {
    1: [3, 4, 5],
    2: [3, 8],
    3: [6],
    4: [6, 8],
    5: [8],
    6: [7],
    7: [8],
    8: []
}

queue = []
indegree = {}
path = {}
for u in G:
    indegree[u] = 0
    path[u] = 0


for u in G:
    for v in G[u]:
        indegree[v] += 1

for u in G:
    if indegree[u] == 0:
        queue.append(u)

while queue:
    u = queue.pop(0)
    print(u, '->', end='')
    for v in G[u]:
        indegree[v] -= 1
        path[v] = max(1 + path[u], path[v])
        if indegree[v] == 0:
            queue.append(v)
