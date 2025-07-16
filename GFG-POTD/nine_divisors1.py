class Solution:
    def countNumbers(self, n):
        # code here
        l=[]
        for i in range(n+1):
            d=2
            for j in range(2,i//2+1):
                if i%j==0:
                    d+=1
            if d==9:
                l.append(d)
        return len(l)
        
