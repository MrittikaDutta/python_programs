def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n

n=int(input("enter n :"))
print(fact(n))