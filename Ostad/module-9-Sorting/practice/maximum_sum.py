import random

from concept.HashMap.CompletePathOfJourney import trace_path


def quick_select(arr, left, right, k,dp:dict):
    if left==right:
        return arr[left]
    if (str(left) + ':' + str(right)) in dp:
        return dp[str(left) + ':' + str(right)]
    pivot_index=random.randint(left,right)
    pivot_index=parttion(arr,left,right,pivot_index)

    num_elements_in_right_including_pivot=right-pivot_index+1
    if num_elements_in_right_including_pivot == k:
        ans = 0
        for i in range(pivot_index, right + 1):
            ans += arr[i]
        dp[str(left)+':'+str(right)]=ans
        return dp[str(left)+':'+str(right)]
    elif num_elements_in_right_including_pivot > k:
        dp[str(left) + ':' + str(right)]=quick_select(arr, pivot_index + 1, right, k,dp)
        return dp[str(left) + ':' + str(right)]
    else:
        ans = 0
        for i in range(pivot_index , right+1):
            ans += arr[i]
        dp[str(left) + ':' + str(right)] = ans + quick_select(arr, left, pivot_index - 1, k- num_elements_in_right_including_pivot,dp)
        return dp[str(left) + ':' + str(right)]

def parttion(arr, left, right, pivot_index):
    pivot_value=arr[pivot_index]
    arr[pivot_index],arr[left]=arr[left],arr[pivot_index]
    temp=right
    for i in range(right,left,-1):
        if arr[i]>pivot_value:
            arr[temp],arr[i]=arr[i],arr[temp]
            temp-=1
    arr[left],arr[temp]=arr[temp],arr[left]
    return temp

def maximum_sum_using_quick_select(arr, k):
    dp=dict()
    return quick_select(arr,0,len(arr)-1,k,dp)
def maximum_sum_using_sort(arr,k):
    arr=sorted(arr,reverse=True)
    ans=0
    for i in range(k):
        ans+=arr[i]
    return ans


if __name__ == '__main__':
    n=input().strip().split(' ')
    arr=input().strip()
    arr=arr.split(' ')
    arr=[int(i) for i in arr]
    print(maximum_sum_using_sort(arr,int(n[1])))