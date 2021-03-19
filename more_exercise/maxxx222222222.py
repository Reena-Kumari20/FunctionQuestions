"""def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return("The number is palindrome!")
    else:
        return("Not a palindrome!")
num=int(input("Enter a palindrome number:"))
a=palindrome(num)"""

# Python Program to find Perfect Number using While loop

def perfect(Number):
    i = 1
    Sum = 0
    while(i < Number):
        if(Number % i == 0):
            Sum = Sum + i
        i = i + 1
    if (Sum == Number):
        return(Number,"is a Perfect Number",Number)
    else:
        return(Number,"is not the Perfect Number",Number)
Number = int(input(" Please Enter any perfect Number: "))
b=perfect(Number)

def harshad_number(num1):
    rem = 0
    sum = 0      
    n = num1 
    while(num1 > 0):    
        rem = num1%10   
        sum = sum + rem    
        num1 = num1//10      
    if(n%sum == 0):    
        return(n, " is a harshad number")    
    else:    
        return(n ," is not a harshad number")
num1=int(input("enter the harshad number"))   
c=harshad_number(num1)

def maximum():
    if b>c:
        print(b,"this number is maximum number")
    elif c>b:
        print(c,"this is maximum")
    else:
        print("sbhi equal hai")
maximum()