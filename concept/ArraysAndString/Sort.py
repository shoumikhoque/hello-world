from typing import List

def mergeSort(a:List[int])->List[int]:
    if len(a)>1:
        return merge(
            mergeSort(a[0:int(len(a) / 2):1]),
            mergeSort(a[int(len(a) / 2):len(a):1]))
    else:
        return a

def merge(a:List[int],b:List[int])->List[int]:
    l1=len(a)
    l2=len(b)
    ans=[0]*(l1+l2)
    i=j=k=0

    while i<l1 and j<l2:
        if a[i]<b[j]:
            ans[k]=a[i]
            i+=1
        else:
            ans[k]=b[j]
            j+=1
        k+=1
    if i==l1:
        while j!=l2:
            ans[k]=b[j]
            k+=1
            j+=1
    elif j==l2:
        while i!=l1:
            ans[k]=a[i]
            k+=1
            i+=1
    return ans




def insertionSort(a:List[int])-> List[int]:
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a
if __name__ == '__main__':
    a=[-5,-2,4,10,8,6,1,3]
    # print(merge([5,2,4,10],[8,6,1,3]))
    print(mergeSort(a))