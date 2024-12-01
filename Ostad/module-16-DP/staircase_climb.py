def climbStairs(n):
    if n <= 1:
        return 1

    # Initialize base cases
    prev2 = 1  # This is ways[0]
    prev1 = 1  # This is ways[1]

    # DP iteration from step 2 up to step n
    for i in range(2, n + 1):
        current = prev1 + prev2  # ways[i] = ways[i-1] + ways[i-2]
        prev2 = prev1  # Move prev2 to prev1
        prev1 = current  # Move prev1 to current

    return prev1
