def fibonacci(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
#calling function
n1=int(input("enter the number of limit: "))
fibonacci(n1)