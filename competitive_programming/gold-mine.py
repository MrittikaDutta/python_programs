def maxGold(n, m, M):
    # Create a 2D array to store the maximum gold collected at each cell
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # Initialize the last column of dp with the values from the mine
    for i in range(n):
        dp[i][m - 1] = M[i][m - 1]

    # Iterate over each column starting from the second-to-last column
    for j in range(m - 2, -1, -1):
        for i in range(n):
            # Consider three possible moves: diagonally up, right, diagonally down
            move_up = dp[i - 1][j + 1] if i - 1 >= 0 else 0
            move_right = dp[i][j + 1]
            move_down = dp[i + 1][j + 1] if i + 1 < n else 0

            # Update the current cell with the maximum gold collected
            dp[i][j] = M[i][j] + max(move_up, move_right, move_down)

    # Find the maximum value in the first column of dp
    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold, dp[i][0])

    return max_gold

# Example usage:
n1, m1 = 3, 3
M1 = [
    [1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]
]
print(maxGold(n1, m1, M1))  # Output: 12

n2, m2 = 4, 4
M2 = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]
print(maxGold(n2, m2, M2))  # Output: 16
