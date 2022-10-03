n = int(input("Enter number of lines:"))
c = float(input("Enter curvature:"))

lb = int(-n/2)
ub = int(n/2-1 if n%2==0 else (n-1)/2)
print(lb,ub)

if c>0:
    for i in range(lb,ub+1):
        x = int(i*i*c)
        print(" "*x, end="")
        print("*")
else:
    d = int(abs(c)*n/2*n/2)
    for i in range(lb,ub+1):
        x = int(i*i*abs(c))
        print(" "*(d-x), end="")
        print("*")
