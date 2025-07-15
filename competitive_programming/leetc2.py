s="dart"
n=len(s)
k=3
for i in range(n-k):
            # c=s[i]
            # s[i]=s[i+k]
            # s[i+k]=c
    s.replace(s[i],s[i+k])
print(s)