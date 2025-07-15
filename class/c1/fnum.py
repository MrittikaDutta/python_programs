
l=[]
d={}
n = int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
    elem = int(input())
    l.append(elem)
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)