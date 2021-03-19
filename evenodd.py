#Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka 
#parameter lega aur 0 se limit tak ke beech ke sabhi even aur odd numbers ko 
#label ke saath print karega jaisa ki niche dikhaya gaya hai.
def showNumbers(limit):
    i=0
    while i<=n1:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
n1=int(input("enter the limit: "))
showNumbers(n1)