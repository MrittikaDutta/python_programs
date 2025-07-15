s=input("enter a string  ")
l=""
for i in range(len(s)):
    l=s[i]+l
if l==s:
    print("palindrome")
else:
    print("not a palindrome")