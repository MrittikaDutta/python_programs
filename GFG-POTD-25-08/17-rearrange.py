class Solution:
    def rearrange(self, arr, x):
        # code here
        
        arr.sort(key=lambda e: abs(e - x))
        return arr
