#Ek function likhiye jo ki ek limit naam ka parameter lega aur 0 se limit tak ke beech ke 
#number jo ki 3 aur 5 ke multiples hain unka sum print karega.jaisa ki niche dikhaya gya hai. 
#Input:- 3 aur 5 ke multiples => 3, 5, 6, 9, 10

def add_of_multiple(limit):
    i=0
    sum=0
    while i<=n1:
        if i%3==0 or i%5==0:
            sum=sum+i
            print("3 or 5 ke multiple:",i)
        i=i+1
    print(sum)
n1=int(input("enter the limit: "))
add_of_multiple(n1)
