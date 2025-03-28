def solve(n):
    numTree=[1]*(n+1)
    for node in range(2,n+1):
        total=0
        for root in range(1,node+1):
            left=root-1
            right=node-root
            total+=(numTree[left]*numTree[right])
        numTree[node]=total
    return numTree[n]



if __name__ == '__main__':
    n=4
    print(solve(n))