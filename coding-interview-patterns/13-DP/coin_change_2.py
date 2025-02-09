def calc(amount,coins,pos,ans):
    if amount == 0:
        return ans + 1
    if amount < 0 or pos >= len(coins):
        return 0
    for i in range(pos, len(coins)):
        if coins[i] <= amount:
            ans = calc(amount - coins[i], coins, i, ans)
    return ans



if __name__ == '__main__':
    amount = 10
    coins = [10]
    coins.reverse()
    print(calc(amount,coins,0,0))