class Solution:
    def balanceSums(self, mat):
        # code here
        n = len(mat)
        rowSum = [0] * n
        colSum = [0] * n
        for i in range(n):
            for j in range(n):
                rowSum[i] += mat[i][j]
                colSum[j] += mat[i][j]

        target = max(max(rowSum), max(colSum))

        # We now try to bring each row and column up to the target
        res = 0
        i = j = 0
        while i < n and j < n:
            # Amount we can add to mat[i][j] without exceeding row/col target
            diff = min(target - rowSum[i], target - colSum[j])
            mat[i][j] += diff
            rowSum[i] += diff
            colSum[j] += diff
            res += diff

            if rowSum[i] == target:
                i += 1
            if colSum[j] == target:
                j += 1

        return res
