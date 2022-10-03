def left_right(L):
    left = []
    right =[]
    
    for i in range(1, len(L)):
        if L[i] <= L[0]:
            left.append(L[i])
        else:
            right.append(L[i])
    return left,L[0],right

def quicksort(L):
    if len(L) == 0:
        return L
    left,p,right = left_right(L)
    if len(L) > 1:
        return quicksort(left) + [p] + quicksort(right)
    else:
        return L


import time
import random

for k in range(1000):
    L = list(range(10**3))
    random.shuffle(L)
    t1 = time.time()
    S = quicksort(L)
    t2 = time.time()
    print(k*10**3, t2-t1)