def min_sub_array_len(nums, target):
    left=0
    min_length=float('inf')
    curr_sum=0
    for right in range(len(nums)):
        curr_sum+=nums[right]
        while curr_sum>target:
            curr_sum-=nums[left]
            left+=1
            min_length = min(min_length, right - left + 1)
        if curr_sum==target:
            min_length=min(min_length,right-left+1)
    return min_length if min_length!=float('inf') else 0

if __name__ == '__main__':
    target = [7,]
    input_arr = [[2, 3, 1, 2, 4, 3]]
    for i in range(len(input_arr)):
        window_size = min_sub_array_len( input_arr[i],target[i])
        print(i + 1, ".\t Input array: ", input_arr[i], "\n\t Target: ", target[i],
              "\n\t Minimum Length of Subarray: ", window_size, sep="")
        print("-" * 100)