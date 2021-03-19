#a = ['Mary', 'had', 'a', 'little', 'lamb']
#for i in range(len(a)):
 #   print(i, a[i])

a=["mary","had","a","little","lamb"]
i=0
while i<len(a):
    print(i,a[i],len(a[i]))
    i=i+1

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            break
        else:
            print(n,'is a prime number')

#
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
            

def initlog(*args):
   pass   # Remember to implement this!