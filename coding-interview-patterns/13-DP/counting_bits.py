def solve(n):
    temp=1
    ans=[0]
    for i in range(1, n+1):
        if i==temp*2:
            temp*=2
            ans.append(1)
        else:
            ans.append(1+ans[i-temp])
    return ans


if __name__ == '__main__':
    n=5
    print(solve(n))