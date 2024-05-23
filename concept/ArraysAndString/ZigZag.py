def zigzag(s, level):
    k=0
    ans=['']*level
    while k<len(s):

        for i in range(0,level):
            for j in range(0,level):
                if k==len(s):
                    break
                if i==j:
                    if (k//level)%2==0 :
                        ans[i] += s[k]
                    else:
                        if k<level:
                            ans[level-i-1]+=s[k]
                        else:
                            ans[level-i-2]+=s[k]
                    k+=1
                else:
                    ans[i]+='-'


    for i in ans:
        print(i)

if __name__ == '__main__':
    s="abcdefghijklmnopqrstjdhsajkdhsajkdhsjkadhsjkadui"
    level=3
    zigzag(s, level)
