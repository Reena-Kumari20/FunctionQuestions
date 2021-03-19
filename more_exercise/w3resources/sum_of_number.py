#Write a Python function to sum all the numbers in a list. 
#Sample List : (8, 2, 3, 0, 7)
def sum(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    return(sum)
list=[8,2,3,0,7]
print(sum(list))
        