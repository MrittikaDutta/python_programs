
from collections import Counter
class Solution:
    def smallestWindow(self, s, p):
        # code here
        if len(p) > len(s):
            return ""
            
        # Create a frequency map for characters in p
        p_freq = Counter(p)
        
        # Initialize a window frequency map (optional, can be done with p_freq directly)
        window_freq = {}
        
        # Initialize pointers and variables for the result
        left = 0
        min_len = float('inf')
        start_index = -1
        
        # Keep track of how many characters from p are currently matched in the window
        matched = 0
        
        # Loop through the string s with the right pointer
        for right, char_right in enumerate(s):
            # Add the current character to the window frequency
            window_freq[char_right] = window_freq.get(char_right, 0) + 1
            
            # Check if this character is one we need from p
            if char_right in p_freq and window_freq[char_right] <= p_freq[char_right]:
                matched += 1
            
            # When we have a valid window (all characters from p are matched)
            while matched == len(p):
                # Update the result if the current window is the smallest so far
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    start_index = left
                    
                # Try to shrink the window from the left
                char_left = s[left]
                
                # Check if the character leaving the window is a required one
                if char_left in p_freq and window_freq[char_left] <= p_freq[char_left]:
                    matched -= 1
                    
                # Decrease the count of the character leaving the window
                window_freq[char_left] -= 1
                
                # Move the left pointer to shrink the window
                left += 1
                
        # If no valid window was found, start_index will remain -1
        if start_index == -1:
            return ""
        
        # Return the smallest window substring
        return s[start_index : start_index + min_len]
