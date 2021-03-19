#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
def multi(list):
    i=0
    multi=1
    while i<len(list):
        multi=multi*list[i]
        i=i+1
    return(multi)
list=[8,2,3,-1,7]
print(multi(list))
        