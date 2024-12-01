def maxProfit(prices):
    if not prices:
        return 0

    # Initialize variables for DP states
    hold = -prices[0]  # Profit if we bought the stock on day 0
    not_hold = 0  # Profit if we didn't buy any stock

    for i in range(1, len(prices)):
        # Update states
        new_hold = max(hold, not_hold - prices[i])
        new_not_hold = max(not_hold, hold + prices[i])

        # Move to the next day
        hold = new_hold
        not_hold = new_not_hold

    # The result is the maximum profit with no stock held on the last day
    return not_hold
