class Solution:
    def maxRectSum(self, mat):
        # code here
        if not mat or not mat[0]:
            return 0
    
        n, m = len(mat), len(mat[0])
        max_sum = float('-inf')
    
        for left in range(m):
            temp = [0] * n
    
            for right in range(left, m):
                # Add values for columns from left to right to temp
                for i in range(n):
                    temp[i] += mat[i][right]
    
                # Apply Kadane's algorithm on temp
                current_max = temp[0]
                max_ending_here = temp[0]
                for i in range(1, n):
                    max_ending_here = max(temp[i], max_ending_here + temp[i])
                    current_max = max(current_max, max_ending_here)
    
                max_sum = max(max_sum, current_max)
    
        return max_sum
