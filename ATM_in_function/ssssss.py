def without_split(a):
    b=[]
    c=" "
    i=0
    while i<len(a):
        if a[i]=="":
            b.append(c)
            c=" "
        else:
            c=c+a[i]
        i=i+1
    if c:
        b.append(c)
    return(b)
a=("my name is reena")
print(without_split(a))
