def recursive_division(n,dp):
    if n==0:
        dp[0]=1
        return dp[n]
    elif n in dp:
        return dp[n]

    dp[n]=recursive_division(n//2,dp)+recursive_division(n//3,dp)
    print(len(dp))
    return dp[n]


if __name__ == '__main__':
    n=9999999999
    dp=[0]*(n//2)
    print(recursive_division(n,dp))