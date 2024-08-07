## Task 1
**Code in [shuffled_string.py](shuffled_string.py)**


### Solution 1: single loop
- create new `ans` array with length of `s`
- traverse the string and replace every character in `ans` according to `indices array`
````
Time Complexity: O(n)
Space Complexity: O(n)
````


### Problem Statement
Write a function that does the following task.
You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to `indices[i]` 
in the shuffled string. Return the shuffled string.
Also, mention the Time and Space Complexity of your solution
## Constraints
```
s.length == indices.length == n
1 <= n <= 100
0 <= indices[i] < n
```
`s` consists of only lowercase English letters.
All values of indices are unique.

### Example 1
```
Input: s = "mamacode", indices = [4,5,6,7,0,1,2,3]
Output: "codemama"
```
**Explanation: As shown, `mamacode` becomes `codemama` after shuffling.**

### Example 2:
```
Input: s = "dosta", indices = [4,0,1,2,3]
Output: "ostad"
```
**Explanation: After shuffling, each character remains in its position.**
### Example 3:
```
Input: s = "abc", indices = [1,0,2]
Output: "bac"
```
**Explanation: After shuffling, each character remains in its position.**