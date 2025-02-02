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


# 10 , [3,6,10,7,2] , [12,10,15,17,13]
if __name__ == '__main__':
    weights = [[1, 2, 3, 5], [4], [2], [3, 6, 10, 7, 2], [3, 6, 10, 7, 2, 12, 15, 10, 13, 20]]
    values = [[1, 5, 4, 8], [2], [3], [12, 10, 15, 17, 13], [12, 10, 15, 17, 13, 12, 30, 15, 18, 20]]
    capacity = [6, 3, 3, 10, 20]
    print(knapsack_dp([3,6,10,7,2],[12,10,15,17,13],10))