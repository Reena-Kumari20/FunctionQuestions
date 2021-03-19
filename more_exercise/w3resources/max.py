#1. Write a Python function to find the Max of three numbers.
def max_of_three(x,y,z):
    if x>y and x>z:
        return(x,"max number")
    elif y>x and y>z:
        return(y,"max number")
    elif z>x and z>y:
        return(z,"max number")
a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
print(max_of_three(a,b,c))