def solve(s):
    dp={}
    def calc(left, right):
        if left==right:
            return 1
        if left>right:
            return 0
        if (left,right) in dp:
            return dp[(left,right)]

        if s[left]==s[right]:
            dp[(left,right)]= 2+calc(left+1,right-1)
        else:
            dp[(left,right)]= max(calc(left+1,right),calc(left,right-1))
        return dp[(left,right)]
    return calc(0,len(s)-1)
def solve_table(s):
    dp=[]


if __name__ == '__main__':
    s='cbabd'
    print(solve(s))