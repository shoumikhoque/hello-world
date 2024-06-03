# Driver to test above code
def binary_search(nums, high, low, key):
    if high < low:
        return -1
    mid = (low + high) // 2
    if key == nums[mid]:
        return mid
    if key > nums[mid]:
        return binary_search(nums, (mid + 1), high, key)
    else:
        return binary_search(nums, low, (mid - 1), key)


def pivoted_binary_search(nums, n, key):
    pivot=find_pivot_point(nums,0,n-1)
    if pivot==-1:
        return binary_search(nums,0,n-1,key)
def find_pivot_point(nums,low, high):
    if high<low:
        return -1
    if high==low:
        return low
    mid=(high+low)//2
    if mid<high and nums[mid]>nums[mid+1]:
        return mid
    if mid>low and nums[mid]<nums[mid-1]:
        return mid-1
    if nums[low]>=nums[mid]:
        return find_pivot_point(nums,low,mid-1)
    else:
        return find_pivot_point(nums,mid+1,high)
    

if __name__ == '__main__':

    nums = [4,6,0, 1, 2, 3 ,7, 8, 9]
    key = 0
    print("Index of the element is : ",
          pivoted_binary_search(nums, len(nums), key))