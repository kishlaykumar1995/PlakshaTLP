import random
inp_array = [random.randint(1,100) for i in range(10)]

def bubble_sort(a):
    l = len(a)
    for i in range(l-1):
        for j in range(l-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

def kth_element(a,k):
    a = bubble_sort(a)
    return a[k]

print(kth_element(inp_array, 6))
print(inp_array)