def harshad_number(number1):
    i=11
    while i<=number1:
        n1=i
        remin=0
        sum=0
        while i>0:
            remin=i%10
            sum=sum+remin
            i=i//10
        if n1%sum==0:
            return(True,n1,"is harshad number")
        else:
            return(False,n1,"is not harshad number")
        i=i+1
number1=int(input("enter the number harshad number: "))
a=harshad_number(number1)
def perfect(Number):
    i=1
    Sum=0
    while(i < Number):
        if (Number%i==0):
            print(i)
            Sum=Sum+i
        i=i+1
    if (Sum==Number):
        return("number is a Perfect Number",Number)
    else:
        return("number is not the Perfect Number",Number)
Num=int(input("enter the number perfect number: "))
b=perfect(Num)
#print(a)
"""def palindrome(num):
    i=1
    a=""
    while i<=len(num):
        a=a+num[-i]
        i=i+1
    if a==num:
        return(num,"is palindrome")
    else:
        return(num,"is not palindrome")
    i=i+1
num=input("enter the palindrome string: ")
c=palindrome(num)"""
def main():
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else:
        print("sbhi equal")
main()