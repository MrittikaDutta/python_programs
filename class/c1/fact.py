n=int(input("enter the value of n"))
l=[0,1]
for i in range(2,n):
    l.append(l[i-1]+l[i-2])
for i in range(n):
    print(l[i])
