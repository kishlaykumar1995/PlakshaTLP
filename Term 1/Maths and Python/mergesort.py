def merge(a, b):
    out = []
    i=j=0
    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i+=1
        else:
            out.append(b[j])
            j+=1
    
    out.extend(a[i:])
    out.extend(b[j:])
    return out

def mergesort(arr, l, r):
    if l<r:
        a = mergesort(arr, l, (l+r)//2)
        b = mergesort(arr, (l+r)//2, r)
        return merge(a, b)
    elif l>=r:
        return arr[l]

import random
a = list(range(5))
random.shuffle(a)
mergesort(a, 0, len(a)-1)
