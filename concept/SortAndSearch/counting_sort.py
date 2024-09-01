def counting_sort(arr):
    dp=[0]*1000000
    for i in arr:
        dp[int(i)]+=1
    ans=[]
    for i in range(len(dp)):
        while dp[i]>0:
            ans.append(i)
            dp[i]-=1
    return ans
def to_str(arr):
    s=''
    for i in arr:
        s+=' '+str(i)
    return s[1:]

if __name__ == '__main__':

    n=int(input().strip())
    arr=input().strip()
    arr=arr.split(' ')
    arr=[int(i) for i in arr]

    print(to_str(counting_sort(arr)))