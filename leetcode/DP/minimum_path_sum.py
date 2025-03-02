def solve(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]
    def dfs(i, j):
        if i == m - 1 and j == n - 1:
            return grid[i][j]
        if dp[i][j] == 0:
            if i == m - 1:
                dp[i][j] = grid[i][j] + dfs(i, j + 1)
            elif j == n - 1:
                dp[i][j] = grid[i][j] + dfs(i + 1, j)
            else:
                dp[i][j] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
        return dp[i][j]
    return dfs(0, 0)

def solve_table(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0]=grid[0][0]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                continue
            dp[i][j]=grid[i][j]+min(dp[i][j],dp[i-1][j],dp[i][j-1])
    return dp[m-1][n-1]

if __name__ == '__main__':
    grid= [[1,3,1],[1,5,1],[4,2,1]]
    print(solve_table(grid))