def maximin(l):
    le=len(l)
    m=l[0]
    mi=l[0]
    for i in range(le):
        if l[i]>m:
            m=l[i]
        elif l[i]<mi:
            mi=l[i]
    return mi,m
    
n=int(input("enter the number of elements in list:"))
l=[]
for i in range(n):
    s=int(input("enter a number :"))
    l.append(s)
print("The  minimum and maximum is:",maximin(l))
