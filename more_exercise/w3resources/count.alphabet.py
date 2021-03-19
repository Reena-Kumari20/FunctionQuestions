#7.Write a Python function that accepts a string and calculate the number of upper case
#letters and lower case letters. Go to the editor
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

def count(string):
    i=0
    upper_case=0
    lower_case=0
    while i<len(string):
        # For upper letters 
        if (ord(string[i]) >= 65 and ord(string[i]) <= 90): 
            upper_case=upper_case+1
          
        # For lower letters 
        elif (ord(string[i]) >= 97 and ord(string[i]) <= 122): 
            lower_case=lower_case+1
        else:
            pass
        i=i+1
    return("No. of upper case character",upper_case +"\n"+ "No. of lower case character",lower_case)
string=input("enter the string: ")
print(count(string))