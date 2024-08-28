## Task 1
**Code in [reverse_linked_list.py](reverse_linked_list.py)**

### Solution : In place reversal

````
Time Complexity: O(n)
Space Complexity: O(1)
````

### Problem Statement
Write a function that does the following task.<br>
Given the head of a singly linked list, reverse the list, and return the reversed list.<br>
(You must create the linked list and pass the head to the function you created.)
Also, mention the Time and Space Complexity of your solution.
## Constraints
```
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
```
### Example 1
```
Input: head = [1,2,3,4,5] 
Output:  [5,4,3,2,1]
```
**Explanation**:<br>
Given linked list: head -> 1 -> 2 -> 3 -> 4 -> 5
Output linked list: head -> 5 -> 4 -> 3 -> 2 -> 1
### Example 2:
```
Input: head = [1,2]
Output: [2,1]
```
**Explanation**:<br>
Given linked list: head -> 1 -> 2
Output linked list: head ->2 -> 1
### Example 3:
```
Input: head = []
Output: []
```
