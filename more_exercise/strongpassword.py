#Yahan pehli command True print karegi. Kyunki True or False boolean hote hain, 
# hum inko if statement mein use kar sakte hain. agar hum iska data type dekhenge 
# toh woh bhi "bool" dikhayega Aapko agli kuch exercises mein iski zaroorat padegi ;-)
#  Hum online account banate wakt bahot jagah password set karte hain. Jaise aapne
#  slack aur gmail ka account banate hue bhi apne passwords set kare honge. Humare 
# accounts ke passwords secret hote hain jo kisi ko pata nahi lagna chaiye. Yeh jitne
#  complex honge kisi aur ke liye guess karna utna mushkil ho jayega. Jaise'rahulverma'
#  ko guess karna aasan hai, lekin 'rahul$%verma12!' ko guess karna mushkil hai. Iss vajah
#  se aap jab bhi online account banaoge toh ek acha sakht password set karna important 
# hota hai. Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki 
# humara password strong hai. * Pehle user se ek password ka string input lijiye.

#Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:
#Kam se kam uski length 6 honi chaiye
#Jada se jada length 16 se jyada na ho
#Kam se kam ek dollar ka sign ($) hona chaiye
#Kam se kam password mein 2 ya 8 hona chaiye
#Password mein capital A ya capital Z hona chaiye
#Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, nahi toh "Weak Password" type karo

password=input("enter the valid password: ")
if len(password)>=6 and len(password)<=16:
    if "a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z":
            if "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
                if "@" in password or "$" in password or "#" in password:
                    print("strong password")
                else:
                    print("weak password")
            else:
                print("please enter in any digit")
    else:
            print("plase enter any alphabet")
else:
    print("invalid pssword,you password length should be more than 6")