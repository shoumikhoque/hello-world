## Task 1

**Code in [cycle_in_graph.py](cycle_in_graph.py)**

### Solution : Simple DFS

````
Time Complexity: O(n) 
Space Complexity: O(n)
````

### Problem Statement

Write a function that does the following task.

Given a directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is an edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

Mention the time and space complexity of your solution.

NOTE:
The cycle must contain at least two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.

## Constraints
````
2 <= A <= 10^5
1 <= M <= min(200000,A(A-1))
1 <= B[i][0], B[i][1] <= A
````
### Example 1

```
Input:
A = 5
B = [  [1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3] ]

Output: 1

Explanation: The given graph contain cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1
```

### Example 2:

```
Input :
A = 5
B = [ [1, 2], [2, 3], [3, 4], [4, 5] ]

Output: 0

Explanation: The given graph doesn't contain any cycle.
```
