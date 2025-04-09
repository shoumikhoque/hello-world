def solve(s, words):
    dp={}
    def calc(i):
        if i>=len(s):
            return True
        if i in dp:
            return dp[i]
        dp[i]=False
        for w in words:
            if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                dp[i]=True and calc(i+len(w))
        return dp[i]

    return calc(0)
def solve_table(s,words):
    dp=[False]*(len(s))+[True]
    for i in range(len(s)-1,-1,-1):
        for w in words:
            if i+len(w)<=len(s) and s[i: i+len(w)]==w:
                dp[i]=dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]

if __name__ == '__main__':
    target = "abcd"
    wordDict = ["a","abc","b","cd"]
    print(solve(target,wordDict))