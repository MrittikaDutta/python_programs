class Solution:
    def maxOnes(self, arr, k):
        # code here
        n = len(arr)
        left = 0
        zero_count = 0
        max_length = 0

        # The right pointer of the sliding window
        for right in range(n):
            # If the current element is 0, increment the zero_count
            if arr[right] == 0:
                zero_count += 1
            
            # If the number of zeros exceeds k, shrink the window from the left
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                # Move the left pointer to the right
                left += 1

            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length
