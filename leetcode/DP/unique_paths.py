def solve(m, n):
    if m==1 or n==1:
        return 1
    dp=[[-1]*(n+1) for i in range(m+1)]
    def run(i,j):
        if i==m and j==n:
            return 1
        if i>m or j>n:
            return 0
        if dp[i][j]==-1:
            dp[i][j]= run(i+1,j) + run (i,j+1)
        return dp[i][j]
    return run(1,1)
def solve_table(m,n):
    if m==1 or n==1:
        return 1
    dp=[[0]*(n+1) for i in range(m+1)]
    dp[1][1]=dp[1][0]=dp[0][1]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]

    return dp[m][n]


if __name__ == '__main__':
    m=3
    n=7
    print(solve_table(m,n))