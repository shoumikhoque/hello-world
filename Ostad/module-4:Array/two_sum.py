
def tow_sum_brute_force(nums, target):
    """
    time-> O(n^2), space-> O(1)
    checking for each value pair from nums  in nested loop
    """
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if i != j and nums[i]+nums[j]==target :
                return [i,j]


def tow_sum_hash_map(nums, target):
    """
    time-> O(n), space-> O(n)
    create a dictionary to store each num's index with target-num
    traverse num -> return ans if the value exists in dictionary
    """
    dict={target - nums[i]: i for i in range(len(nums))}
    for i,num in enumerate(nums):
        if num in dict and dict[num]!=i:
            return [i,dict[num]]

if __name__ == '__main__':
    nums = [2,7,11,2]
    target = 4
    print(tow_sum_brute_force(nums,target))
    print(tow_sum_hash_map(nums, target))
