import random
def linear_search(arr, ser):
    """
    This function performs linear search by iterating over each element in the array
    and comparing it with the element to be searched
    """
    for ind in range(len(arr)):
        if arr[ind] == ser:
            print(ser, "found at index", ind)
            return
    print(ser, "not found in the list")      # Return -1 if not found


def binary_search(arr, ser, lb, ub):
    """
    This function performs binary search by eliminating atleast half of a given list
    in each iteration(Needs a sorted list).
    Requires 4 parameters: 1) arr - array, 2)ser - search element, 3) lb = lower bound (Pass 0 here)
                           4) ub - upper bound (pass (length of array-1))  
    """
    if lb > ub:          # This means the list is exhausted
        print(ser, " not found in the list")
        return -1
    mid = (lb+ub)//2
    if arr[mid]==ser:    # Element found, return index
        print(ser, " found at index", mid)
        return mid
    elif arr[mid] < ser: # Element is larger than mid, search upper half of list
        return binary_search(arr, ser, mid + 1, ub)
    else:                # Element is smaller than mid, search lower half of list
        return binary_search(arr, ser, lb, mid - 1)


def bubble_sort(arr):
    """
    This function performs bubble sort by pushing the largest element to
    the end of the list in each iteration.
    """
    terminate = True                    # Flag to terminate early in case list is sorted
    for i in range(len(arr)-1):
        terminate = True
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:       # if any element is smaller than the next then swap and update the terminate flag
                terminate = False      
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if terminate:                   # if no swaps, exit the loop as the list is already sorted
            break


def selection_sort(arr):
    """
    This function performs selection sort by pulling the smallest element to
    the back of the list in each iteration.
    """

    for i in range(len(arr)-1):
        min_index = i                                          # Chose initial minimum index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:                        # Update minimum index if a smaller element is found
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]        # Swap current element with minimum index

# Linear Search
a = [i for i in range(50)]
random.shuffle(a)
linear_search(a, 23)
linear_search(a, 52)

# Binary Search
a = [random.randint(1,1000) for i in range(50)]
ser1,ser2 = a[0], a[-1]
a.sort()
binary_search(a, ser1, 0, len(a)-1)
binary_search(a, ser2, 0, len(a)-1)
binary_search(a, 1001, 0, len(a)-1)

# Bubble sort
a = [random.randint(1,1000) for i in range(10)]
print("Original:", a)
bubble_sort(a)
print("Bubble Sorted:", a)

# Selection sort
a = [random.randint(1,1000) for i in range(10)]
print("Original:", a)
selection_sort(a)
print("Selection Sorted:", a)