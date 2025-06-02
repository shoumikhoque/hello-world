def solve(mat):
    m = len(mat)
    n = len(mat[0])
    if m == 1 and n == 1:
        return mat
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                temp = 100000
                if i - 1 >= 0:
                    temp = min(temp, mat[i - 1][j])
                if j - 1 >= 0:
                    temp = min(temp, mat[i][j - 1])
                if i + 1 < m:
                    temp = min(temp, mat[i + 1][j])
                if j + 1 < n:
                    temp = min(temp, mat[i][j + 1])
                mat[i][j] =1+ temp
    return mat


if __name__ == '__main__':
    mat = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
           [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
           [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
           [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
    print(solve(mat))
