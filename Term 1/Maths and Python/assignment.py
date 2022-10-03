def ques1():
    """
    This function takes an input N prints the following:
    N = 1 (1 star with one row)
    N = 2 (2 rows: Row 1 - 1 star, Row 2 - 2 stars)
    and so on
    """
    n = int(input("Enter N:"))
    for i in range(n):
        print("*"*(i+1))                 # Print stars

def ques2():
    """
    This function takes an input N prints the following:
    N = 1 (1 star with one row)
    N = 2 (2 rows: Row 1 - 1 star(from the right), Row 2 - 2 stars(from the right))
    and so on
    """
    n = int(input("Enter N:"))
    for i in range(n):
        print(" "*(n-i-1), "*"*(i+1))     # Print spaces and stars

def ques3():
    """
    This function takes an input N prints the following:
    N = 4
           *
         * * *
       * * * * *
     * * * * * * *
    """
    n = int(input("Enter N:"))
    for i in range(n+1):
        print(" "*2*(n-i),end="")        # Print spaces
        for j in range(i*2-1):
            print('*', end=" ")          # Print stars
        print()                          # Print newline

def ques4():
    """
    This function takes an inputs i and j prints a list containing the numbers between i and j(inclusive).
    """
    i = int(input("Enter i:"))
    j = int(input("Enter j:"))
    if i > j:
        print("Error!! i must be less than j")
        return
    l = [x for x in range(i,j+1)] # generate a list b/w i and j using list comprehension
    print(l)

def ques5():
    """
    This function takes an inputs i an j and prints all prime nos between i and j in a list.
    """
    i = int(input("Enter i:"))
    j = int(input("Enter j:"))
    # Numbers must be positive and i must be greater than j
    if i > j:
        print("Error!! i must be less than j")
        return
    elif i < 0:
        print("Error!! Numbers must be greater than 0")
        return
    
    if i < 2:
        i=2
    
    prime = lambda x:True if sum([1 if x%z==0 else 0 for z in range(2,int(x))])==0 else False # Lambda function which returns True if prime and False if not prime
    l = [x for x in range(i,j+1) if prime(x)]
    print("Prime Nos:", l)

#ques1()
#ques2()
#ques3()
#ques4()
ques5()

