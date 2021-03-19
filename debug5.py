def distance(kms):
        if kms<20:
            print("close")
        elif kms<50:
            print("median")
        else:
            Print("far")
x=int(input("enter the kms: "))
distance(x) 