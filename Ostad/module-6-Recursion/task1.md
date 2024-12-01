## Task 1
**Code in [palindrome_recursive.py](palindrome_recursive.py)**

### Solution 1: simple recursion
- return True if the length of s is less than 2
- if the 1st and last character of `s` is same ,
then call the function again without the 1st and last character
- else return False
````
Time Complexity: O(n)
Space Complexity: O(n)
````

### Problem Statement
Write a function that does the following task.<br>
Given a string s, return true if it is a palindrome, or false otherwise.
The input string is given as a string ‘s’.<br>
You must use **Recursion** to solve the problem. <br>
Also, mention the Time and Space Complexity of your solution.
## Constraints
```
1 <= s.length <= 10^5
```
### Example 1
```
Input: s = "madam"
Output: true
```
### Example 2:
```
Input: s = "adam"
Output: false
```
### Example 3:
```
Input: s = "tenet"
Output: true
```
