# In place manipulation of Linked List
**Requires no extra space to modify linked-list**
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