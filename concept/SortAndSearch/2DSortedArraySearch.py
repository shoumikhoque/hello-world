def binary_search_2d(nums,r_low,r_high,c_low,c_high,key):
    if nums[r_low][c_low]==key or nums[r_low][c_high]==key or nums[r_high][c_low]==key or nums[r_high][c_high]==key:
        return True
    if key<nums[r_low][c_low] or key>nums[r_high][c_high]:
        return False
    r_mid = (r_high + r_low) // 2
    c_mid = (c_low + c_high) // 2
    return (binary_search_2d(nums, r_low, r_mid, c_low, c_mid,key) or
            binary_search_2d(nums, r_low, r_mid, c_mid + 1, c_high, key) or
            binary_search_2d(nums, r_mid+1, r_high, c_low, c_mid, key) or
            binary_search_2d(nums, r_mid+1, r_high, c_mid+1, c_high, key))
def find_in(nums, key):
    if nums is None or len(nums)==0:
        return False
    rows=len(nums)
    cols=len(nums[0])
    if cols==0:
        return False
    return binary_search_2d(nums,0,rows-1,0,cols-1,key)

if __name__ == '__main__':
    lst = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [27, 29, 30, 31],
        [32, 33, 39, 50]
    ]

    # Example 1
    print(find_in(lst, 51))

    # Example 2
    print(find_in(lst, 10))