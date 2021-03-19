Balance=50000
#this function for inter your pin code number:....
def pin_code():
    print("Please insert your card")
    i=1
    while i<=3:
        #print("please insert your card\n")
        pin=input("enter the pin code:  ")
        if pin=="1234":
            print("your pin code is correct\n")
            print("Please wait\n")
            print("Thank You")
            break
        else:
            print("wrong pin code,you have only",3-i,"chance")
        
        i=i+1
        
#this function for transaction and about for saving account:.....
def option2():
        print("choose any withdrawl option:\n  ")
        #1.saving
        #2.current or credit
        option2=input("enter the withdrawl option:\n ")
        if option2=="2":
            trans_action()
            pin_code()
        elif option2=="1":
            print("SAVING")
            print(Balance)
#this function for choose option for prossess...        
def option1():
    option1=input("enter the any option:  ")
    if option1=="1":
        print("CASH WITHDRWAL")
        print("1.SAVING\n2.CURRENT or CREDIT\n")
        option2()
    elif option1=="2":
        print("BALANCE INQUERY")
        print("In your account have balance: ",Balance)
#this function for your transaction......       
def trans_action():
    #Balance=50000
    transaction=int(input("enter the amount\nHow many ammount you want: "))
    if transaction<Balance:
        print("your transaction is being processed\n")
        #print("Please wait\n")
        #print("Thank You")
    elif transaction>Balance:
        print("In your account no extra transaction")
    else:
        print("your transaction in being processed")

# this is main function for calling another function.....
def A_T_M():
    #Balance=500000
    print("WELCOME TO ATM\n")
    print("you have to chose lanhguage:\n1.English\n2.Hindi\n")
    language=input("enter the language:  ")
    if language=="1":
        print("chose any option \n1.CASH WITHDRWAl\n2.BAlANCE INQUERY\n")
        option1()
        #pin_code()
    else:
        print("you have only english language")
A_T_M()
