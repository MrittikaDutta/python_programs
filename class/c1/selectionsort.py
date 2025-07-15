

n=int(input("enter the number of elements in a list: "))
l=[]
flag=False
for i in range(n):
    g=int(input("enter element :"))
    l.append(g)
for i in range(n):
    min=i
    for j in range(i,n):
        if l[min]>l[j]:
            min=j
    (l[i],l[min])=(l[min],l[i])
print("sorted list")
for i in range(n):
    print(l[i],end=" ")