def solve(grid):
    m=len(grid)
    n=len(grid[0])
    if m==1  and n==1:
        return int(grid[0][0]==0)
    dp=[[-1]*n for i in range(m)]
    def dfs(i,j):
        if i<0 or j<0:
            return 0
        if i==0 and j==0:
            return int(grid[0][0]==0)
        if dp[i][j]==-1 :
            if  grid[i][j]==0:
                dp[i][j]= dfs(i-1,j)+dfs(i,j-1)
            else:
                dp[i][j]= 0
        return dp[i][j]
    return dfs(m-1,n-1)
def solve_table:
    pass

if __name__ == '__main__':
    grid= [[0,0,0],[0,1,0],[0,0,0]]
    print(solve(grid))