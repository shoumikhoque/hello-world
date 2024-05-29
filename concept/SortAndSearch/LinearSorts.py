from encodings.punycode import insertion_sort


def selection_sort(arr):
    # select the minimum number in the list and put it in the front
    for i in range(len(arr)-1):
        mini=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr


def bubble_sort(arr):
    #compare two adjacent items and swap position if necessary until end
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def insertion_sort(lst):
    # Traverse through 1 to len(lst)
    for i in range(1, len(lst)):
        key = lst[i]
        # Move elements of lst greater than key, to one position ahead
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

if __name__ == '__main__':
    arr=[11,6,4,8,7,6,5,3,0,9]
    print(insertion_sort(arr))