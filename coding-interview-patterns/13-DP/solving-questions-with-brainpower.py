def solve_memo(questions):
    if len(questions)==0:
        return 0
    cache=[-1]*(len(questions))
    def calc(pos):
        if pos>=len(questions):
            return 0
        if cache[pos]==-1:
            cache[pos]= max(questions[pos][0]+calc(pos+questions[pos][1]+1),calc(pos+1))
        return cache[pos]
    return calc(0)
def solve_table(questions):
    if len(questions)==0:
        return 0
    dp=[0]*(len(questions))
    for i in range(len(questions)-1,-1,-1):
        dp[i]=questions[i][0]+( dp[i+1+questions[i][1]] if i+1+questions[i][1] <len(questions) else 0 )
        if i+1<len(questions):
            dp[i]=max(dp[i],dp[i+1])
    return max(dp)

if __name__ == '__main__':
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    print(solve_table(questions))