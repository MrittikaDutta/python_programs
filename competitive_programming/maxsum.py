def maxSumIS(self, Arr, n):
        dp = Arr.copy()
        for i in range(1, n):
            for j in range(i):
                if Arr[i] > Arr[j] and dp[i] < dp[j] + Arr[i]:
                    dp[i] = dp[j] + Arr[i]
        return max(dp)