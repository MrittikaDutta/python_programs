import math
from itertools import combinations_with_replacement

class Solution:
    def lcm(self, a, b):
        return a * b // math.gcd(a, b)

    def lcmTriplets(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6

        max_lcm = 0
        # Try combinations from top 10 numbers only
        candidates = list(range(max(1, n - 10), n + 1))

        for a, b, c in combinations_with_replacement(candidates, 3):
            current_lcm = self.lcm(self.lcm(a, b), c)
            max_lcm = max(max_lcm, current_lcm)

        return max_lcm
