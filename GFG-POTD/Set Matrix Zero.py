class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
     
        zero_rows = set()
        zero_cols = set()
    
        # Step 1: Find all rows and columns that need to be zeroed
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
    
        # Step 2: Set corresponding rows to 0
        for i in zero_rows:
            for j in range(m):
                mat[i][j] = 0
    
        # Step 3: Set corresponding columns to 0
        for j in zero_cols:
            for i in range(n):
                mat[i][j] = 0
    
        return mat
