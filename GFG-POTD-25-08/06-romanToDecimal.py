class Solution:
    def romanToDecimal(self, s): 
        # code here
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            value = roman_map[s[i]]

            # If the current value is less than the next one, subtract it
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= value
            else:
                total += value

        return total
