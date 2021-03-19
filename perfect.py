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
Num=int(input("enter the number: "))
a=perfect(Num)
print(a)