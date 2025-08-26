class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        i = 0  # pointer for s1
        j = 0  # pointer for s2

        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1

        return i == len(s1)
