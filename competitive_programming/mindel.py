def minimumNumberOfDeletions(s):
        # code here 
        l=len(s)
        s2=s[l-1:l//2:-1]
        s1=s[0:l//2+1]
        h=""
        for i in range(l//2):
            for j in s[l-1:l//2:-1]:
                if s[i]==j:
                    h=h+j
                    break
        k=len(h)
        print(s1)
        print(s2)
        return h
print(minimumNumberOfDeletions("aebcbda"))