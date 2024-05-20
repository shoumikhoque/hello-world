def find_pairs(nums):
    map=dict()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum=nums[i]+nums[j]
            if sum in map:
                return [map[sum],[nums[i],nums[j]]]
            else:
                map[sum]=[nums[i],nums[j]]
    return None


if __name__ == '__main__':
    nums_list = [
        [3, 4, 7, 1, 12, 9, 0],
        [1, 2, 3, 5, 8],
        [10, 20, 30, 40, 50, 60, 70, 5, 65, 15, 25],
        [-5, -3, -1, 0, 2, 4, 6],
        [0, 1, 2, 3, 4, 99]
    ]

    # Iterate through each test case
    for i, nums in enumerate(nums_list):
        print(f"{i + 1}.\tnums =  {nums}")
        result = find_pairs(nums)
        if result:
            print(f"\tFound pairs: {result}\n")
        else:
            print("\tNo matching pairs found.\n")
        print("-" * 100)