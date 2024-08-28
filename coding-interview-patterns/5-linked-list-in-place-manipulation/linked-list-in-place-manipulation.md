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

### 1. Reverse Linked List : [Solution](../../Ostad/module-7:LinkedList/practice/reverse_linked_list.py)
````
input: head of a linked list
output: head of the reversed linked list
````
#### Steps
1. initialize `prev` and `next` pointers to null, `current` pointer to head node
2. traverse the linked list until current reaches the end
3. within the loop
   1. set the next pointer to the `next` node in the list and reverse the `current` node's pointer to point to the `prev` node.
   2. update the `current` and `prev` pointers
4. after the loop, the `prev` pointer will point to the last node of the original linked list, set the head pointer to `prev` pointer.
#### Complexity
`Time: O(n)
Space: O(1)`


### 2.Reverse nodes in k-Group : [Solution](reverse_nodes_in_groups.py)
The task is to reverse the nodes in groups of k in a given linked list, where k is a positive integer, and at most the length of the linked list. If any remaining nodes are not part of a group of kk, they should remain in their original order.
`Note: Use only O(1) extra memory space. Time: O(n)` 

#### Naive Approach: Using a stack :
Push k nodes to a stack. add elements to a new linked list after popping k nodes from the stack. repeat the process linkedlist reaches the end.
`Time: O(n), Space: O(n+k)->O(k) for stack + O(n) for a new linked list`

#### Steps
1. Use a pointer to try to traverse k nodes in the linked list
2. if the pointer successfully traverse a group of k nodes , reverse this group
3. reconnect the reversed group of k nodes with the rest of the linked list
4. repeat the process until less than k or no nodes are left in the linked list

#### Complexity
`Time: O(n)
Space: O(1)`


### 3.Ranged Reverse: [Solution](reverse_nodes_in_groups.py)
Given a singly linked list with n nodes and two positions, left and right, the objective is to reverse the nodes of the 
list from left to right.

#### Steps
1. store original head node .
2. find left and right positioned nodes , node_before_left and node_after_right
2. disconnect left and right from the original linked list 
3. reverse disconnected linked list
4. reconnect left with node before left and right with node_after_right.
5. reassign the original head node

#### Complexity
`Time: O(n)
Space: O(1)`

### 4. ReOrder List: [Solution](reorder_list.py)
Given the head of a singly linked list, reorder the list as if it were folded on itself. For example, if the list is represented as follows:

`L0L0 → L1L1  → L2L2  → … → Ln−2Ln−2  → Ln−1Ln−1 → LnLn`

This is how you’ll reorder it:

`L0L0 → LnLn  → L1L1  → Ln−1Ln−1  → L2L2  → Ln−2Ln−2 → …`

You don’t need to modify the values in the list’s nodes; only the links between nodes need to be changed.

#### Steps
1. Find the middle node. If there are two middle nodes choose the second one.
2. reverse the second half of the list
3. merge 1st and 2nd half of the list

#### Complexity
`Time: O(n)
Space: O(1)`

### 4. Swapping nodes: [Solution](swapping_nodes.py)
Given the linked list and an integer, k, return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end of the linked list.

#### Steps
1. find kth element from first (front) and back(end).
2. swap two nodes

#### Complexity
`Time: O(n)
Space: O(1)`

### 5. Reverse Nodes In Even Length Groups: [Solution](reverse_node_in_even_groups.py)
Given the head of a linked list, the nodes in it are assigned to each group in a sequential manner. The length of these groups follows the sequence of natural numbers. Natural numbers are positive whole numbers denoted by (1,2,3,4...).
#### Steps
1. traverse from head node
2. find each group with size from (1.2.3.....)
3. keep prev node of a group
4. for each group find last of a group and first of next group 
5. reverse the group if the groupSize is even
6. then reassign the group after prev node and before the first node of the next group
7. return the linked list

#### Complexity
`Time: O(n)
Space: O(1)`

### 6. Swap node in pairs: [Solution](swap_each_pairs.py)
swap every two adjacent nodes of the linked list. After the swap, return the head of the linked list.
#### Steps
1. traverse list 
2. check to make sure there is at least two nodes in the remaining part of the list
3. swap the two nodes
4. reconnect two swapped nodes
5. repeat until there is only one or no nodes left

#### Complexity
`Time: O(n)
Space: O(1)`