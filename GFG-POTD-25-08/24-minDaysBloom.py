import math
class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        """
        Finds the minimum number of days to make exactly m bouquets,
        each requiring k adjacent bloomed flowers.

        Args:
            arr (list[int]): A list where arr[i] is the day the flower at position i will bloom.
            k (int): The number of adjacent flowers required for a single bouquet.
            m (int): The target number of bouquets.

        Returns:
            int: The minimum number of days, or -1 if it's not possible.
        """
        n = len(arr)
        # A quick check to see if we have enough flowers in total.
        # If the number of flowers needed is more than the total available,
        # it's impossible to make the bouquets.
        if m * k > n:
            return -1

        # The range for our binary search is the number of days.
        # The minimum possible day is the earliest bloom day, and the maximum is the latest.
        low = min(arr)
        high = max(arr)
        ans = -1

        def can_make_bouquets(days):
            """
            Helper function to check if we can make 'm' bouquets by a given day.
            We iterate through the flowers, counting adjacent bloomed flowers.
            When we find a group of 'k' adjacent bloomed flowers, we form a bouquet
            and reset the count.
            """
            bouquets_made = 0
            adjacent_flowers = 0
            for bloom_day in arr:
                if bloom_day <= days:
                    # This flower has bloomed. Increment the adjacent count.
                    adjacent_flowers += 1
                    if adjacent_flowers == k:
                        # We have enough adjacent flowers for a bouquet.
                        bouquets_made += 1
                        adjacent_flowers = 0
                else:
                    # The flower has not bloomed, breaking the adjacent streak.
                    adjacent_flowers = 0
            
            # Return true if we can make at least 'm' bouquets.
            return bouquets_made >= m

        # Perform binary search on the number of days.
        while low <= high:
            mid = (low + high) // 2
            if can_make_bouquets(mid):
                # If we can make the bouquets by 'mid' days, it's a potential answer.
                # We try to find an even smaller number of days.
                ans = mid
                high = mid - 1
            else:
                # If we can't make the bouquets by 'mid' days, we need more time.
                # Shift the search range to the right.
                low = mid + 1
        
        return ans
