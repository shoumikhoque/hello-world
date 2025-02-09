def change(amount, coins) :
    dp = [[0] * len(coins) for x in range(amount + 1)]
    def calc(amount, pos):
        if amount == 0:
            return dp[amount][pos] + 1
        if amount < 0 or pos >= len(coins):
            return 0
        if dp[amount][pos]==0:
            for i in range(pos, len(coins)):
                if coins[i] <= amount:
                    dp[amount][pos] = calc(amount - coins[i], i)
        return dp[amount][pos]
    calc(amount, 0)
    return sum(dp[amount])



if __name__ == '__main__':
    amount = 5
    coins = [1,2,5]
    coins.reverse()
    print(change(amount,coins))