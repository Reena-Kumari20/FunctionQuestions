a="good"
b="odg"
i=1
c=""
while i<len(a):
    c=c+a[i]
    i=i+1
j=0
while j<len(b):
    if b[j] not in c:
        c=c+b[j]
    j=j+1
print(c)
