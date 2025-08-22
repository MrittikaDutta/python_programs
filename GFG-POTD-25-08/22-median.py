import bisect

class Solution:
    def median(self, mat):
    	# code here 
    	n = len(mat)
        m = len(mat[0])
        
        # The number of elements we want to find that are less than or equal to the median.
        # For an odd number of elements, the median is at index (n*m)//2 (0-indexed).
        # We are looking for a value with (n*m)//2 elements smaller than or equal to it.
        desired = (n * m) // 2
        
        # Binary search on the range of possible values
        low = 1
        high = 2000
        
        while low <= high:
            mid = (low + high) // 2
            
            count = 0
            for i in range(n):
                # Using bisect_right to count elements less than or equal to mid
                # in a row-wise sorted list.
                count += bisect.bisect_right(mat[i], mid)
            
            if count <= desired:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
