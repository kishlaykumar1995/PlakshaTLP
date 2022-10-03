def binary_exponent(a,b):
    """
    This function performs binary exponentiation iteratively
    """
    a_pow=a                  # This variable stores the power of 'a' in a particular iteration

    #1st iteration - Here the power of a is 1
    if b%2==1:
        result = a
    else:
        result = 1
    b = b//2

    while b>0:
        rem = b%2
        b = b//2
        a_pow = a_pow*a_pow  # Power of a increases in powers of 2 in every iteration
        if rem==1:           # if remainder is 1, then multiply the result with current iteration of a_pow 
            result = result*a_pow


    return result
print(binary_exponent(6,12))