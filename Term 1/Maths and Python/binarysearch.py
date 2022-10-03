import random
a = [4, 13, 18, 21, 43, 53, 76, 85, 89, 99]
n = 13

lb,ub = 0,10
while(lb <= ub):
    mid = int((lb + ub)/2)
    if n == a[mid]:
        print(mid)
        break
    elif n > a[mid]:
        lb = mid+1
    else:
        ub = mid
        