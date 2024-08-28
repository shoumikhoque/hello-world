## Task 1
**Code in [remove_duplicate.py](remove_duplicate.py)**

### Solution : Using Stack
1. init a stack `st` and traverse through `s`
2. for each element `s[i]` in s , if stack is not empty and stack top is equal to` s[i]`, then pop stack
3. otherwise push `s[i]` to stack
4. traverse the stack and store the element in stack in reverse order in a string `s`
5. return `s `

````
Time Complexity: O(n)
Space Complexity: O(n)
````

### Problem Statement
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent 
and equal letters and removing them.
<br>
We repeatedly make duplicate removals on s until we no longer can. Return the final string after all such duplicate 
removals have been made. It can be proven that the answer is unique.
## Constraints
```
1 <= s.length <= 10^5
s consists of lowercase English letters.
```
### Example 1
```
Input: s = "abbaca"
Output: "ca"
```
**Explanation**:<br>
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
### Example 2:
```
Input: s = "azxxzy"
Output: "ay"
```
**Explanation**:<br>
For example, in "azxxzy" we could remove "xx" since the letters are adjacent and equal, and this is the only possible move.
The result of this move is that the string is "azzy", of which only "zz" is possible, so the final string is "ay".

