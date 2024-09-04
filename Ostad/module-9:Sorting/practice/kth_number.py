import random

def quickselect(arr, left, right, k):
    if left == right:
        return arr[left]
    # Randomly choose a pivot index
    pivot_index = random.randint(left, right)
    # Partition the array around the pivot and get the final position of the pivot
    pivot_index = partition(arr, left, right, pivot_index)
    # Number of elements in the left partition including the pivot
    num_elements_in_left = pivot_index - left + 1
    if k < num_elements_in_left - 1:
        # k-th smallest is in the left partition
        return quickselect(arr, left, pivot_index - 1, k)
    elif k == num_elements_in_left - 1:
        # The pivot is the k-th smallest element
        return arr[pivot_index]
    else:
        # k-th smallest is in the right partition
        return quickselect(arr, pivot_index + 1, right, k - num_elements_in_left)

def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    # Move pivot to the end
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    # temp index for the smaller element
    temp = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[temp], arr[i] = arr[i], arr[temp]
            temp += 1
    # Move pivot to its final place
    arr[right], arr[temp] = arr[temp], arr[right]
    return temp
def kth_median(arr,k):
    return quickselect(arr,0,len(arr)-1,k-1)

if __name__ == '__main__':
    n=input().strip().split(' ')
    arr=input().strip().split(' ')
    arr=[int(i) for i in arr]
    print(kth_median(arr,int(n[1])))