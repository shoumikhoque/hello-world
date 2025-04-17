def solve(arr, diff):
    dp={}
    ans=1
    for num in arr:
        if num-diff in dp:
            dp[num]=dp[num-diff] +1
        else:
            dp[num]=1
        ans=max(ans,dp[num])
    return ans
if __name__ == '__main__':
    arr = [1,3,5,7]
    diff= 1
    print(solve(arr,diff))