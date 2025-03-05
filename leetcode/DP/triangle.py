def solve(triangle):
    if len(triangle)==1:
        return triangle[0][0]
    dp=[[float('inf')] * i for i in range(1,len(triangle)+1)]
    def calc(i,j):
        if i==len(triangle):
            return 0
        if dp[i][j]==float('inf'):
            dp[i][j]=triangle[i][j]+min(calc(i+1,j),calc(i+1,j+1))
        return dp[i][j]
    return calc(0,0)
def solve_table(triangle):
    if len(triangle)==1:
        return triangle[0][0]
    dp=[[0] * i for i in range(len(triangle)-1,-1,-1)]
    for i in range(len(triangle)-1,-1,-1):
        for j in range(len(triangle[0])-1,-1,-1):
            dp[i][j]=triangle[i][j]+min(dp[i-1][j],dp[i-1][j-1])
    return dp[0][0]

if __name__ == '__main__':
    triangle =[[2],[3,4],[6,5,7],[4,1,8,3]]
    print(solve_table(triangle))