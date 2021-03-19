print('welcome to our ATM')
print('Insert the card')
Balance=10000
language='English'
def language_choice(language):
language=input("plese choose any one languge: English or Hindi;- ")
if language=='Hindi':
    print('Hindi language is not available')
elif language=='English':
    pin=int(input("please inter your pin number: "))
    # pin=1234
    if pin==1234:
        print('your pin code is correct')
        option=input("choose option any one:- CASH WITHDRWAl or BALANCE INQUERY; ")
        if option=='CASH WITHDRWAL':
            print('SAVING,CURRENT,CREDIT')
            option=input('choose any withdrwal option; ')
            if option=='CURRENT'or 'CREDIT':
                transaction=int(input("enter how many amount you want: "))
                if transaction<Balance:
                    print('Your transaction is being processed,')
                    print('Please wait')
                elif transaction>Balance:
                    print('in your account no extra transaction')
                else:
                    print("your transaction is being processed,")
                    print('Please wait')
            elif option=='SAVING':
                print(Balnce)
            else:
                print('no available')
        elif option=='BALANCE INQUERY':
            print('In your account have Balance',Balance)
        else:
            print("nothing")
    else:
        print('pin is wrong')
else:
    print('other language is also not avaible')