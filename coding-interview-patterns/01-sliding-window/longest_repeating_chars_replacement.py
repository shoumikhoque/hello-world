def find(s,k):
    freq_map={}
    left=0
    max_length=0
    for right in range(len(s)):
        c=s[right]
        freq_map[c]=1+freq_map.get(c,0)
        if max_length - find_most_freq_char_in_map(freq_map)<k:
            max_length=max(max_length,right-left+1)
        else:
            freq_map[s[left]]-=1
            left+=1
    return max_length


def find_most_freq_char_in_map(freq_map:dict):
    max_count=0
    for k,v in freq_map.items():
        max_count=max(max_count,v)
    return max_count



if __name__ == '__main__':
    s='aabccbb'
    k=2
    print(find(s,k))