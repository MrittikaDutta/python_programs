class Solution:
    def searchMatrix(self, mat, x):
        # code here
        n = len(mat)
        if n == 0:
            return False
        m = len(mat[0])
        if m == 0:
            return False

        # Treat the matrix as a flattened, rotated, sorted array.
        low = 0
        high = n * m - 1

        while low <= high:
            mid = low + (high - low) // 2
            
            # Map the 1D mid index to 2D coordinates
            row = mid // m
            col = mid % m
            
            mid_val = mat[row][col]

            if mid_val == x:
                return True
            
            # This part handles the rotated nature of the array
            # Determine which half is sorted
            # The start of the flattened array is mat[0][0]
            start_val = mat[0][0]

            if start_val <= mid_val:  # Left half is sorted
                if start_val <= x < mid_val:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # Right half is sorted
                # The last element of the flattened array is mat[n-1][m-1]
                end_val = mat[n - 1][m - 1]
                if mid_val < x <= end_val:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
