n = int(input("Enter no of lines:"))
incl = float(input("Enter incl:"))
incl = int(incl*10)
for i in range(n):
    print(" "*i*incl, end="*\n")
    