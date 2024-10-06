# In place manipulation of Linked List

## Introduction
Uses no extra space to modify linked-list

### Pattern:
1. Linked list restructuring: The input data is given as a linked list, and the task is to modify its structure without 
modifying the data of the individual nodes.

2. In-place modification: The modifications to the linked list must be made in place, that is, we’re not allowed to use 
more than O(1) additional space.

### Real World problems:
- **File system management**: for rearranging files within a directory
- **memory management**: for dynamic memory allocation, garbage collection etc
## Practice Problems

### 1. N-Queens @ [Leetcode:Hard](https://leetcode.com/problems/n-queens/) 
````
input: n
output: all possible board view with above conditions
````
#### Steps : [Solution](n_queens.py)
1. Place a queen in the first column of the first row.
2. Place a queen wherever permissible in the next row.
3. Backtrack if no safe configuration exists.
4. Once a solution is found, backtrack to find other possible configurations.
#### Complexity
`Time: O(n!)
Space: O(n)`