class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        if n == 0:
            return -1

        i = 0
        j = n - 1

        # Step 1: Find a potential celebrity candidate
        while i < j:
            if mat[i][j] == 1:
                # i knows j, so i cannot be the celebrity. Eliminate i.
                i += 1
            else:
                # i does not know j, so j cannot be the celebrity. Eliminate j.
                j -= 1
        
        candidate = i
        
        # Step 2: Validate the candidate
        for k in range(n):
            if k == candidate:
                continue
            
            # Check if the candidate knows anyone
            # A celebrity does not know anyone
            if mat[candidate][k] == 1:
                return -1
            
            # Check if everyone knows the candidate
            # A celebrity is known by everyone
            if mat[k][candidate] == 0:
                return -1
                
        return candidate
