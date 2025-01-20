def coin_counts(coins, coins_len, sum, dp):
    if sum==0:
        return 1
    if sum<0 or coins_len==0:
        return 0
    if dp[coins_len-1][sum]==0:
        dp[coins_len - 1][sum]=(coin_counts(coins[:-1],coins_len-1,sum,dp)+
                    coin_counts(coins,coins_len,sum-coins[coins_len-1],dp))
    return dp[coins_len - 1][sum]
def coin_counts_bottom_up(coins,sum):
    if sum<=0 or len(coins)<=0:
        return 1
    dp = [[0 for x in range(len(coins))] for i in range(sum + 1)]
    for i in range(len(coins)):
        dp[0][i]=1
    for i in range(1,sum+1):
        for j in range(len(coins)):
            x,y=0,0
            if i-coins[j]>=0: # include coin[j]
                x = dp[i - coins[j]][j]
            if j-1>=1: # exclude coin[j]
                y = dp[i][j - 1]
            dp[i][j]=x+y
    return dp[sum][len(coins)-1]


if __name__ == '__main__':
    coins=[25,10,5,2,1]
    sum=10
    dp=[[0 for x in range(sum+1)] for i in range(len(coins))]
    # print(coin_counts(coins,len(coins),sum,dp))
    print(coin_counts_bottom_up(coins, sum))