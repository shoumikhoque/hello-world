from collections import deque
def solve(mat):
    if not mat or not mat[0]:
        return []
    rows, cols = len(mat), len(mat[0])
    queue = deque()
    mx = rows * cols
    # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                mat[i][j] = mx
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and mat[r][c] > mat[row][col] + 1:
                queue.append((r, c))
                mat[r][c] = mat[row][col] + 1
    return mat

def solve_using_two_dp_loop(mat):
    rows = len(mat)
    if rows == 0:
        return []

    cols = len(mat[0])
    if rows == 1 and cols == 1:
        return mat
    mx = rows * cols
    dp = [[mx] * cols for _ in range(rows)]
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if mat[i][j] == 0:
                dp[i][j] = 0
            else:
                right = dp[i][j + 1] if j + 1 < cols else mx
                bottom = dp[i + 1][j] if i + 1 < rows else mx
                dp[i][j] = 1 + min(right, bottom)

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                dp[i][j] = 0
            else:
                left = dp[i][j - 1] if j - 1 >= 0 else mx
                top = dp[i - 1][j] if i - 1 >= 0 else mx
                dp[i][j] = min(dp[i][j], 1 + min(top, left))
    return dp

if __name__ == '__main__':
    # mat = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    #        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    #        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    #        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    #        [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    #        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    #        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    #        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    #        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    #        [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
    mat=[[0,0,0],[0,1,0],[1,1,1]]
    print(solve(mat))
