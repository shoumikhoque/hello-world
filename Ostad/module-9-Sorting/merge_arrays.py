def merge_array(arr1, arr2, m, n):
    i, j = 0, 0
    ans = []
    arr1=arr1[:m]
    # Traverse both arrays and merge them
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    # If there are remaining elements in arr1, add them to ans
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    # If there are remaining elements in arr2, add them to ans
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    arr1=ans
    return arr1



if __name__ == '__main__':
    nums1=[1,2,3,0,0,0]
    nums2=[2,5,6]
    m=3
    n=3
    print(merge_array(nums1,nums2,m,n))