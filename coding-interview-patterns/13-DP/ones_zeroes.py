def convert_to_tuples(strs):
    for i in range(len(strs)):
        ones=0
        zeroes=0
        for char in strs[i]:
            zeroes+=(char=='0')
            ones+=(char=='1')
        strs[i]=(zeroes,ones)
    return strs


def max_subset_size_memoize(strs, m, n):
    arr=convert_to_tuples(strs)
    cache={}
    def calc(target,pos):
        if pos==len(strs):
            return 0
        zeroes, ones=target[0],target[1]
        if zeroes<1 and ones<1:
            return 0
        if (pos,target) in cache:
            return cache[pos,target]
        cache[pos,target]=0
        if arr[pos][0]<=zeroes and arr[pos][1]<=ones:
            cache[pos,target]=max(cache[pos,target],1+calc((zeroes-arr[pos][0],ones-arr[pos][1]),pos+1))
        cache[pos,target]=max(cache[pos,target],calc((zeroes,ones),pos+1))
        return cache[pos,target]
    return calc((m,n),0)

def max_subset_size_dp(strs, m, n):
    arr=convert_to_tuples(strs)
    if len(strs)<1:
        return 0
    if m<1 and n<1:
        return 0
    dp={}



if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    # strs = ["10", "0", "1"]
    # m = 1
    # n = 1
    print(max_subset_size_memoize(strs,m,n))