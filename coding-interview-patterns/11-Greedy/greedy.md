





### 6. Maximum Length of Pair Chain
````
input:  array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
output: the length longest chain 
````

#### Solution 
1. sort the pairs according to the end value
2. keep end value of the first pair for future comparison
3. for each pair p  from the 2nd to last of the list:
    1. if the first value of p is greater than the previous end value then take this pair and increment result and end value accordingly
4. return length of the longest chain:
#### complexity
`Time:O(n+nLogn)
Space:O(1)`