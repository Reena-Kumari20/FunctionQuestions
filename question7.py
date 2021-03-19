#Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski 
#length jyaada hogi use print karega aur agar dono strings ki length equal hui to dono ko
#line by line print karega . Hint :- use len() builtin function.

def find_of_length(a,b):
    x=len(a)
    y=len(b)
    if x<y:
        print(y,"high length of b",b)
    elif y<x:
        print(x,"high length of a",a)
    else:
        print(a,b)
str1=input("enter the string1: ")
str2=input("enter the string2: ")
find_of_length(str1,str2)