## Task 1

**Code in [connected_components.py](connected_components.py)**

### Solution : Simple DFS

````
Time Complexity: O(n) 
Space Complexity: O(n)
````

### Problem Statement

Write a function that does the following task.

Given a graph with A nodes.
The edges in the graph are given in a 2D array B.
There is an undirected edge between B[i][0] and B[i][1].
Find the number of connected components in the given graph.

Mention the time and space complexity of your solution.

## Constraints
````
1 <= A <= 10^5
1 <= |B| <= 10^5
1 <= B[i][0], B[i][1] <= A
````
### Example 1

```
Input:A = 4 B =[[1, 2],[2, 3]]
Output : 2
Explanation: The two connected components are [1, 2, 3] and [4].
```

### Example 2:

```
Input:
A = 3 B = [[1, 2],[2, 1]]
Output: 2
Explanation: The two connected components are [1, 2] and [3].
```
