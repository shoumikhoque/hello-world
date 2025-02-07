def coin_change(coins, total,dp):
    if total<=0:
        return 0
    if dp[total]== total+1:
        for i in coins:
            if i<=total:
                dp[total]=min(dp[total],1+coin_change(coins,total-i,dp))
    return -1 if dp[total]==total+1 else dp[total]
def coin_change_tabulation(coins,total):
    if total<=0:
        return 0
    dp = [total+1 for x in range(total + 1)]
    dp[0]=0
    for sum in range(1,total+1):
        for coin in coins:
            if coin<=sum:
                dp[sum]=min(dp[sum],1+dp[sum-coin])

    return -1 if dp[total]==total+1 else dp[total]


if __name__ == '__main__':
    coins = [1, 2, 4, 5]
    coins.reverse()
    total = 11
    dp=[(total+1) for x in range(total+1)]
    print(coin_change(coins,total,dp))