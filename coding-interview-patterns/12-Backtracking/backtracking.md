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
### 5 .Flood Fill [Leetcode:Easy](https://leetcode.com/problems/flood-fill/description/)
````
input: 2D array[n*m] as image , co-ordinate of starting point and target color number
output: 2D array as image , after changing color
````
#### [Solution](flood_fill.py)
1. traverse in 4 directions from starting point using DFS
2. if color is matched with the starting pixel's color then update color 

```
Time: O(n*m)
Space: O(n*m), 
```
### 6. Sudoku Solver [Leetcode:Hard](https://leetcode.com/problems/sudoku-solver/description/)
````
input: 2D array[9*9] as board ,numbers present existing numbers, '.' presents empty position
output: 2D array as board, solved sudoku
````
#### [Solution](sudoku_solver.py)
1. start iterating the board from the top left cell until we reach the first free cell
2. one by one, place all numbers between 1 and 9 in the current cell, if the number isn't already present in the current
   row , column and 3x3 sub box.
3. write down the number that is now present in the current row , column and sub box
4. if we reach the last cell[8,8], that means we have solved the sudoku
5. else we move onto next cell
6. Backtrack if the solution is not yet present and remove the last number from the cell. (clean up process)

```
Time: O(n*m)
Space: O(n*m), 
```
### 7. MatchSticks to Square [Leetcode:Medium](https://leetcode.com/problems/matchsticks-to-square/)
````
input: list of numbers representing lengths of matchsticks
output: if the matchsticks can form a valid Square
````
#### [Solution](sudoku_solver.py)
1. check if the array len is less than 4 or sum(array) is not dividable by 4 or tha maximum length of a stick is larger 
   than the side of square. return false for all these cases.
2. sort the matches
3. for each of the matchsticks use backtracking to check if that matchstick can be used to any of the 4 sides
4. if a side + matchstick is <= target len of a side then use that matchstick and call next matchstick 
5. if all the matchsticks can be used then a square can be made

```
Time: O(4^n+nlog(n))
Space: O(n), 
```
