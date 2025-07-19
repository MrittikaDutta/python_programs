from math import factorial
from collections import Counter
class Solution:
    def vowelCount(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        freq = Counter(s)
        
        # Get unique vowels in the string
        unique_vowels = [v for v in vowels if freq[v] > 0]
        if not unique_vowels:
            return 0
    
        # Count selection ways: multiply occurrence of each vowel
        selection_ways = 1
        for v in unique_vowels:
            selection_ways *= freq[v]
        
        # Total permutations = selection_ways × (number of vowels)!
        return selection_ways * factorial(len(unique_vowels))
