def minimum_substring(s, pattern):
    if pattern =='':
        return pattern
    req_count=dict()
    window=dict()
    for i in pattern:
        req_count[i]=1+req_count.get(i,0)
        window[i]=0
    current,required=0,len(req_count)
    res,res_len=[-1,-1],float('inf')
    left=0
    for right in range(len(s)):
        c=s[right]
        if c in pattern:
            window[c]=1+window.get(c,0)
        if c in req_count and window[c]==req_count[c]:
            current+=1
        while current==required:
            if(right-left+1)<res_len:
                res=[left,right]
                res_len=(right-left+1)
            if s[left] in pattern:
                window[s[left]]-=1
                if s[left] in req_count and window[s[left]]<req_count[s[left]]:
                    current-=1
                left+=1
    left,right=res
    return s[left:right+1] if res_len !=float('inf') else ""




if __name__ == '__main__':
    s='ABDOEDECOBE'
    pattern='BC'
    print(minimum_substring(s,pattern))