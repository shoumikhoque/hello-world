def solve(n):
    if n <3:
        return n
    MOD=1e9 +7
    dp=[[0]*3 for i in range(n+1)]
    dp[0][0]=dp[1][0]=1
    dp[1][1]=dp[1][2]=1
    for i in range(2,n+1):
        dp[i][0]=(dp[i-1][0]+dp[i-2][0]+
                  dp[i-2][1]+dp[i-2][2]) %MOD
        dp[i][1]=(dp[i-1][0]+dp[i-1][2])%MOD
        dp[i][2]=(dp[i-1][0]+dp[i-1][1])%MOD

    return int(dp[n][0])
def solve_optimized(n):
    if n <3:
        return n
    dp = [0]*(n+1)
    dp[0]=1
    dp[1]=1
    dp[2]=2
    dp[3]=5
    MOD = 1e9 + 7
    for i in range(4,n+1):
        dp[i]=(2* dp[i-1]+dp[i-3])% MOD
    return int(dp[n])



if __name__ == '__main__':
    n=4
    print(solve_optimized(n))