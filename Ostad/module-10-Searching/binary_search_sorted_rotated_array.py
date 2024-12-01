def find_min_rotated_sorted_array(nums):
    left=0
    right=len(nums)-1
    res=nums[0]
    while left<=right:
        if nums[left]<nums[right]:
            res=min(res,nums[left])
        mid=(left+right)//2
        res = min(res, nums[mid])
        if nums[mid]>=nums[left]:
            left=mid+1
        else:
            right=mid-1
    return res

if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    print(find_min_rotated_sorted_array(nums))