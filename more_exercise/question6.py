#string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
#Aapke code ko iss string_list se ek nayi list banani chaiye jo yeh hogi:

#new_list = ["Rishabh", "Abhishek", "Divyashish"] 
def string_list(list1):
    i=0
    a=[]
    while i<len(list1):
        if list1[i] not in a:
            a.append(list1[i])
        i=i+1
    return(a)
list1=["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
print(string_list(list1))

#string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai'] 
#Isse aapke code ko yeh nayi list banani hogi:

 #new_list = ["Delhi", "Mumbai", "Chennai"] 

def string_list(list2):
    i=0
    b=[]
    while i<len(list2):
        if list2[i] not in b:
            b.append(list2[i])
        i=i+1
    return(b)
list2=["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
print(string_list(list2))

#string_list=["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
def string_list(list3):
    i=0
    c=[]
    while i<len(list3):
        if list3[i] not in c:
            c.append(list3[i])
        i=i+1
    return(c)
list3=["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
print(string_list(list3))