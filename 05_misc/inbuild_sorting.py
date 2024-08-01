#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:57:21 2023

@author: ram
"""
from queue import PriorityQueue
pq = PriorityQueue()
pq.put([10, 2])
pq.put([11, 3])
pq.put([12, 3])
pq.put([3, 3])
pq.put([5, 2])

for i, v in enumerate(pq.queue):
    print(i, v)