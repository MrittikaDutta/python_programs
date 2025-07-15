def toh(n,s,d,a):
    if n==1:
        print("move",s,"to",d)
        return
    toh(n-1,s,a,d)
    print("MOVE DISC",a,"from ",s,"to",d)
    toh(n-1,a,d,s)


n=int(input("ENTER N:"))
toh(n,'a','b','c')