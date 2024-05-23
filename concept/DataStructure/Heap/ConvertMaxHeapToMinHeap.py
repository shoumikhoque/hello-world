from concept.DataStructure.Heap.MinHeap import MinHeap


def convertToMinHeap(arr):
    minHeap=MinHeap()
    minHeap.buildHeap(arr)
    for i in minHeap.heap:
        print(i ,end=" ")
    return minHeap
if __name__=="__main__":
    maxHeap=[9,4,7,1,-2,6,5]
    print(convertToMinHeap(maxHeap))