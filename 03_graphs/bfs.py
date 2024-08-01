# -*- coding: utf-8 -*-

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


queue = []
visited = []
queue.append(2)
visited.append(2)

while queue:
    u = queue.pop(0)
    for v in G[u]:
        if not v in visited:
            visited.append(v)
            queue.append(v)

visited=[]
def bfs(G, u):
    for v in G[u]:
        
        visited.append[u]