class Solution:
    def subarraySum(self, arr):
        # code here 
        total = 0
        n = len(arr)
        for i in range(n):
            total += arr[i] * (i + 1) * (n - i)
        return total
