class MaxHeap:
    def __init__(self):
        self.heap=[]


    def insert(self, val):  # appends given value to the heap and heapify up
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def getMax(self): # gets the max value of the heap
        if self.heap:
            return self.heap[0]
        return

    def removeMax(self): #swaps 0th value with the last value and heapify 0th value
        if len(self.heap)==1:
            max_val=self.heap[0]
            del self.heap[0]
            return max_val
        elif len(self.heap)>1:
            max_val=self.heap[0]
            self.heap[0]=self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max_val
        else:
            return None

    def __percolateUp(self, index): # relocate a value to restore the heap property after inserting a new node
        parent=(index)//2
        if index<=0:
            return
        elif self.heap[parent]<self.heap[index]:
            tmp=self.heap[parent]
            self.heap[parent]=self.heap[index]
            self.heap[index]=tmp
            self.__percolateUp(self,parent)

    def __maxHeapify(self, index): # restores the heap property after a node is removed
        left=(index*2)+1
        right=(index*2)+2
        largest=index
        if len(self.heap)>left and self.heap[left]>self.heap[largest]:
            largest=left
        if len(self.heap)>right and self.heap[largest]>self.heap[right]:
            largest=right
        if largest!=index:
            tmp=self.heap[largest]
            self.heap[largest]=self.heap[index]
            self.heap[index]=tmp
            self.__maxHeapify(self,largest)
    def buildHeap(self,arr): #This function restores creates a heap from a list passed as an argument.
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__maxHeapify(i)


if __name__=='__main__':
    heap = MaxHeap()