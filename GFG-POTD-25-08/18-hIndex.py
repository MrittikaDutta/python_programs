class Solution:
    def hIndex(self, citations):
        #code here
        n=len(citations)
        citations.sort(reverse=True)
        h = 0
        for i in range(n):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        return h
