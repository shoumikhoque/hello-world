def solve(s, t):
    cache={}
    def calc(i,j):
        if j==len(t):
            return 1
        if i==len(s):
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        if s[i]==t[j]:
            cache[(i, j)] = calc(i+1,j+1)+calc(i+1,j)
        else:
            cache[(i, j)] = calc(i+1,j)
        return cache[(i, j)]
    return calc(0,0)
def solve_table(s, t):
    return


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    print(solve(s,t))