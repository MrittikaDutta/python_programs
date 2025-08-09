class Solution:
    def getLongestPrefix(self, s):
        # code here
        n  = len(s)
        Z = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l, r = i, i + Z[i] - 1

        # Try from largest to smallest proper prefix
        for length in range(n - 1, 0, -1):
            # Check if repeating s[:length] covers s
            if Z[length] >= n - length:
                return length
        return -1
        
