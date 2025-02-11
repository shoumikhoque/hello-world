def change(amount, coins) :
    if amount == 0:
        return 1
    dp = [[0] * len(coins) for x in range(amount + 1)]
    coins.reverse()
    def calc(amount, pos):
        if dp[amount][pos]!=0:
            return dp[amount][pos]
        for i in range(pos, len(coins)):
            if coins[i] == amount:
                dp[amount][pos] += 1
            elif coins[i] < amount:
                dp[amount][pos] += calc(amount - coins[i], i)
        return dp[amount][pos]

    return calc(amount, 0)

# 5
# [5,2,1]


if __name__ == '__main__':
    amount = 5
    coins = [5,2,1]

    print(change(amount,coins))