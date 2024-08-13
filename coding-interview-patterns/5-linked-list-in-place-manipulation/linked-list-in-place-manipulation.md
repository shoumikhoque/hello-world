# In place manipulation of Linked List
**Uses no extra space to modify linked-list**
### Usage:
- Linked list restructuring
- In place modification

### Real World problems:
- **File system management**: for rearranging files within a directory
- **memory management**: for dynamic memory allocation, garbage collection etc
## Problems
### 1. Reverse Linked List : [Solution](../../Ostad/module-7/practice/reverse_linked_list.py)
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

### Reverse nodes in k-Group : [Solution](reverse_nodes_in_groups.py)
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
### Ranged Reverse: [Solution](reverse_nodes_in_groups.py)
Given a singly linked list with nn nodes and two positions, left and right, the objective is to reverse the nodes of the list from left to right.
#### Steps
1. store original head node .
2. find left and right positioned nodes , node_before_left and node_after_right
2. disconnect left and right from the original linked list 
3. reverse disconnected linked list
4. reconnect left with node before left and right with node_after_right.
5. reassign the original head node