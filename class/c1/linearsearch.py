n=int(input("enter the number of elements in a list: "))
l=[]
flag=False
for i in range(n):
    g=int(input("enter element :"))
    l.append(g)
c=int(input("enter a number to search :"))
for i in range(n):
    if l[i]==c:
        print("element found at position:",i+1)
        flag=True
if flag==False:
    print("Element not found")