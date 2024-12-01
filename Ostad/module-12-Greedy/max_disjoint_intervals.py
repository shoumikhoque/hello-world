def max_disjoint_intervals(A):
    arr=sorted(A,key=lambda x :x[1])
    last_end=0
    ans=0
    for elem in arr:
        if last_end< elem[0]:
            ans+=1
            last_end=elem[1]
    return ans


if __name__ == '__main__':
    A = [ [1, 9], [2, 3], [5, 7] ]
    print(max_disjoint_intervals(A))