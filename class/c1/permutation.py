def permutation(n,r):
    def fact(n):
        if n==0 or n==1:
            return 1
        else:
            return fact(n-1)*n
    return fact(n)/fact(n-r)

def combination(n,r):
    def fact(n):
        if n==0 or n==1:
            return 1
        else:
            return fact(n-1)*n
    return fact(n)/(fact(n-r)*fact(r))

n=int(input("enter n:"))
r=int(input("enter r:"))
print(int(permutation(n,r)))
print(int(combination(n,r)))
