## Task 1
**Code in [first_occurance_in_string.py](first_occurance_in_string.py)**
### Solution 1: slice
- traverse the haystack string form beginning to n -m+1 where n=len(haystack),m=len(needle)
- take a slice of length m from haystack and compare with needle
````
Time Complexity: O(n*m)
Space Complexity: O(1)
````
### Problem Statement
Write a function that does the following task.
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or `-1` if needle is not part of haystack.
Also, mention the Time and Space Complexity of your solution
## Constraints
```
1 <= haystack.length, needle.length <= 10^4
```
haystack and needle consist of only lowercase English characters.

### Example 1
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
```
**Explanation:  `sad` occurs at index `0` and `6`. The first occurrence is at index `0`, so we return `0`.**

### Example 2:
```
Input: haystack = "codemama", needle = "ostad"
Output: -1
```