def solve(s1, s2):
    if s1==s2:
        return len(s1)
    dp={}
    def calc(i,j):
        if i>=len(s1) or j>=len(s2):
            return 0
        if (i,j) in dp :
            return dp[(i,j)]
        if s1[i]==s2[j]:
            dp[(i,j)]= 1+calc(i+1,j+1)
        else:
            dp[(i,j)]= max(calc(i,j+1),calc(i+1,j))
        return dp[(i,j)]
    return calc(0,0)
def solve_table(s1,s2):
    if s1==s2:
        return len(s1)
    n1=len(s1)
    n2=len(s2)
    dp=[[0]*(n2+1) for _ in range(n1+1)]
    for i in range(n1-1,-1,-1):
        for j in range(n2-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    return dp[0][0]

if __name__ == '__main__':
    s1='abcde'
    s2='ace'
    print(solve_table(s1,s2))