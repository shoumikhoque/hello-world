def coin_change(coins, total,dp):
    if total<=0:
        return 0
    if dp[total]!= float('inf')
        for i in coins:
            if i<=total:
                dp[i]=min(dp[i],1+coin_change(coins,total-i,dp[i]))
    return dp[total]


if __name__ == '__main__':
    coins = [1, 2, 4, 5]
    coins.reverse()
    total = 11
    dp=[float('inf') for x in range(total+1)]
    print(coin_change(coins,total,dp))