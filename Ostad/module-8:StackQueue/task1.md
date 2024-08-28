## Task 1
**Code in [balance_parentheses.py](balance_parentheses.py)**

### Solution : using stack
1. traverse through `s` and push every opening braces in `s[i]` into a stack
2. if a closing brace is found
   1.  stack has a top with opening brace similar to `s[i] ` then pop from stack.
   2. otherwise return false
3. If `s` is traversed fully and stack is empty after traversal then return `true`.

````
Time Complexity: O(n)
Space Complexity: O(n)
````

### Problem Statement
Write a function that does the following task.<br>
Given a string s containing just the characters `'(', ')', '{', '}', '[' and ']'`. determine if the input string is valid.
<br>
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
<br>
Also, mention the Time and Space Complexity of your solution.
## Constraints
```
1 <= s.length <= 10^4
s consists of brackets only '()[]{}'.
```
### Example 1
```
Input: s = "()"
Output: true
```

### Example 2:
```
Input: s = "()[]{}"
Output: true
```

### Example 3:
```
Input: s = "(]"
Output: false
```
### Example 4:
```
Input: s = "{()}"
Output: true
```
### Example 5:
```
Input: s = "{(})"
Output: false
```