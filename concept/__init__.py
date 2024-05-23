def findMin(nums):
    if len(nums)==1:
        return nums[0]
    elif len(nums)==2:
        if nums[0]<nums[1]:
            return nums[0]
        else:
            return nums[1]
    else:
        n=len(nums)
        left_min=findMin(nums[0:n//2])
        right_min=findMin(nums[n//2:n])
        if left_min<right_min:
            return left_min
        else:
            return right_min


if __name__ == '__main__':
    print(findMin([1,2,5,9,-1,6,3]))