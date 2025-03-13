from uaclient.util import retry


def solve(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    dp={}
    def calc(r,c):
        if r>=rows or c>=cols:
            return 0
        if (r,c) not in dp:
            dp[(r,c)]=int(matrix[r][c])
            if matrix[r][c]=='1' :
                dp[(r,c)]=1+min(calc(r,c+1),calc(r+1,c),calc(r+1,c+1))
            else:
                calc(r+1,c)
                calc(r,c+1)
        return dp[(r,c)]
    calc(0,0)
    return max(dp.values())**2

def solve_table(matrix):
     rows = len(matrix)
     cols = len(matrix[0])
     mx=0
     for r in range(rows-1,-1,-1):
         for c in range(cols-1,-1,-1):
             if matrix[r][c]=='1':
                 bottom=right=diagonal=0
                 if r+1<rows and c+1<cols:
                     diagonal=matrix[r+1][c+1]
                 if r+1<rows:
                    bottom = matrix[r + 1][c]
                 if c+1< cols:
                    right = matrix[r][c + 1]
                 matrix[r][c]=1+min(diagonal,right,bottom)
             else:
                 matrix[r][c]=0
             if mx<matrix[r][c]:
                 mx=matrix[r][c]
     return mx ** 2

if __name__ == '__main__':
    matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(solve_table(matrix))