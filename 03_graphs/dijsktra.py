# -*- coding: utf-8 -*-

from queue import PriorityQueue

G = {1: [[10, 2], [80, 3]],
     2: [[10, 1], [6, 3], [20, 5]],
     3: [[80, 1], [6, 2], [70, 4]],
     4: [[70, 3]],
     5: [[20, 2], [50, 6], [10, 7]],
     6: [[50, 5], [5, 7]],
     7: [[10, 5], [5, 6]]}

maxcost = 0
burnt = []
burnt_time = {}
queue = PriorityQueue()

for u in G:
    for v in G[u]:
        maxcost += maxcost + v[0]

for u in G:
    burnt_time[u] = maxcost

def dijstra(G, s):
    burnt_time[s] = 0
    queue.put([0, s])

    while not queue.empty():
        u = queue.get()[1] # Minimum
        if u in burnt:
            continue

        burnt.append(u)
        for v in G[u]:
            if burnt_time[v[1]] > burnt_time[u] + v[0]:
                burnt_time[v[1]] = burnt_time[u] + v[0]
                queue.put([burnt_time[v[1]], v[1]])

dijstra(G, 1)        