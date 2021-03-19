def positive_sum(arr):
    sum=0
    i=0
    while i<len(arr):
        if arr[i]>0:
            sum=sum+arr[i]
        i=i+1
    return(sum)
print(positive_sum([-1,2,3,4,-5]))