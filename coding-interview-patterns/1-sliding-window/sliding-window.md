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