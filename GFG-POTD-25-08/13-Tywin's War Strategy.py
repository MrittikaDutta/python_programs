import math
class Solution:
    def minSoldiers(self, arr, k):
        # code here
        n = len(arr)
        required_lucky_troops = math.ceil(n / 2)
        
        costs = []
        for soldiers in arr:
            if soldiers % k == 0:
                costs.append(0)
            else:
                cost_to_add = k - (soldiers % k)
                costs.append(cost_to_add)
        
        costs.sort()
        
        t = sum(costs[:required_lucky_troops])
        return t
