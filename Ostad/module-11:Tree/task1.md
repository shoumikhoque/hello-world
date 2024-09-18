## Task 2
**Code in [binary_tree_height.py](binary_tree_height.py)**

### Solution : BFS traversal

````
Time Complexity: O(n) for traversing all the nodes of the binary tree
Space Complexity: O(log(n))  for memory stack
````

### Problem Statement


Given the root of a binary tree, return its Height. A binary tree's Height is the number of nodes along the longest path from the root node down to the farthest leaf node.

Mention the time and space complexity of your solution.
## Constraints
```
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
```
```
Note: You will be given a tree as input. The example inputs are shown as an array for simplification only.
In the array, the (2^index) is the left child and (2^index + 1) is the right child of the node at 'index'. In this case, index=0 is the root of the tree.
### Example 1
```
Input: root = [3,9,20,null,null,15,7] 
Output: 3
Explanation: 
the tree is visually as following
    3
   /  \
  9   20
 / \
7  15
```
### Example 2:
```
Input: root = [1,null,2]
Output: 2
Explanation: the tree is visually as following
      1
    /  \
        2
```