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
`Time: O(c×3l), where c is the number of cells and l is the length of the word we are searching for
Space: O(l), where l is the length of the word`

### 2. House Robber III @ [Leetcode:Medium](https://leetcode.com/problems/house-robber-iii/description/)