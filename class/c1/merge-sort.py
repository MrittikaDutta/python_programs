def merge(arr,l,m,r):
    n1=m-1+1
    n2=r-m
    l=[0]*[n1]
    r=[0]*[n2]
    for i in range(0,n1):
        l[i]=arr[l+1]
    for j in range(0,n2):
        r[i]=arr[l+1]