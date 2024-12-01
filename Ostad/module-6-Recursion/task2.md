## Task 1
**Code in [multiplication_recursive.py](multiplication_recursive.py)**
### Solution 1: 
- add the larger number with the returned value of recursive function called with decreasing the smaller number by 1
````
Time Complexity: O(min(a,b))
Space Complexity: O(min(a,b))
````
### Problem Statement
Write a function that does the following task.<br>
Write a recursive function to multiply given two positive integers ‘a’ and ‘b’
without using the * operator (multiplication operator).
You can only use + operator (addition operator) and - operator (subtraction operator). <br>
Also, mention the Time and Space Complexity of your solution
## Constraints
```
1 <= a, b <= 10^5
```
### Example 1
```
Input: a = 4, b = 5
Output: 20
```
**Explanation:  `sad` occurs at index `0` and `6`. The first occurrence is at index `0`, so we return `0`.**

### Example 2:
```
Input: a = 3, b = 3
Output: 9
```
### Example 3:
```
Input: a = 0, b = 2
Output: 0
```