from collections import deque
def clean_up(i,current_window,nums):
    while current_window and nums[i]>=nums[current_window[-1]]:
        current_window.pop()

def find_max_sliding_window(nums, w):
    if len(nums)==1:
        return nums
    output=[]
    current_window=deque()
    for i in range(w):
        clean_up(i,current_window,nums)
        current_window.append(i)
    output.append(nums[current_window[0]])
    for i in range(w,len(nums)):
        clean_up(i,current_window,nums)
        if current_window and current_window[0]<=(i-w):
            current_window.popleft()
        current_window.append(i)
        output.append(nums[current_window[0]])
    return output


if __name__ == '__main__':
    window_sizes = [3, 3, 3, 3, 2, 4, 3, 2, 3, 6]
    nums_list = [
        [9, 5, 3, 1, 6, 3],
    ]

    for i in range(len(nums_list)):
        print(f"{i + 1}.\tInput list:\t{nums_list[i]}")
        print(f"\tWindow size:\t{window_sizes[i]}")
        output = find_max_sliding_window(nums_list[i], window_sizes[i])
        print(f"\n\tMaximum in each sliding window:\t{output}")
        print("-" * 100)