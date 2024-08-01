# -*- coding: utf-8 -*-
# Shortest path using DAG
import functools 

G = {'S': [['A', 10], ['C', 2]],
     'A': [['B', 6]],
     'B': [['E', 2], ['D', 1]],
     'C': [['D', 3], ['A', 4]],
     'D': [['E', 1]],
     'E': []}

def topological_sort(G):
    indegree = {}
    queue = []
    path = []

    for v in G:
        indegree[v] = 0

    for u in G:
        for v in G[u]:
            indegree[v[0]] += 1

    for v in G:
        if indegree[v] == 0:
            queue.append(v)

    while queue:
        u = queue.pop(0)
        path.append(u)

        for v in G[u]:
            indegree[v[0]] -= 1

            if indegree[v[0]] == 0:
                queue.append(v[0])

    return path


def shortest_path(G, tp, s):
    distance = {}
    skip_flag = True
    parents = {}

    max_distance = 0

    for u in tp:
        for v in G[u]:
            max_distance = max_distance + v[1]
            
    for u in tp:
        distance[u] = max_distance + 1

    for u in tp:
        if skip_flag and u == s:
            distance[u] = 0
            skip_flag = False

        if skip_flag:
            continue

        for v in G[u]:
            if distance[v[0]] > distance[u] + v[1]:
                distance[v[0]] = distance[u] + v[1]
                parents[v[0]] = u
    
    return parents
    

s = 'S'
d = 'D'

tp = topological_sort(G)
parents = shortest_path(G, tp, 'S')
 
path = []

while d in parents:
    path.append(d)
    d = parents[d]
    if s == d:
        path.append(s)

print(functools.reduce(lambda x, y: x+'->'+y, path[::-1]))