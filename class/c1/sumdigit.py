n=int(input("enter a number: "))
k=n
s=0
while k>0:
    s=s+k%10
    k=k//10
print("sum of digits :",s)