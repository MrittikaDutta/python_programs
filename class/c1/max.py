n=int(input("enter the number of elements : "))
a=[]
for i in range(n):
    k=int(input("enter a number: "))
    a.append(k)
max=a[0]
for i in range(n):
    if a[i]>max:
        max=a[i]
print("the maximum is: ",max)