def binary_search(nums, target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=left+(right-left+1)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9,10, 12]
    target = 5
    print(binary_search(nums,target))