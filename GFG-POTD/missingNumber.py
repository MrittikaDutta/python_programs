class Solution:
    def missingNumber(self, arr):
        # code here
        n=len(arr)
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        
        for i in range(n):
            if arr[i] != i+1:
                return i+1
        return n+1
