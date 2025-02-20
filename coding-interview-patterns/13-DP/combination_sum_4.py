def all_combinations_memo(nums, target):
    if target==0:
        return 1
    dp=[0]+[0]*(target)
    def calc(sum):
        if sum==0:
            return 1
        if sum<0 :
            return 0
        if dp[sum]==0:
            for num in nums:
                if num<=sum:
                    dp[sum]+=calc(sum-num)
        return dp[sum]
    return calc(target)
def all_combination_table(nums,target):
    if target==0:
        return 1
    if target<0:
        return 0
    dp=[1]+[0]*(target)
    for sum in range(1,target+1):
        for num in nums:
            if num <= sum:
                dp[sum] += dp[sum-num]
    return dp[target]

if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(all_combination_table(nums,target))