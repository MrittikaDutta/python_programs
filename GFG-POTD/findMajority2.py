from collections import Counter
class Solution:
    def findMajority(self, arr):
        # code here
        l=[]
        n=len(arr)//3
        d=Counter(arr)
        a=sorted(list(set(arr)))
        for i in a:
            if d[i]>n:
                l.append(i)
        return l
