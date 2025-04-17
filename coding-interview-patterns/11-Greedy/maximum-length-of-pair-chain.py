def solve(pairs):
    pairs.sort(key=lambda p : p[1])
    result=1
    end=pairs[0][1]
    for i in range(1,len(pairs)):
        if end< pairs[i][0]:
            result+=1
            end=pairs[i][1]
    return result

if __name__ == '__main__':
    pairs = [[1,2],[2,3],[3,4]]
    print(solve(pairs))