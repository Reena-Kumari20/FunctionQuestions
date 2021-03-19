#Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list banne 
# jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. 
# Socho aapki do list yeh hain:

#list1 = [1, 342, 75, 23, 98]
#list2 = [75, 23, 98, 12, 78, 10, 1] 
#Inn dono list se aapki nayi list yeh banni chaiye:

 #new_list = [1, 23, 75, 98] 

def dublicate(list1,list2):
    i=0
    while i<len(list1):
        j=0
        c=[]
        while j<len(list2):
            if list1[i] in list2[j]:
                c.append(list1[i])
            j=j+1
        i=i+1
    print(c)
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
dublicate(list1,list2)


