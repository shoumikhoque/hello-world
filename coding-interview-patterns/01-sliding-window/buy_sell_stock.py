def max_profit(prices):
    if len(prices) < 2:
        return 0
    current_max = 0
    ans = 0
    for i in range(1, len(prices)):
        current_max += prices[i] - prices[i - 1]
        current_max = max(0, current_max)
        ans = max(current_max, ans)
    return ans


if __name__ == '__main__':
    prices=[10, 4, 11, 1, 5]
    print(max_profit(prices))