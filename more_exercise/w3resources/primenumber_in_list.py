#at takes a number as a parameter and check the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no 
# positive divisors other than 1 and itself.

def prime_or_not(number):
    i=1
    count=0
    while i<=number:
        if number%i==0:
            count=count+1
        i=i+1
    if count==2:
        return("prime number",number)
    else:
        return(number,"is not prime number")
number=int(input("enter the number: "))
print(prime_or_not(number))