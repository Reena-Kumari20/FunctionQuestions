"""def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)"""

def range(num):
    i=0
    while i<=stop_number:
        if num>0 and num<stop_number:
            return(num,"is in the range")
        else:
            return(num,"is outside the given range")
stop_number=int(input("enter the stop number: "))
num=int(input("enter the number: "))
print(range(num))
