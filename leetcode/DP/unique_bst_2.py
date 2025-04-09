def solve(n):
    dp={}
    def calc(left,right):
        if left>right:
            return [None]
        if (left,right) in dp:
            return dp[(left,right)]
        dp[(left, right)]=[]
        for val in range(left,right+1):
            for leftSubTree in calc(left,val-1):
                for rightSubTree in calc(val+1,right):
                    dp[(left, right)].append(TreeNode(val,leftSubTree,rightSubTree))
        return dp[(left, right)]
    return calc(1,n)



if __name__ == '__main__':
    n=3
    print(solve(n))