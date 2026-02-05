def power(x, n):
    if n == 1:
        return x
    elif n % 2 == 2:
        y = power(x, n/2)
        return y * y 
    else:
        return x * power(x, n-1)

def modular_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent & 1)  == 1:
           result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def mod_power_rec(A, B, C):
     
    # Base Cases
    if (A == 0):
        return 0
    if (B == 0):
        return 1
     
    # If B is Even
    y = 0
    if (B % 2 == 0):
        y = mod_power_rec(A, B / 2, C)
        y = (y * y) % C
     
    # If B is Odd
    else:
        y = A % C
        y = (y * mod_power_rec(A, B - 1, C) % C) % C
    return ((y + C) % C)
 
