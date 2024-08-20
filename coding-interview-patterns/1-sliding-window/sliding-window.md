# Sliding Window
## Introduction

Used for efficiently solving subarray or substring problems.
### Pattern
1. **Contiguous data**: The input data is stored in a contiguous manner, such as an array or string.

3. **Processing subsets of elements**: The problem requires repeated computations on a contiguous subset of data elements
(a subarray or a substring), such that the window moves across the input array from one end to the other. The size of the
window may be fixed or variable, depending on the requirements of the problem.

3. **Efficient computation time complexity**: The computations performed every time the window moves take constant or 
relatively smaller time.

### Real World Problems
1. **Telecommunications**: Find the maximum number of users connected to a cellular network’s base station in every 
k-millisecond sliding window.

2. **Video streaming**: Given a stream of numbers representing the number of buffering events in a given user session, 
calculate the median number of buffering events in each one-minute interval.

3. **Social media content mining**: Given the lists of topics that two users have posted about, find the shortest sequence
of posts by one user that includes all the topics that the other user has posted about.

## Practice Problems
### 1. Repeated DNA Sequence
Given a string, `dna`, that represents a DNA subsequence, and a number `k`, return all the contiguous 
subsequences (substrings) of length `k` that occur more than once in the string. 
#### Brute force Steps
1. iterate the whole dna to get substrings with length k
2. for each substring add it to a set `substring_set` if this substring is not already present in that set
3. if a substring is already present in `substring_set` , then add it to the `output_set`.
4. repeat until end of string and return `output_set`
#### Complexity
`Time: O((n-k)*k)`<br>
This is because we iterate over `(n−k+1)` substrings of length `k`, and at each iteration, the time taken to generate
a k-length substring is `O(k)`.
`Space: O((n-k)*k)`<br>
our set can contain `(n−k+1)` elements, and at each iteration of the traversal, we are allocating memory to generate
a new k-length substring.
#### Using Robin Karp with Rolling hash : [Solution](repeated_dna_sequence.py)
1. traverse the string using sliding window 
2. compute the hash of the current k length substring 
   1. use this polynomial method for hashing: <br>
   `H=c1*a^k−1+c2*a^k−2+...+ci*a^k−i+...+ck−1*a1+ck*a0`
   2. we can also use the [modulus version](https://www.geeksforgeeks.org/introduction-to-rolling-hash-data-structures-and-algorithms/)
   to limit large hash_value  
   3. for calculating current window rolling hash :
      1. we need to take the previous window hash , subtract the hash of left most character
      2. multiply this result with the base_value (in this case 4) and add the hash of the new character of the window
   
3. if the hash is present in `substring_set` then we add this substring to `output_set`
4. otherwise add it to `substring_set` 
5. repeat until end of string and return `output_set`
#### Complexity

`Average time O(n)`

- Time taken to populate the numbers array: O(n).
- Time taken to traverse all the kk-length substrings: O(n−k+1).
- Time taken to calculate the hash value of a kk-length substring: O(1).

`worst Time: O((n-k)*k)  ` case:  `“AAAAAAAA”`

`Space: O(n)`

- Space occupied by the mapping hash map: O(1).
- Space occupied by the numbers array: O(n).
- Space occupied by the hash_set set: O(n−k+1).
