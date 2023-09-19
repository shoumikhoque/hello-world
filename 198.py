def robHouse(self, nums: List[int], pos, dp: List[int]) -> List[int]:
    if dp[pos] >= 0:
        return dp
    n = len(nums)
    if pos == n - 1:
        dp[pos] = nums[pos]
        return dp
    for i in range(pos, n):
        temp = 0
        for j in range(i + 2, n):
            temp = max(temp, self.robHouse(nums, j, dp)[j])
        dp[i] = nums[i] + temp
    return dp


def rob(self, nums: List[int]) -> int:
    dp = [-1] * len(nums)
    ans = self.robHouse(nums, 0, dp)
    print(ans)
    if len(ans) >= 2:
        return max(ans[0], ans[1])
    else:
        return ans[0]