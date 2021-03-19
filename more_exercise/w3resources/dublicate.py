#Write a Python function that takes a list and returns a new list with unique elements of 
# the first list. Go to the editor
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def dublicate(list):
    i=0
    a=[]
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
        i=i+1
    return a
list=[1,2,3,3,3,3,4,5]
print(dublicate(list))