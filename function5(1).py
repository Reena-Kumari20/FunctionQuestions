def check_numbers_list(num1,num2):
    i=0
    j=0
    while i<len(num1):
        a=num1[i]+num2[j]
        print(a)
        if num1[i]%2==0 and num2[j]%2==0:
            print("dono even hai")
        else:
            print("dono even nhi hai")
        j=j+1
        i=i+1
check_numbers_list([2,6,18,10,3,75],[6,19,24,12,3,87])