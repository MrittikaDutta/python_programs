def maximum(l):
    le=len(l)
    m=l[0]
    for i in range(le):
        if l[i]>m:
            m=l[i]
    return m
def minimum(l):
    le=len(l)
    mi=l[0]
    for i in range(le):
        if l[i]<mi:
            mi=l[i]
    return mi
n=int(input("enter the number of elements in list:"))
l=[]
for i in range(n):
    s=int(input("enter a number :"))
    l.append(s)
print("The maximum is:",maximum(l))
print("The minimum is:",minimum(l))
