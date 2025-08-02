class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        n = len(arr)
        # Convert array to +1 and -1
        nums = [1 if x > k else -1 for x in arr]
    
        prefix_sum = 0
        max_len = 0
        index_map = {}  # stores first occurrence of prefix_sum
    
        for i in range(n):
            prefix_sum += nums[i]
    
            if prefix_sum > 0:
                max_len = i + 1
            if prefix_sum not in index_map:
                index_map[prefix_sum] = i
    
            # If prefix_sum - 1 is seen before, we can try to get a subarray with positive sum
            if (prefix_sum - 1) in index_map:
                max_len = max(max_len, i - index_map[prefix_sum - 1])
    
        return max_len
