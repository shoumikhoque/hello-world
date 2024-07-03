
def buying_selling_stocks_brute_force(prices):
    """
    time-> O(n^2), space-> O(1)
    checking for each price pair for each day in nested loop
    """
    if len(prices)<2:
        return 0
    current_max = 0
    ans = 0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            current_max=max(0,current_max,prices[j]-prices[i])
        ans=max(ans,current_max)
    return ans
def buy_selling_stocks_greedy(prices):
    """
    time-> O(n), space-> O(1)
    using cumulative sum to find current_max profit for i-th day
    updating current_max profits to find the overall max profit
    """
    if len(prices)<2:
        return 0
    current_max = 0
    ans = 0
    for i in range(1,len(prices)):
        current_max+=prices[i]-prices[i-1]
        current_max=max(0,current_max)
        ans=max(current_max,ans)
    return ans


if __name__ == '__main__':
    prices=[7,1,5,3,6,4]
    print(buy_selling_stocks_greedy(prices))
    print(buying_selling_stocks_brute_force(prices))