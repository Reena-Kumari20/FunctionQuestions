#ss program mein hum students ki ginti aur ek student ke kharche se hisaab se
#pure NavGurukul ka ek mahine ka kharcha nikalenge input ka use kar ke do 
# values ka input lo: * Number of students

#Ek student ka kharcha
#Iss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya 
# usse kam hai toh print karein "Hum budget ke andar hain" nahi toh print karo ki hum
#  budget ke bahar hain. Note: Inn exercises mein aapko variables ke naam apne aap
#  soch kar likhne hain
def budget(a,b):
    amount=a*b
    if amount<=50000:
        return("Hum budget ke ander hai")
    else:
        return("Hum budget ke bahar hai")
Number_of_students=int(input("enter the students number: "))
pay=int(input("ek student ka kharcha: "))
print(budget(Number_of_students,pay))
    

