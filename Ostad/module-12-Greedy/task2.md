## Task 2
**Code in [max_disjoint_intervals.py](max_disjoint_intervals.py)**

### Solution : Simple greedy

````
Time Complexity: O(nlogn)
Space Complexity: O(1)
````

### Problem Statement
Write a function that does the following task.

Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.
Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.
Return a integer denoting the length of maximal set of mutually disjoint intervals
Mention the time and space complexity of your solution.
## Constraints
`1 <= N <= 10^5
1 <= A[i][0] <= A[i][1] <= 10^9`

### Example 1
```
Input: A = [ [1, 4], [2, 3], [4, 6], [8, 9] ]
Output: 3
```
Explanation :
Intervals [2, 3] and [1, 4] overlap.
We must include [2, 3] because if [1, 4] is included then we cannot include [4, 6].
We can include at max three disjoint intervals: [[2, 3], [4, 6], [8, 9]]
### Example 2:
```
Input :  A = [ [1, 9], [2, 3], [5, 7] ]
Output: 2
```
Explanation 2:
We can include at max two disjoint intervals: [[2, 3], [5, 7]]
