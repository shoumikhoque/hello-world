def findSmallestArray(arr1,arr2):
    if arr1 is None:
        return arr2;
    elif arr2 is None:
        return arr1;
    elif len(arr1)<len(arr2):
        return arr1
    else:
        return arr2
def bestSum(target,arr,memo={}):
    if target==0:
        return []
    elif target<0:
        return None
    for i in arr:
        remainder=target-i
        result=bestSum(remainder,arr,memo)
        if remainder in memo:
            result=findSmallestArray(result,memo[remainder])
        memo[remainder]=result
        if result is None:
            memo[target]=[i]
        else:
            result.append(i)
            memo[target]=result
        return memo[target]
    return None



if __name__ == '__main__':
    print(bestSum(8,[2,3,5]))

