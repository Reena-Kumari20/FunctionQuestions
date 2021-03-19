def without_split(string):
    a=[]
	b=" "
	i=0
	while i<len(string):
	    if string[i]==" ":
	        a.append(b)
	        b=" "
	    else:
	        b=b+string[i]
	    i=i+1
	if b:
	    a.append(b)
	return a
string=("my name is reena sara sarmishtha anzum bharti")
print(without_split(string))

