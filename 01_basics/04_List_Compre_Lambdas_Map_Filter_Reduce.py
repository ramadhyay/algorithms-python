# -*- coding: utf-8 -*-

import numpy as np

l1 = [i for i in range(0, 10)]
print(l1)


print((lambda x: x**2)(2))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

full_name('guido', 'van rossum')

add = lambda x, y: x+y

for i in map(np.sqrt, l1):
    print(i, end=", ")


for j in filter((lambda x: x>2), l1):
    print(j)    

lambda1 = (lambda x, y: x+y)

inputs = input()
print([eval(i) for i in inputs.split()])

for i in inputs.split():
    print(i)
    
l2=list(map(eval, inputs.split()))
l2    
