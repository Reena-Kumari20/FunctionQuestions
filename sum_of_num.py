def add(number):
    i=1
    sum=0
    while i<=number:
        sum=sum+i
        i=i+1
        return sum
n1=int(input("enter the num: "))
print(add(n1))