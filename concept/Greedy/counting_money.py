"""
Statement:
Given an infinite number of quarters (25cents)(25cents), dimes (10cents)(10cents), nickels (5cents)(5cents),
and pennies (1cent)(1cent), implement a function to calculate the minimum number of coins to represent vv cents.
inputs:
v = 19, available_coins = [1, 5, 10, 25]
Constraints:
The available coins are in the ascending order.
"""
def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    # Initialize result
    result = []
    n = len(coins_available)

    # Traverse through all available coins
    for i in reversed(range(n)):
        while v >= coins_available[i]:
            v -= coins_available[i]
            result.append(coins_available[i])

    return result


# Main program to test the above code
if __name__ == "__main__":

    coins_available = [1, 5, 10, 25] # The available coins are in increasing order
    print(find_min_coins(19, coins_available))