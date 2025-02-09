def change(amount, coins) :
    def calc(amount, pos, ans):
        if amount == 0:
            return ans + 1
        if amount < 0 or pos >= len(coins):
            return 0
        for i in range(pos, len(coins)):
            if coins[i] <= amount:
                ans = calc(amount - coins[i], i, ans)
        return ans
    return calc(amount, 0, 0)



if __name__ == '__main__':
    amount = 5
    coins = [1,2,5]
    coins.reverse()
    print(change(amount,coins,))