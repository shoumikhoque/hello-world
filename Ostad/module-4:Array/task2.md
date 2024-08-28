## Task 2:
**Code in [Best time to buy and sell stock](buying_selling_stocks.py)**
### Solution 1: Brute Force
checking for each price pair for each day in nested loop
````
Time Complexity: O(n^2)
Space Complexity: O(1)
````

### Solution 2: Greedy
- using cumulative sum to find current_max profit for i-th day
- updating current_max profits to find the overall max profit
````
Time Complexity: O(n)
Space Complexity: O(1)
````
Write a function that does the following task.

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
<br>
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
<br>
Also, mention the Time and Space Complexity of your solution


### Constraints: 
```
1 <= prices.length <= 105
0 <= prices[i] <= 104
```
### Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
```
**Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.**

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
```
**Explanation: In this case, no transactions are done and the max profit = 0.**