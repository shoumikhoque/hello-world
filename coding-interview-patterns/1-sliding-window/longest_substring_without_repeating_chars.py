from operator import index

# abcabcbb
# window_start=7
# longest=3
# last_found_index={a:3,b:6,c:5}
def find(s):
    if len(s)==0:
        return 0
    window_start,longest=0,0
    last_found_index={}
    for i,val in enumerate(s):
        if val not in last_found_index:
            last_found_index[val]=i
        else:
            if last_found_index[val]>=window_start:
                longest=max(longest,i-window_start)
                window_start=last_found_index[val]+1
            last_found_index[val]=i
    return longest

if __name__ == '__main__':
    s='abcabcbb'
    print(find(s))