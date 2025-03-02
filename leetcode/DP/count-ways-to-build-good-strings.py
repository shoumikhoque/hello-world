def count(low, high, zero, one):
    dp={}
    mod =10**9+7
    def calc(length):
        if length>high:
            return 0
        if length in dp:
            return dp[length]
        dp[length]=1 if length>=low else 0
        dp[length]+=calc(length+zero)
        dp[length]+=calc(length+one)
        return dp[length]% mod
    return calc(0)


def count_tabulation(low, high, zero, one):
    dp=[1]+[0]*(high)
    mod = 10 ** 9 + 7
    for i in range(1,high+1):
        dp[i]=(dp[i-zero]+dp[i-one]) % mod
    return sum(dp[i] for i in range(low, high+1))% mod


if __name__ == '__main__':
    low = 2
    high =3
    zero = 1
    one = 2
    print(count_tabulation(low,high,zero,one))