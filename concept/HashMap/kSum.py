def find_sum(nums, target):
    nums_set=set(nums)
    for i in nums_set:
        if target-i in nums_set:
            return [i,target-i]
    return None


if __name__ == '__main__':
    inputs = [[1, 2, 3, 4],
              [1, 2],
              [2, 2],
              [-4, -1, -9, 1, -7],
              [25, 50, 75, 100, 400]]

    k = [5, 3, 4, -3, 425]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tResult: ", find_sum(inputs[i], k[i]), sep="")
        print("-" * 100)