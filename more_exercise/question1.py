#1 se 1000 tak saare numbers print karne ka loop likho. Lekin * Agar number 3 se 
#divisible hai toh "nav" print karvao.

#Agar number 7 se divisible hai toh "gurukul" print karvao.
#Agar number 21 se divisible hai toh "navgurukul" print karvao.

def question(num):
    i=1
    while i<=num:
        if i%3==0 and i%7==0 and i%21==0:
            print("number is divisible by 3,7 and 21",i)
        if i%3==0:
            print("nav",i)
        if i%7==0:
            print("gurukul",i)
        if i%21==0:
            print("navgurukul",i)
        else:
            print("nothing",i)
        i=i+1
n1=int(input("enter the number: "))
print(question(n1))