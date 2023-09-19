def minCostClimbingStairs(arr,pos,ans):
    if pos==0 :
        ans[0] = 0
        return ans[0]
    if pos==1:
        ans[1]=arr[0]
        return ans[1]
    forPos1=minCostClimbingStairs(arr,pos-1,ans)+arr[pos-1]
    forPos2=minCostClimbingStairs(arr,pos-2,ans)+arr[pos-2]
    ans[pos]=min(forPos1,forPos2)
    return ans[len(arr)]


if __name__ == '__main__':
    print("hello")
    print(minCostClimbingStairs([2,4,1,5], 4,ans=[0,0,0,0,0]))