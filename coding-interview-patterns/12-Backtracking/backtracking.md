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
### 2. Word Search @ [Leetcode:Medium](https://leetcode.com/problems/word-search)
````
input: m*n board with chars, word to search
output: true/false if the word exists in the board
````
#### Steps : [Solution](word_search.py)
1. start traversing the grid from `board`[0][0] for `word`[0] using `dfs`
2. check if the char in position of the `board` matches the char in `word` ,
   1. if matches then add it to a set `path` and traverse the adjacent 4 chars by calling the same method
   2. if not return false 
3. if dfs search returns false , then start the word search from the next char of the board until the whole board 
   is searched or the word is found
#### Complexity
```
Time: O(c×3l), where c is the number of cells and l is the length of the word we are searching for
Space: O(l), where l is the length of the word
```

### 3. House Robber III @ [Leetcode:Medium](https://leetcode.com/problems/house-robber-iii/description/)
````
input: binary tree as array
output: max profit value
````
#### [Solution](house_robber_3.py)
1. if the tree is empty return [0,0]
2. otherwise , recursively calculate the max amount of money that can be robbed from left and  right sub-tree 
3. calculate the amount of that can be robbed including root and excluding root 
   1. for including root -> root.val + left_subtree_without_root +right_subtree_without_root
   2. for excluding root -> max(with , without root of left sub-tree) +max(with , without root of right sub-tree)
4. return the max of these two values
```
Time: O(n)
Space: O(n), 
```
### 4 .Restore IP Addresses [Leetcode:Medium](https://leetcode.com/problems/restore-ip-addresses/description/)
````
input: The input string s consists of digits only where 4≤ s.length ≤12
output: list of ip addresses
````
#### [Solution](restore_ip_address.py)
1. take 4 segments using backtrack and place dots among them
2. take either 1/2/3 digits for every possible segments where no segment starts with 0
3. add every valid ip address to the result array when 4 segments are found and end of the string is reached
```
Time: O(3^4)
Space: O(n), for string concatenation 
```