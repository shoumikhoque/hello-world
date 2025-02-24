def solve(n):
    if n==0 or n==1:
        return 1
    dp=[1]+[1]+[0]*(n)
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]


if __name__ == '__main__':
    n=3
    print(solve(n))