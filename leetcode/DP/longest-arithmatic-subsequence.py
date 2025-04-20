def solve(nums):
    n = len(nums)
    if n <= 2:
        return n
    dp = [{} for _ in range(n)]
    ans = 2
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff]=dp[j].get(diff, 1) + 1
            ans = max(ans, dp[i][diff])
    return ans

# [40,26,16,57,39,52,9,37,53,18,52,56,33,52,23,46,25,51,23,16,49,18,27,5,29,7,28,31,19,19,47,8,8,27,28,36,24,52,52,15,42,27,47,33,24,60,44,60,60,43,37,54,5,30,6,57,28,40,0,10,0,37,0,21,49,2,55,40,37,4,3,52,37,27,39,51,27,37,22,9,48,25,25,60,17,49,41,54,58,29]

if __name__ == '__main__':
    nums = [20,1,15,3,10,5,8]
    print(solve(nums))
