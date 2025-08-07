class Solution:
    def minDifference(self, arr):
        # code here
        def to_seconds(t):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s

        # Convert all times to seconds
        seconds = sorted(to_seconds(t) for t in arr)
        
        # Initialize min_diff to a large value
        min_diff = float('inf')
        n = len(seconds)

        # Compare adjacent times in sorted list
        for i in range(1, n):
            min_diff = min(min_diff, seconds[i] - seconds[i - 1])

        # Handle circular case: wrap-around from last to first
        circular_diff = (86400 + seconds[0] - seconds[-1]) % 86400
        min_diff = min(min_diff, circular_diff)

        return min_diff
        
