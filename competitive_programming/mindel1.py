def minimumNumberOfDeletions(s):
        # code here 
        l=len(s)
        l1=[]
        s2=s[l-1:l//2:-1]
        s1=s[0:l//2+1]
        h=""
        n=l-1
        for i in range(len(s1)):
            while n>0:
                  if s[n]==s1[i]:
                        h=s[n]+h+s1[i]
                        break
                  else:
                        n=n-1
        k=len(h)
        print(s1)
        print(s2)
        return h
print(minimumNumberOfDeletions("geeksforgeeks"))