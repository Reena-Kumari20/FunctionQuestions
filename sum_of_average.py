#Ek function banaiye jo 3 numbers ka sum aur average print kare.Hum 
#user se 3 number input karwayenge aur fir unn 3 numbers ka sum aur 
#average print karwayenge jaisa ki niche output diya hua hain.

def average_of_sum(a,b,c):
    sum=a+b+c
    average=sum/3
    print(sum)
    return("average of sum:",average)
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
print(average_of_sum(a,b,c))


