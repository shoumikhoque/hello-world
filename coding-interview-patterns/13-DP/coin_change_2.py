def change(amount, coins) :
    dp = [[0] * len(coins) for x in range(amount + 1)]
    def calc(amount, pos):
        if amount == 0:
            return  1
        if amount < 0 or pos >= len(coins):
            return 0
        if dp[amount][pos]==0:
            for i in range(pos, len(coins)):
                if coins[i]==amount:
                    dp[amount][pos]=1
                elif coins[i] < amount:
                    dp[amount][pos] += calc(amount - coins[i], i)
        return sum(dp[amount][pos:])
    return calc(amount, 0)

# 5
# [5,2,1]


if __name__ == '__main__':
    amount = 500
    coins = [2,7,13]
    coins.reverse()
    print(change(amount,coins))