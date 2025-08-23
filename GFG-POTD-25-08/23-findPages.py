class Solution:
    def findPages(self, arr, k):
        # code here
        if k > len(arr):
            return -1

        low = max(arr)
        high = sum(arr)
        result = -1

        def check(max_pages):
            students_needed = 1
            current_pages = 0
            for pages in arr:
                if current_pages + pages > max_pages:
                    students_needed += 1
                    current_pages = pages
                    if students_needed > k:
                        return False
                else:
                    current_pages += pages
            return True

        while low <= high:
            mid = low + (high - low)a // 2
            if check(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
