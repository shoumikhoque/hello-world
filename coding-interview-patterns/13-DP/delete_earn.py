def solve(nums):
    mapper = {}
    for i in nums:
        mapper[i] =mapper.get(i, 0) + 1
    nums=list(mapper.keys())
    nums.sort(reverse=True)
    dp=[-1]*(len(nums)+1)
    def calc(index):
        if index==len(nums):
            return 0
        if dp [index]==-1:
            key=nums[index]
            if index+1<len(nums) and nums[index]-1==nums[index+1]:
                dp[index]=max(key*mapper[key]+calc(index+2),calc(index+1))
            else:
                dp[index]=key*mapper[key]+calc(index+1)
        return dp[index]
    return calc(0)


def solve_table(nums):
    mapper = {}
    for i in nums:
        mapper[i] = mapper.get(i, 0) + 1
    nums = list(mapper.keys())
    nums.sort()
    dp = [nums[0] * mapper[nums[0]]]+ [0] * (len(nums) )

    for index in range(1,len(nums)):
        key = nums[index]
        dp[index] = key * mapper[key]
        if key - 1 == nums[index - 1]:
            if index-2 >=0:
                dp[index]+=dp[index-2]
            dp[index] = max(dp[index], dp[index-1])
        else:
            dp[index]+=dp[index-1]
    return dp[len(nums)-1]


if __name__ == '__main__':
    nums=[2,2,3,3,3,4]
    print(solve_table(nums))