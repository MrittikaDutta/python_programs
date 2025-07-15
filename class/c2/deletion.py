s=input("enter a string:")
c=input("enter char to delete:")
l=""
for i in s:
    if i==c:
        l=l+""
    else:
        l=l+i
print(l)