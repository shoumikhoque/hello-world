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
### 1. Repeated DNA Sequence @ [Leetcode:Medium](https://leetcode.com/problems/repeated-dna-sequences/description/)
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
### 2. Find max in sliding window @ [Leetcode: Hard](https://leetcode.com/problems/sliding-window-maximum/description/)
Given an integer list, `nums`, find the maximum values in all the contiguous sub-arrays (windows) of size `w`.
#### Brute force 
1. take each sliding window  O(n-w+1)
2. for each window, calculate the max value by traversing window from start to end -> `time O(w)`
#### Complexity
`Time: O(n*w)`
`Space: O(w)`
#### Using deque : [Solution](find_max_sliding_window.py)
1. if list size is 1 , return list as `output`
2. create a `deque` to store indices of the candidate maximum of each window
2. process the first `w` elements . 
3. for each element, perform `clean-up` step , removing the indices of the elements from the 
deque whose values are smaller than or equal to the value of the new element . 
4. append the index of the new element at the back of the deque. 
5. append the element whose index is present at the front of deque to the output list as the maximum of the first window
6. repeat step 3 for the rest of the elements
7. additionally , in each iteration , before appending index to the current element to the deque, 
check if the first index of the deque has fallen out of the bound of current window
8. return `output` list
#### Complexity
[Complexity Analysis](https://www.educative.io/module/page/8q5JgjuQREjpzD9gq/10370001/4803867293515776/4961871808692224#Time-complexity)

### 3. Minimum Window Subsequence @ [Leetcode premium](https://leetcode.com/problems/minimum-window-subsequence/description/)
Given two strings, `str1` and `str2`, find the shortest substring in str1 such that str2 is a subsequence of that substring.

A `SubString` is defined as a contiguous sequence of characters within a string. <br>
A `SubSequence` is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.
#### using sliding window : **[Solution](minimum_window_subsequence.py)**
1. iterate through `str1` to locate potential window that contains all the characters of `str2` in their order of appearance.
2. backtrack through the characters of `str1` from this end position until found all the characters of `str2` in reverse order.
   this helps locate potential start of the smallest subsequence.
3. update the minimum window subsequence if the current window is smaller than the shortest subsequence found so far.
4. repeat the process , starting every time from the second character of the current window, until the end of `str1` has been reached
5. return minimum window subsequence
#### Complexity
`time:O(n*m)
space: O(1)`
### 4. Minimum window Substring @ [Leetcode:Hard](https://leetcode.com/problems/minimum-window-substring/description/)
Given two strings, `s` and `pattern`, find the minimum window substring in s, which has the following properties:
 - It is the shortest substring of s that includes all the characters present in `pattern`.
 - It must contain at least the same frequency of each character as in `pattern`.
 - The order of the characters does not matter here.
 - Strings s and t consist of uppercase and lowercase English characters.
 - `1 <=s.length, t.length <=10^3`

#### Using sliding window and hashmap : [Solution](minimum_window_substring.py)
1. if `pattern` is empty then return empty string
2. define two hashmaps , `req_count` to store the required count of each char in `pattern` and `window` to store char count of the current window
3. iterate over the string to find a window with all chars in `pattern` the help of hashmaps 
4. if the length is less than previous `res_len` , then store the length and substring as `result` 
5. decrease the window from left side such that it at least 1 char is missing in the window
6. again start traversing the string and add chars in window , repeat step 3
7. return the `result` string after iterating the whole string 

#### Complexity
`time:O(n+m) for traversing the whole string twice and traversing window
space: O(n) for hashmap`
### 5. Longest Substring Without Repeating Characters @ [Leetcode:Medium](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
Given a string `input_str`, return the length of the longest substring without repeating characters.
#### Constraints:
`1 <= input_str.length <= 10^5` <br>
`input_str` consists of English letters, digits, symbols, and spaces.

#### Using sliding window: [Solution](longest_substring_without_repeating_chars.py)
1. Init: `window_start`,  a hashmap to store `last_found_index` of every characters.
2. traverse through the string
3. if a char doesn't exist in the hashmap, just add it 
4. if a char already exist , then find the length of the current window [window_start,current_index], update final length
using max function
5. return length

#### Complexity
`time:O(n) for traversing the whole string
space: O(26)~)(1) for hashmap`
### 6. Longest Repeating Character Replacement @ [Leetcode:Medium](https://leetcode.com/problems/longest-repeating-character-replacement/description/)

### 7. Minimum Size Subarray Sum @ [Leetcode:Medium](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

### 8. Best Time to Buy and Sell Stock @ [Leetcode:Easy](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
