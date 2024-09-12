def minimum_substring(s, pattern):
    if pattern =='':
        return pattern
    req_count=dict()
    window=dict()
    for i in pattern:
        req_count[i]=1+req_count.get(i,0)

    have,need=0,len(req_count)
    res,res_len=[-1,-1],float('inf')
    left=0
    for right in range(len(s)):
        c=s[right]
        window[c]=1+window.get(c,0)
        if c in req_count and window[c]==req_count[c]:
            have+=1
        while have==need:
            if(right-left+1)<res_len:
                res=[left,right]
                res_len=(right-left+1)
            left_char = s[left]


            if left_char in pattern:
                window[left_char]-=1
            if left_char in req_count and window[left_char]<req_count[left_char]:
                have-=1
            left+=1
    left,right=res
    return s[left:right+1] if res_len !=float('inf') else ""
if __name__ == '__main__':
    s='ADOBECODEBANC'
    pattern='ABC'
    print(minimum_substring(s,pattern))