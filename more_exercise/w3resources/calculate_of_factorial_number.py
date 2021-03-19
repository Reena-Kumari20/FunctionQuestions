#Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.
"""def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))"""

def factorial(n):
    i=1
    factorial=1
    while i<=n:
        factorial=factorial*i
        i=i+1
    return(factorial)
n=int(input("enter the number: "))
print(factorial(n))

