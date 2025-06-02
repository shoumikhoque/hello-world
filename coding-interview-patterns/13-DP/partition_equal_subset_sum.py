def solve_bottom_up(nums):
    total=sum(nums)
    if total %2==1:
        return False
    total=total//2
    dp = [False] * (total + 1)
    dp[0] = True

    for n in nums:
        for target in range(total, n - 1, -1):
            if dp[target]:
                continue
            if dp[target - n]:
                dp[target] = True
            if dp[-1]:
                return True
    return False

if __name__ == '__main__':
    nums=[100,4,6]
    print(solve_bottom_up(nums))