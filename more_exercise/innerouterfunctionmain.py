def add(a,b):
    x=a+b
    return x
def sub(a,b):
    x=a-b
    return x
def multi(a,b):
    x=a*b
    return x
def division(a,b):
    x=a/b
    return x
    
a=int(input("enter the number:"))
b=int(input("enter the number:"))
operator=input("enter the number: ")
def main():
    if operator=="+":
        print(add(a,b))
    elif operator=="-":
        print(sub(a,b))
    elif operator=="*":
        print(multi(a,b))
    elif operator=="/":
        print(division(a,b))
main()