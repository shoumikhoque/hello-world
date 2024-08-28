def max_power_of_two_less_than_number(n):
    i=1
    while 2*i<=n:
        i=2*i
    return i
def min_tiles(m,n,dp:dict):
    # base case
    if m==0 or n==0:
        return 0
    if str(m)+','+str(n) in dp :
        return dp[str(m)+','+str(n)]
    elif str(n)+','+str(m) in dp:
        return dp[str(n)+','+str(m)]
    #recursive case
    k=max_power_of_two_less_than_number(min(m,n))
    if k==m:
        dp[str(m)+','+str(n)]= (n//k)+min_tiles(n%k,m,dp)
    elif k==n:
        dp[str(m)+','+str(n)]= (m//k) + min_tiles(m%k,n,dp)
    else:
        dp[str(m)+','+str(n)]= 1 + min_tiles(max(m-k,n-k),min(m,n),dp)+ min_tiles(min(m-k,n-k),k,dp)
    return dp[str(m)+','+str(n)]
if __name__ == '__main__':
    inp=input().split(' ')
    dp=dict()
    print(min_tiles(int(inp[0]),int(inp[1]),dp))