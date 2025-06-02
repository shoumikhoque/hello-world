'''
There are N stations on route of a train.
The train goes from station 0 to N-1.
The ticket cost for all pair of stations (i, j) is given where j is greater than i.
Find the minimum cost to reach the destination.
'''
def solve(cost):
    n=len(cost)
    dp=[[-1]*n for _ in range(n)]
    def calc(src,dst):
        if src>=dst:
            return 0
        if dp[src][dst]>0:
            return dp[src][dst]

    return calc(0,n-1)

def to_sparse_array(matrix):
    sparse = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val = matrix[i][j]
            if val != -1:
                sparse.append((i, j, val))
    return sparse
if __name__ == '__main__':
    cost= [[0, 15, 80, 90],
           [-1, 0, 40, 50],
           [-1, -1, 0, 70],
           [-1, -1, -1, 0]]

    print(solve(cost))
