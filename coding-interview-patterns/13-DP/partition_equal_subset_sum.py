def solve_bottom_up(nums):
    total=sum(nums)
    if total %2==1:
        return False
    total=total//2
    nums.sort()
    dp= [[True]* len(nums)] + [[False]*len(nums) for i in range(total)]
    for target in range(1,total+1):
        for i in range(len(nums)):
            if nums[i]==target:
                dp[target][i]=True
                continue
            if i>0:
                dp[target][i]= dp[target][i-1] or (target-nums[i]>=0 and dp[target-nums[i]][i-1])
    return dp[total][len(nums)-1]
if __name__ == '__main__':
    nums=[100,4,6]
    print(solve_bottom_up(nums))