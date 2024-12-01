## Task 1
**Code in [maximum_unit.py](maximum_unit.py)**

### Solution : Simple greedy using sort

````
Time Complexity: O(nlogn) 
Space Complexity: O(1)
````

### Problem Statement
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [number_of_boxes_i, number_of_unit_per_box_i]:

Number_of_boxes_i is the number of boxes of type i.
Number_of_unit_per_box_i is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
Mention the time and space complexity of your solution.
## Constraints
`1 <= boxTypes.length <= 1000
1 <= number_of_boxes_i, number_of_unit_per_box_i<= 1000
1 <= truckSize <= 10^6`

### Example 1
```
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
```
### Example 2:
```

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
Explanation: There are:
- 5 boxes of the first type that contain 10 units.
- 3 boxes of the second type that contain 9 units each.
- 2 boxes of the third type that contain 7 units each.
The total number of units will be = (5 * 10) + (3 * 9) + (2 * 7) = 91.
```