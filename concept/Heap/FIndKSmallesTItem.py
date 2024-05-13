from concept.Heap.MinHeap import MinHeap


def find_k_smallest_item(arr,k):
    ans=[]
    minHeap=MinHeap()
    minHeap.buildHeap(arr)
    for i in range(k):
        ans.append(minHeap.getMin())
        minHeap.removeMin()
    return ans
if __name__=="__main__":
    print(find_k_smallest_item([9, 4, 7, 1, -2, 6, 5],3))