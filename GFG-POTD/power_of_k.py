from collections import Counter
import math
class Solution:
	def maxKPower(self, n, k):
	    
	    def prime_factors(k):
            pf = Counter()
            d = 2
            while d * d <= k:
                while k % d == 0:
                    pf[d] += 1
                    k //= d
                d += 1
            if k > 1:
                pf[k] += 1
            return pf
        
        def power_in_factorial(n, p):
            power = 0
            div = p
            while div <= n:
                power += n // div
                div *= p
            return power
        	    
	    
	    
		# code here
		factors = prime_factors(k)
        min_x = float('inf')
        
        for p, e in factors.items():
            total_power = power_in_factorial(n, p)
            min_x = min(min_x, total_power // e)
        
        return min_x
    
