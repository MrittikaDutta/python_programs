class Solution:
    def maxMinDiff(self, arr, k):
        # code here
        arr.sort()
        
        def canPlace(mid):
            count = 1
            last = arr[0]
            for i in range(1, len(arr)):
                if arr[i] - last >= mid:
                    count += 1
                    last = arr[i]
                    if count >= k:
                        return True
            return False
        
        low, high = 0, arr[-1] - arr[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlace(mid):
                ans = mid  # mid is possible, try larger
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
