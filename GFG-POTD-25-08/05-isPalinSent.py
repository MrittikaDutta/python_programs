import re
class Solution:
	def isPalinSent(self, s):
		# code here
		cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Step 2: Check if palindrome
        return cleaned == cleaned[::-1]
