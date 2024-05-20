def find_sub_zero(nums):
    result=[]
    sum=dict()
    total_sum=0
    for i in range(len(nums)):
        total_sum+=nums[i]
        if nums[i]==0 :
            result.append([i,i])
        if total_sum==0:
            result.append([0,i])
        if sum.get(total_sum)!=None:
            result.append( [sum.get(total_sum)+1,i])
        sum[total_sum]=i
    return result
if __name__ == '__main__':
    inputs = [[10, 4, 10, -56, 23, 7, 2, -2, 9],
              [-3, 3],
              [2, -5, -4, 43, 2],
              [-7, 1, 2, 5, -6, 1, -3, 3, -17],
              [25, 50, 75, 100, 400]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tResult: ", find_sub_zero(inputs[i]))
        print("-" * 100)