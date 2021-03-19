#Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono lists ke
#  elements hone chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare 
# elements sirf ek-ek baar hi hone chaiye. Agar humare paas yeh do lists hain:

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
#Toh humari nayi list yeh hogi:

#new_list = [1, 2, 5, 10, 12, 13, 16, 20] 
#Yahan dekho ki dono lists ke items ek ek baar aa rahe hain. 
#* Jaise dono lists mein 1 aa raha tha, lekin nayi list mein ek hi baar aa raha hai.

#Aise hi 10 aur 16 bhi dono list mein aa raha tha, lekin nayi list mein ek hi baar hai
#Aur 5, 2, 12, 13 aur 20 mein se kuch pehli list mein the aur kuch dusri mein, lekin
#Sabhi numbers nayi list mein ek hi baar aayenge.
def number(list1,list2):
    i=0
    a=[]
    while i<len(list1):
        if list1[i] not in a:
            a.append(list1[i])
        i=i+1
    i=0
    while i<len(list2):
        if list2[i] not in a:
            a.append(list2[i])
        i=i+1
    a.sort()
    return(a)
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
print(number(list1,list2))
