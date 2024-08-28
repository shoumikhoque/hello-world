## Task 1
**Code in [two_sum.py](two_sum.py)**
### Solution 1: Brute Force
Checking for each value pair from nums  in a nested loop
````
Time Complexity: O(n^2)
Space Complexity: O(1)
````

### Solution 2: Using Map
- Create a dictionary to store each num's index with target-num
- Traverse nums -> return ans if the value exists in dictionary as key
````
Time Complexity: O(n)
Space Complexity: O(n)
````


### Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Use of C++ or JavaScript is preferred.
## Constraints
```
 2 <= nums.length <= 10^4
 -10^9 <= nums[i] <= 10^9
 -10^9 <= target <= 10^9
```
Only one valid answer exists.

### Example 1
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```
**Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].**

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```