'''
import random
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

a = [5,3,2,7,9,14,11,6,8]
print(quickselect_median([5,3,2,7,9,14,11,6,8]))
a.sort()
print(a)
'''

def partition(arr,l,r):
    i=l;j=l;pvt=r;
    while(j<=r):
        if arr[j] < arr[pvt]:
            arr[j],arr[i] = arr[i],arr[j]
            i+=1
        j+=1
    arr[i],arr[pvt] = arr[pvt],arr[i]
    return i

def find_median(a,l,r,k):
    pvt = partition(a,l,r)
    if pvt == k:
        return a[k]
    elif pvt < k:
        l = pvt+1
        return find_median(a,l,r,k)
    else:
        r = pvt-1
        return find_median(a,l,r,k)

#a = [18,5,3,2,7,9,14,11,6,8,23]
a = [5,7,92,46,27,33,19,12]
if len(a)%2 != 0:
    print(find_median(a,0,len(a)-1, int((len(a)-1)/2)))
else:
    j = (find_median(a,0,len(a)-1, int((len(a)-1)/2)) + find_median(a,0,len(a)-1, int(len(a)/2)))/2
    print(j)
a.sort()
print(a)