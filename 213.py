# 198. House Robber
from typing import List

def robHouse( nums: List[int],pos,dp:List[int]) -> List[int]:
    if dp[pos]>=0:
        return dp
    n=len(nums)
    if pos==n-1 :
        dp[pos]=arr[pos]
        return dp
    for i in range(pos,n):
        temp=0
        for j in range(i+2,n):
            temp=max(temp,robHouse(nums,j,dp)[j])
        dp[i]=arr[i]+temp
    return dp




if __name__ == '__main__':
    print("hello")
    arr=[0]
    n=len(arr)
    if n==1:
         print(arr[0])
    dp1=[-1]*(n)
    ans1 = robHouse(arr[:-1], 0, dp1)
    dp2 = [-1] * (n - 1)
    ans2 = robHouse(arr[1:], 0, dp2)

    print(max(dp1[0],dp1[1],dp2[0],dp2[1]))
