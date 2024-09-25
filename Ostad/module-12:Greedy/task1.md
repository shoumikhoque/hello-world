## Task 1
**Code in [maximum_unit.py](maximum_unit.py)**

### Solution : Simple greedy

````
Time Complexity: O(n) for traversing all the nodes of the binary tree
Space Complexity: O(log(n))  for memory stack
````

### Problem Statement
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [number_of_boxes_i, number_of_unit_per_box_i]:

Number_of_boxes_i is the number of boxes of type i.
Number_of_unit_per_box_i is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
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