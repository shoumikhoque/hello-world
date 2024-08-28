def max_frequency(s):
    dp=dict()
    for i in s:
        if i in dp:
            dp[i]+=1
        else:
            dp[i]=1
    max_count=0
    max_char=''
    for k,v in dp.items():
        if v== max_count and k<max_char:
            max_count = v
            max_char = k
        if v>max_count:
            max_count=v
            max_char=k
    return max_char+' '+str(max_count)

if __name__ == '__main__':
    s=input()
    print(s.upper())