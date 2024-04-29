def canSum(arr, sum,ans=False,memo=[]):
    if sum in arr:
        ans=True or ans
        return ans
    for n in arr:
        if sum - n >= arr[0]:
            print(n)
            memo=canSum(arr, sum - n,ans,memo)
            ans= memo[n] or ans
    return ans
if __name__ == '__main__':
    print(canSum([6,4,2], 8))

