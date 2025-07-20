class Solution:
    def countValid(self, n, arr):
        # code here
        arr_set = set(arr)
        forbidden_digits = set(str(d) for d in arr_set)
        
        from functools import lru_cache
        
        allowed_digits = [str(d) for d in range(10) if str(d) not in forbidden_digits]

        @lru_cache(maxsize=None)
        def dp(pos, tight, leading_zero):
            if pos == n:
                return 0 if leading_zero else 1  # valid number if it has started
            
            res = 0
            upper_limit = 9 if not tight else int(limit[pos])
            for d in range(0, upper_limit + 1):
                ch = str(d)
                if ch in forbidden_digits:
                    continue
                next_tight = tight and (d == upper_limit)
                next_leading_zero = leading_zero and d == 0
                # skip numbers that start with 0
                if next_leading_zero:
                    continue
                res += dp(pos + 1, next_tight, next_leading_zero)
            return res

        # Total number of n-digit numbers
        total = 9 * (10 ** (n - 1))

        # Build limit string for DP (just 999...n times)
        limit = '9' * n
        
        # Count invalid numbers (numbers without any digit from arr)
        invalid_count = dp(0, True, True)

        return total - invalid_count
