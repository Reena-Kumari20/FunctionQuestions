#input ka use kar ke 3 alag variables mein 3 integers ka input lein. 
#Input lene ke baad inn 3 mein se sabse bade number ko print karo Note: 
#Isme aap loops ka use nahi kar sakte.

def number(a,b,c):
    if a>b and a>c:
        return(a)
    elif b>a and b>c:
        return(b)
    elif c>b and c>a:
        return(c)
    else:
        return("sb equal")
a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
print(number(a,b,c))