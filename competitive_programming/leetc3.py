n=5
k=2
l=[i for i in range(1,n+1)]
i=1
c=1
print(l)
while len(l)>1:
    for i in l:
        #c+=1
        if c==k:
            l.remove(i)
            c=0
        c+=1
    print(l)
print(l)