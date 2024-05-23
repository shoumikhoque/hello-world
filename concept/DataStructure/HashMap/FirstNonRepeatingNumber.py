def find_first_unique(nums):
    d={}

    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in nums:
        if d[i]==1:
            return i
    return None


if __name__ == '__main__':
    inputs = [
        [9, 2, 3, 2, 6, 6],
        [-5, -4, -4, 6, -1],
        [-1, 2, -1, -4, -10],
        [1, 1, 2, 9],
        [-2, 2, -2, 2, 5]
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tfirst unique number: ", find_first_unique(inputs[i]), sep="")
        print("-" * 100)