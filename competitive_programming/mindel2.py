def min_deletions_to_make_palindrome(S):
    n = len(S)
    # Create a table to store the length of the longest palindromic subsequence
    dp = [[0] * n for _ in range(n)]

    # All characters are palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the table using bottom-up approach
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if S[i] == S[j] and cl == 2:
                dp[i][j] = 2
            elif S[i] == S[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # Minimum number of deletions is equal to the length of the input string minus length of longest palindromic subsequence
    min_deletions = n - dp[0][n - 1]
    return min_deletions

# Example usage
input_string1 = "aebcbda"
print("Output for input '{}' : {}".format(input_string1, min_deletions_to_make_palindrome(input_string1)))

input_string2 = "geeksforgeeks"
print("Output for input '{}' : {}".format(input_string2, min_deletions_to_make_palindrome(input_string2)))
