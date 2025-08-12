class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        prices.sort()
        n = len(prices)
        minCost = 0
        i = 0
        rem= n
        while i < rem:
            minCost += prices[i]
            i += 1
            rem-= k

        maxCost = 0
        i = n - 1
        index = -1
        while i > index:
            maxCost += prices[i]
            i -= 1
            index += k

        return [minCost, maxCost]
