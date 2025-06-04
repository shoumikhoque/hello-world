def solve(cost):
    src = 0
    dest = len(cost) - 1
    dp = {}
    def min_cost(src, dest):
        if src == dest:
            return 0
        if (src, dest) in dp:
            return dp[(src, dest)]
        if src < dest:
            dp[(src, dest)] = cost[src][dest]
            for i in range(src + 1, dest):
                dp[(src, dest)] = min(dp[(src, dest)], min_cost(src, i) + min_cost(i, dest))
            return dp[(src, dest)]

    return min_cost(src, dest)

def solve_tabulation(cost):
    n = len(cost)
    dp = [float('inf')] * n
    dp[0] = 0  # Starting at station 0

    for i in range(1, n):
        for j in range(i):
            if cost[j][i] != -1:  # Check if a direct route exists
                dp[i] = min(dp[i], dp[j] + cost[j][i])


'''
There are N stations on route of a train.
The train goes from station 0 to N-1.
The ticket cost for all pair of stations (i, j) is given where j is greater than i. 
Find the minimum cost to reach the destination.
'''
if __name__ == '__main__':
    cost = [[0, 15, 80, 90],
            [float('inf'), 0, 40, 50],
            [float('inf'), float('inf'), 0, 70],
            [float('inf'), float('inf'), float('inf'), 0]]

    print(solve_tabulation(cost))
