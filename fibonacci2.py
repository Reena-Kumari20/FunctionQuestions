def fib2(n): 
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)   
         a, b = b, a+b
     return result
n1=int(input("enter the number of limit: "))
f100=fib2(100)    
print(f100)                
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]