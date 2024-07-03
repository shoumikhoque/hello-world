# def knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, current_index):
#     # base checks
#     if capacity <= 0 or current_index >= profits_length or current_index < 0:
#         return 0
#     # if we have already solved the problem, return the result from the table
#     if lookup_table[current_index][capacity] != 0:
#         return lookup_table[current_index][capacity]
#     # recursive call after choosing the element at the current_index
#     # if the weight of the element at current_index exceeds the capacity, we shouldn't process this
#     profit1 = 0
#     if weights[current_index] <= capacity:
#         profit1 = (profits[current_index] +
#                    knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity - weights[current_index], current_index + 1))
#     # recursive call after excluding the element at the current_index
#     profit2 = knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, current_index + 1)
#     lookup_table[current_index][capacity] = max(profit1, profit2)
#     return lookup_table[current_index][capacity]
# def knap_sack(profits, profits_length, weights, capacity):
#     lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]
#     return knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, 0)
def knap_sack_bottom_up(profits, profits_length, weights, capacity):
    # basic checks
    if capacity <= 0 or profits_length == 0:
        return 0
    lookup_table = [0 for x in range(capacity + 1)]
    # if we have only one weight, we will take it if it is not more than the capacity
    for i in range(capacity + 1):
        if weights[0] <= i:
            lookup_table[i] = profits[0]
    # process all sub-lists for all the capacities
    for i in range(1, profits_length):
        for j in reversed(range(capacity + 1)):
            profit1 = 0
            # include the item, if it is not more than the capacity
            if weights[i] <= j:
                profit1 = profits[i] + lookup_table[j - weights[i]]
            # exclude the item
            profit2 = lookup_table[j]
            # take maximum
            lookup_table[j] = max(profit1, profit2)
    return lookup_table[capacity]




# Driver code to test the above function
if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack_bottom_up(profits, len(profits), weights, 7))
    # print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 6))
