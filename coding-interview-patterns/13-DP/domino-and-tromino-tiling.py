def solve(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    MOD = 10 ** 9 + 7
    dp = [0] * (n + 1)

    dp2 = [0] * (n + 1)

    # Base cases
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    dp2[1] = 1
    dp2[2] = 2

    # Fill dp and dp2 using recurrence relations
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp2[i - 1]) % MOD
        dp2[i] = (dp[i - 1] + dp2[i - 1]) % MOD

    return dp[n]


if __name__ == '__main__':
    n=4
    print(solve(n))