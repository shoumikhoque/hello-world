


def min_edit_dist_bottom_up(w1, w2):
    dp=[[float("inf")]* (len(w2)+1) for i in range(len(w1)+1)]
    for j in range(len(w2)+1):
        dp[len(w1)][j]=len(w2)-j
    for i in range(len(w1)+1):
        dp[i][len(w2)]=len(w1)-i

    for i in range(len(w1)-1,-1,-1):
        for j in range(len(w2)-1,-1,-1):
            if w1[i]==w2[j]:
                dp[i][j]=dp[i+1][j+1]
            else:
                dp[i][j]=1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])

    return dp[0][0]


def min_edit_dist_top_down(w1, w2):
    dp = [[float("inf")] * (len(w2) + 1) for i in range(len(w1) + 1)]
    def dfs(i,j):
        if i==0:
            return j
        if j==0:
            return i
        if dp[i][j] !=float("inf"):
            return dp[i][j]
        if w1[i ]==w2[j ]:
            dp[i][j ]=dfs( i - 1, j - 1)
        else:
            dp[i][j]= 1 + min(dfs( i - 1, j),dfs(i, j - 1),dfs( i - 1, j - 1))
        return dp[i ][j ]
    return dfs(len(w1)-1,len(w2)-1)
if __name__ == '__main__':
    w1 = "horse"
    w2 = "ros"

    # print(min_edit_dist_bottom_up(w1, w2))
    print(min_edit_dist_top_down(w1, w2))