import pdb
n = float(input("Enter N:"))
da = int(input("Enter decimal accuracy:"))

k = -1
sqt = 0.0
temp =0.0
for i in range(int(n/2)):
    if i**2 <= n and (i+1)**2 > n:
        sqt = i


temp=sqt
while k>=-da:
    for j in range(9):
        c = 10**k * j
        temp = sqt + c
        #print(c, temp, temp**2, (temp+(10**k))**2, temp**2 <= n and (temp+(10**k))**2 > n)
        if temp**2 <= n and (temp+(10**k))**2 > n:
            break
    sqt = temp
    k-=1
print(str(sqt)[:da+2])