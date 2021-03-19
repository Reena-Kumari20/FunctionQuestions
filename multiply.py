def list_change(a,b):
    i=0
    c=0
    d=[]
    while i<len(a):
        c=a[i]*b[i]
        d.append(c)
        i=i+1
    print(d)
    return d
list_change([5, 10, 50, 20], [2, 20, 3, 5])

