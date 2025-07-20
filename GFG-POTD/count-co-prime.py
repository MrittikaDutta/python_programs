# not optimized
from math import gcd

class Solution:
    def cntCoprime(self, arr):
        n = len(arr)
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if gcd(arr[i], arr[j]) == 1:
                    count += 1
                    
        return count
sol = Solution()
print(sol.cntCoprime([1, 2, 3]))      # Output: 3
print(sol.cntCoprime([4, 8, 3, 9]))   # Output: 4
