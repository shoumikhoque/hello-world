## Task 1
**Code in [kth_largest_element.py](kth_largest_element.py)**

### Solution : using heap
1. create a min heap 
2. traverse the array and push elements to the heap
3. if the size exceeds k , then remove the top
4. after traversal , return min heap's top element
````
Time Complexity: O(nlogk)
Space Complexity: O(k) for heap space
````

### Problem Statement
Write a function that does the following task.<br>
Given an integer array nums and an integer k, return the kth largest element in the array.
You must solve the problem in O(nlog(n)) time complexity and with the smallest space complexity possible. You should not use any built-in sorting functions.

Discuss which sorting algorithm you are using and why it is best fit for this problem.
## Constraints
```
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
```
### Example 1
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

### Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```