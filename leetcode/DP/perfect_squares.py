def getSquares(n):
    i=1
    ans=[]
    while i*i<=n:
        ans.append(i*i)
        i+=1
    return ans
def perfect_squares_memoize(n):
    sq=getSquares(n)
    dp=[0]+[n+1]*(n)
    def calc(target):
        if target<=0:
            return 0
        if dp[target]!=n+1:
            return dp[target]
        for i in sq :
            if i<=target:
                dp[target]=min(dp[target],1+calc(target-i))
        return dp[target]
    return calc(n)
def perfect_squares_tabulation(n):
    sq=getSquares(n)
    dp= [0] + [n + 1] * (n)
    if n <= 0:
        return 0
    for sum in range(1, n + 1):
        for i in sq:
            if i <= sum:
                dp[sum] = min(dp[sum], 1 + dp[sum - i])
    return dp[n]


if __name__ == '__main__':
    n=12
    print(perfect_squares_tabulation(n))