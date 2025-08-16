
import functools
class Solution:

	def findLargest(self, arr):
	    # code here
	    str_arr = [str(x) for x in arr]
        def compare(a, b):
            if b + a > a + b:
                return 1
            elif b + a < a + b:
                return -1
            else:
                return 0

        str_arr.sort(key=functools.cmp_to_key(compare))
        
        # Handle the case where all numbers are zeros
        if str_arr[0] == '0':
            return '0'
        return "".join(str_arr)
