#Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list banne 
# jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. 
# Socho aapki do list yeh hain:

#list1 = [1, 342, 75, 23, 98]
#list2 = [75, 23, 98, 12, 78, 10, 1] 
#Inn dono list se aapki nayi list yeh banni chaiye:

 #new_list = [1, 23, 75, 98] 
#Iss nayi list mein sirf 1, 75 aur 98 isliye hain kyunki aur koi bhi items dono lists mein nahi aa rahi. Dusri saari items ya toh pehli list mein aa rahi hai ya dusri mein. Note: Aapka yeh code kitne bhi items ki list pe kaam karna chaiye. Aur dono lists ki length alag bhi ho sakti hai.

def new_list(list1,list2):
    i=0
    a=list1+list2
    b=[]
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        i=i+1
    return(b)
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
print(new_list(list1,list2))
