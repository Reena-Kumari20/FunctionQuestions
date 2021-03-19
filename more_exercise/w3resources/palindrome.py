#on function that checks whether a passed string is palindrome or not. 
#Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
#  e.g., madam or nurses run.

def palindrome(string):
    i=1
    a=""
    while i<=len(string):
        a=a+string[-i]
        i=i+1
    if a==string:
        return(string,"is palindrome")
    else:
        return(string,"is not palindrome")
    i=i+1
string=input("enter the string: ")
print(palindrome(string))
