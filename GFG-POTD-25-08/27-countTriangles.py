class Solution:
    def countTriangles(self, arr):
        # code here
        n = len(arr)
        if n < 3:
            return 0
        
        # Sort the array
        arr.sort()
        
        count = 0
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    # A valid triangle is formed. Since arr is sorted,.
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
                    
        return count
