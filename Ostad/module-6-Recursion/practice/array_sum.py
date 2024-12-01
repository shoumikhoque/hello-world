def array_sum(target:int, arr:[],ans:int)->int:
    if target==0:
        return 1
    elif ans[target]>0:
        return ans[target]
    for i in arr:
        if i<=target:
            temp=array_sum(target-i,arr,ans)
            if temp>0:
                ans[target]+=temp
    return ans[target]


if __name__ == '__main__':
    target=int(input())
    print(array_sum(target,[i for i in range(1,target+1)],[0]*(target+1)))