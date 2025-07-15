#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code h(ere
        k=[i for i in range(1,n+1)]
        d={}
        a=list(set(k).difference(set(arr)))
        for i in arr:
            if i in d:
                b=i
                break
            else:
                d[i]=1
        return(b,a[0])   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends