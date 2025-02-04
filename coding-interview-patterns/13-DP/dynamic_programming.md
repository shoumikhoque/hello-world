# Dynamic Programming
## Intro:

### Pattern:
1. Optimal Substructure
2. Overlapping SubProblems

### TopDown Approach
`fib(n)=fib(n-1)+fib(n-2)+ ..... + fib(1)+fib(0)`
### Bottom Up Approach
`(f(0)+f(1)=f(2))+f(1)=f(3).......=f(n-1)+ f(n-2)=f(n)`
### Real World problems:
1. Optimal route planning in gps navigation systems
2. Text Justification
3. Robotics motion planning
4. 
## Practice Problems
### 1. 0/1 Knapsack 
````
input: list of weights, list of profits of objects and capacity of bag
output: maximum value that can be put in the bag  
````
#### Steps : [Solution](knapsack_01.py)
#### Brute force
1. Base case: if there is no item to add in the bag or max capacity is reached then return 0
2. if the current item weighs more than capacity , then we don't include the item and move to next item. 
3. else we make two recursive calls , one for including the item in the bag and other for excluding the item in the bag. we take maximum if these two values.
#### Top-Down Memoization:
in the naive solution we get two variable(capacity and the number of items to consider) changes in recursive call. therefore, we take a 2D table to memoize. 
#### Bottom-Up Tabulation: 
1. 2D table dp of size(n+1)*(capacity+1). Each row corresponds to an item and each column represents the remaining capacity of knapsack at any given point.
2. dp[i][j] stores the value of the combination that consists of 0 or more of the first items that doesn't weigh more than j and there is no combination of these items that yields a higher profit.
3. first, we fill the first column with 0 , since the value of knapsack is 0 when the capacity is 0
4. then we fill the first row with 0,since 0 items added will have no value. 
5. for the remaining rows , we iterate from top-left to bottom-right
6. if the weight of i-th item is less than or equal j-weights[i] capacity than we can find the max profit from calculating the including it and excluding it  
7. else we reuse the subproblem of dp[i-1][j]
8. return the last entry dp[n][capacity]

#### Complexity
