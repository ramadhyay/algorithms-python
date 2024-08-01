# -*- coding: utf-8 -*-
# s is sum and coins is the minimum number of coins

# coins = [1, 4, 5]

memo={}

def min_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def min_coins(coins, s):
    if s in memo:
        return memo[s]
    
    if s==0:
        return 0
    
    answer = None
    
    for value in coins:
        if value > s:
            continue
        
        answer = min_none(answer, min_coins(coins, s - value) + 1)
    
    memo[s] = answer
    return answer