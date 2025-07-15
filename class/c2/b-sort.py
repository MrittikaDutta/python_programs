n=int(input("enter the number of elements in a list: "))
l=[]
flag=False
for i in range(n):
    g=int(input("enter element :"))
    l.append(g)
for i in range(n-1):
    for j in range(0,n-1-i):
        if l[j]>l[j+1]:
            c=l[j]
            l[j]=l[j+1]
            l[j+1]=c
print(" bubble sorted list")
for i in range(n):
    print(l[i],end=" ")