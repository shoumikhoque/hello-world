from decimal import Decimal


def coin_change(coins, total,dp):
    if total<=0:
        return 0
    if dp[total]== Decimal('Infinity'):
        for i in coins:
            if i<=total:
                dp[total]=min(dp[total],1+coin_change(coins,total-i,dp))
    return dp[total]


if __name__ == '__main__':
    coins = [1, 2, 4, 5]
    coins.reverse()
    total = 11
    dp=[Decimal('Infinity') for x in range(total+1)]
    print(coin_change(coins,total,dp))