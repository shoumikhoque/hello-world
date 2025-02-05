import copy


def knapsack_dp(weights, values, capacity):
    dp=[[0]*(capacity+1)]*len(weights)
    def calc(index,cap):
        if cap<=0 or index==len(weights):
            return 0
        if dp[index][cap]==0:
            if weights[index]<=cap:
                # take this element
                x=values[index]+calc(index+1,cap-weights[index])
                # or leave this element
                y=calc(index+1,cap)
                dp[index][cap]= max(x,y)
        return dp[index][cap]
    return calc(0,capacity)


def knapsack_tabulation(weights,values,capacity):
    n=len(weights)
    dp=[[0 for i in range(capacity+1)] for x in range (n+1)]

    for i in range(1,n+1):
        for j in range(1,capacity+1):
            wt=weights[i-1]
            if wt<=j:
                dp[i][j] = max(values[i-1] + dp[i-1][j-wt],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
def knapsack_memory_optimized(weights,values,capacity):
    n=len(weights)
    dp=[0]*(capacity+1)
    temp=[0]*(capacity+1)
    for i in range(n+1):
        for j in range(capacity+1):
            if weights[i-1]<=j:
                temp[j]=max(values[i-1]+dp[j-weights[i-1]],dp[j])
            else:
                temp[j]=dp[j]
        dp=copy.deepcopy(temp)

    return dp[capacity]
def knapsack_shortest(weights,values,capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for j in range(capacity, -1, -1):
            if weights[i] <= j:
                dp[j] = max(values[i] + dp[j - weights[i]], dp[j])
    return dp[capacity]




# 10 , [3,6,10,7,2] , [12,10,15,17,13]
if __name__ == '__main__':
    weights = [[1, 2, 3, 5], [4], [2], [3, 6, 10, 7, 2], [3, 6, 10, 7, 2, 12, 15, 10, 13, 20]]
    values = [[1, 5, 4, 8], [2], [3], [12, 10, 15, 17, 13], [12, 10, 15, 17, 13, 12, 30, 15, 18, 20]]
    capacity = [6, 3, 3, 10, 20]
    print(knapsack_shortest(weights[0],values[0],capacity[0]))