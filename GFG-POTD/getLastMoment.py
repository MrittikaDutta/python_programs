class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        last_left  = max(left) if left else 0
        # Time for right‑moving ants to fall is (n - start).
        last_right = max((n - x) for x in right) if right else 0
        return max(last_left, last_right)
