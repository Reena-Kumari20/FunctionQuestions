def calculate(number_x,operation,number_y):
    if operation=="add":
        a=number_x+number_y
    elif operation=="subtract":
        a=number_x-number_y    
    elif operation=="multiply":
        a=number_x*number_y
    elif operation=="division":
        a=number_x/numbery
    else:
        "nothing"
    return a
x=int(input("enter the number: "))
y=int(input("enter the number: "))
user=input("enter the operation: ")
print(calculate(x,user,y))