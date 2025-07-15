def longest_common_subsequence(list1, list2):
    m, n = len(list1), len(list2)
    # Initialize a 2D list to store LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if list1[i - 1] == list2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from dp table
    lcs_length = dp[m][n]
    lcs = [0] * lcs_length
    i, j = m, n
    while i > 0 and j > 0:
        if list1[i - 1] == list2[j - 1]:
            lcs[lcs_length - 1] = list1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 1, 3, 5]
result = longest_common_subsequence(list1, list2)
print("Longest Common Subsequence:", result)
