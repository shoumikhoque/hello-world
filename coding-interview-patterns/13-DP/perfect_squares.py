def getSquares(n):
    i=1
    ans=[]
    while i*i<=n:
        ans.append(i*i)
        i+=1
    return ans
def perfect_squares(n):
    sq=getSquares(n)
    dp=[n+1]*(n+1)
    def calc(target):
        if target<=0:
            return 0
        if dp[target]!=n+1:
            return dp[target]
        for i in sq:
            dp[target]=min(dp[target],1+calc(target-i))
        return dp[target]
    return calc(n)


if __name__ == '__main__':
    n=12
    print(perfect_squares(n))