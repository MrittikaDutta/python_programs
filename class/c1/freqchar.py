s=input("enter a string:")
d={}
l=len(s)
for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
print(d)