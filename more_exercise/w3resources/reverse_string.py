#Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse_of_string(string):
    i=1
    a=" "
    while i<=len(string):
        a=a+string[-i]
        i=i+1
    return(a)
a=input("enter the string: ")
print(reverse_of_string(a))
