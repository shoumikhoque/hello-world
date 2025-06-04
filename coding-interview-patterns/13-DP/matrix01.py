from collections import deque


def solve(mat):
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    queue = deque()
    MAX_VALUE = m * n

    # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                mat[i][j] = MAX_VALUE

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                queue.append((r, c))
                mat[r][c] = mat[row][col] + 1

    return mat


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
