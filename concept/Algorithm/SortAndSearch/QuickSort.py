import random

def choose_pivot(left, right):
    # Pick 3 random numbers within the range of the list
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    # Return their median
    return max(min(i1, i2), min(max(i1, i2), i3))


def partition(lst, left, right):
    pivot_index=choose_pivot(left,right)
    lst[right],lst[pivot_index]=lst[pivot_index],lst[right]
    pivot_value=lst[right]
    i=left-1
    for j in range(left,right):
        if lst[j]<=pivot_value:
            i+=1
            lst[i],lst[j]=lst[j],lst[i]
    lst[i+1],lst[right]=lst[right],lst[i+1]
    return i+1


def quick_sort(lst, left, right):
    if left<right:
        pivot_index=partition(lst,left,right)
        quick_sort(lst,left,pivot_index-1)
        quick_sort(lst,pivot_index+1,right)


if __name__ == '__main__':
    lst = [50, 40, 20, 10, 30]
    quick_sort(lst, 0, len(lst) - 1)

    # Printing Sorted list
    print("Sorted list: ", lst)