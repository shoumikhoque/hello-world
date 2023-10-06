def calc( s: str,n,dp) :
    if n == 0 or n == 1:
        dp[n] = 1
        return dp[n]
    if s[0]=="0":
        dp[n]=0
        return dp[n]
    if dp[n]>-1:
        return dp[n]
    elif s[0:2]<="26":
        dp[n]=calc(s[1:],n-1,dp)+calc(s[2:],n-2,dp)
    else :
        dp[n]=calc(s[1:],n-1,dp)
    return dp[n]



if __name__ == '__main__':
    nums="121506"
    n=len(nums)
    dp=[-1]*(n+1)
    print(calc( nums,n,dp))
