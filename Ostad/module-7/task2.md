## Task 1
**Code in [merge_linked_list.py](merge_linked_list.py)**

### Solution 1: simple traversal
- start traversal from the heads of both linked_list
- add any value to the `list1` from  `list2` when  `node2.val<node1.next.val`
- return `list1`

````
Time Complexity: O(n)
Space Complexity: O(1)
````

### Problem Statement
Write a function that does the following task.<br>
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.<br>
(You must create the linked lists and pass the head to the function you created.)
Also, mention the Time and Space Complexity of your solution
## Constraints
```
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
```
### Example 1
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```
**Explanation**:<br>
Given linked lists
list1: head -> 1 -> 2 -> 4
list2: head -> 1 -> 3 -> 4
Output linked list: head -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
### Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

### Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```
**Explanation**:<br>
Given linked lists
list1: head ->
list2: head -> 0
Output linked list: head -> 0