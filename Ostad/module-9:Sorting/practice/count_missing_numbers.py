def missing_numbers(arr, k):
    s=set()
    for i in arr:
        if i<k:
            s.add(i)
    return k-len(s)-1

if __name__ == '__main__':
    n=input().strip().split(' ')
    arr=input().strip()
    arr=arr.split(' ')
    arr=[int(i) for i in arr]
    print(missing_numbers(arr,int(n[1])))