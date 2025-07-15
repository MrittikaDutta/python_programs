s=input("enter a string:")
l=""
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        l=l+chr(ord(i)-32)
    elif ord(i)>= 65 and ord(i)<=90:
        l=l+chr(ord(i)+32)
print(l)
