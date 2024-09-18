## Task 1
**Code in [binary_search_tree.py](binary_search_tree.py)**

### Solution : search in BST

````
Time Complexity: O(logn)
Space Complexity: O(1) 
````

### Problem Statement
You are given a binary search tree (BST) and an integer val. Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Mention the time and space complexity of your solution.
## Constraints
```
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
The tree is a binary search tree.
1 <= val <= 10^7
```
```
Note: You will be given the root node of the trees. The example inputs are shown as an array for simplification only.
```
### Example 1
```
Input: tree = [4,2,7,1,3], val = 2 
Output: [2,1,3]

Explanation:
val = 2
Input tree:
      4
     / \
   2    7
  / \
 1   3

output:
  2
 / \
1   3
Or an array [2,1,3]
```
### Example 2:
```
Input: tree= [4,2,7,1,3], val = 5
Output: []

Explanation:
val= 5
Input tree:
      4
     / \
   2  7
  / \
1   3

Output: null or an array [ ]
```