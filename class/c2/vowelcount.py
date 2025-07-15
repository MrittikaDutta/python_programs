s=input("enter a string:")
v=0
k=0
c=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o'or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        v=v+1
    elif ord(i)>=97 and ord(i)<=122:
        c=c+1
    elif ord(i)>= 65 and ord(i)<=90:
        c=c+1
    else:
        k=k+1
print("NUMBER OF VOWELS:",v)
print("NUMBER OF consonents:",c)
print("NUMBER OF SPECIAL CHARACTER:",k)