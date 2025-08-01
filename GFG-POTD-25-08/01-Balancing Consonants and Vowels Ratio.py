class Solution:
    def countBalanced(self, arr):
        # code here
        def count_vc(s):
            vowels = set('aeiou')
            v = sum(1 for ch in s if ch in vowels)
            c = len(s) - v
            return v, c

        from collections import defaultdict

        prefix_diff = 0
        result = 0
        diff_count = defaultdict(int)
        diff_count[0] = 1  # base case: diff = 0 before anything

        for s in arr:
            v, c = count_vc(s)
            prefix_diff += (v - c)
            result += diff_count[prefix_diff]
            diff_count[prefix_diff] += 1

        return result
        
