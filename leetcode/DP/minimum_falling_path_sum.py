def solve(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    dp = [[0] * n for _ in range(n)]

    def calc(i, j):
        if i == n :
            return 0
        if j == n or j<0:
            return float('inf')
        if dp[i][j] == 0:
            dp[i][j] = (matrix[i][j] + min(calc(i + 1, j), calc(i + 1, j + 1), calc(i + 1, j - 1)))
        return dp[i][j]
    mx=float('inf')
    for i in range(n):
        mx=min(mx,(calc(0, i)))
    return mx

def solve_table(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    dp = [[float('inf')] *( n+1) for _ in range(n+1)]
    for i in range(n):
        dp[n][i]=0
    dp[n][n]=0
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            dp[i][j]=matrix[i][j]+min(dp[i+1][j],dp[i+1][j-1],dp[i+1][j+1])
    return min(dp[0])
if __name__ == '__main__':
    matrix=[[2,1,3],[6,5,4],[7,8,9]]
    print(solve_table(matrix))


