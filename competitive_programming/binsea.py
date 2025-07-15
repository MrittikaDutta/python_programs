class Solution:	
    def binarysearch(self, arr, n, k):
     mid=n//2
     l=0
     r=n
     while l<=r:
        mid=l+(r-1)//2
        if(arr[mid]==k):
             return mid+1
        elif arr[mid]<k:
             l=mid+1
        else:
            r=mid-1
        return (k,"is not present.")