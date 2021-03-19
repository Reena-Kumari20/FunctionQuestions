# Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]

def even_in_list(list):
    i=0
    a=[]
    while i<len(list):
        if list[i]%2==0:
            a.append(list[i])
        i=i+1
    return a
list=[1,2,3,4,5,6,7,8,9,]
print(even_in_list(list))

