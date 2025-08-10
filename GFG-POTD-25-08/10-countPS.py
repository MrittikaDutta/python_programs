class Solution:
    def countPS(self, s):
        # code here
        n = len(s)
        count = 0
        def expand(left: int, right: int):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= 2:
                    count += 1
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return count
