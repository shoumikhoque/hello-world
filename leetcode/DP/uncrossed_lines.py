def solve(nums1, nums2):
    dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
    for i in range(len(nums1)-1,-1,-1):
        for j in range(len(nums2)-1,-1,-1):
            if nums1[i]==nums2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]

if __name__ == '__main__':
    nums1=[1,4,2]
    nums2=[1,2,4]
    print(solve(nums1,nums2))