def subseq(n,l):
    Best = [1] * n
    lee=len(l)
    for i in range(len(l)):
        for j in range(i):
            Best[i]+=1
    return max(Best)
            

n=int(input())
l=[]
r=[]
c=1

for i in range(n):
    a=int(input())
    l.append(a)
le=len(set(r))
print(subseq(n,l))