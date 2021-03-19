num=[2,3,6,7,24,5]
sum=0
i=0
while i<len(num):
    if num[i]%i==0:
        sum=sum+i
    i=i+1
if sum==num[i]:
    print("perfect no")
else:
    print("not perfect")