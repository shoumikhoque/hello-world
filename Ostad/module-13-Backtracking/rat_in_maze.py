def is_valid_path(n,m,i=0,j=0):
    if i>=n or j>=n:
        return False
    if m[i][j]==0 or m[n-1][n-1]==0:
        return False
    if i==n-1 and j==n-1:
        return True
    return is_valid_path(n,m,i+1,j) or is_valid_path(n,m,i,j+1)

if __name__ == '__main__':
    n=4
    m=[[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]
    print(is_valid_path(n,m))