class MaxHeap:
    def __init__(self):
        self.heap=[]

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def getMax(self):
        if self.heap and len(self.heap)>0:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap)==1:
            max_value=self.heap[0]
            del self.heap[0]
            return max_value
        elif len(self.heap)>1:
            max_value=self.heap[0]
            self.heap[0]=self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max_value

    def __percolateUp(self, index):
        if index<=0:
            return
        parent=(index-1)//2
        if self.heap[parent] and self.heap[parent]<self.heap[index]:
            tmp=self.heap[parent]
            self.heap[parent]=self.heap[index]
            self.heap[index]=tmp
            self.__percolateUp(parent)


    def __maxHeapify(self, index):
        left=index*2+1
        right=index*2+2
        largest=index
        if len(self.heap)>left and self.heap[largest]< self.heap[left]:
            largest=left
        if len(self.heap)>right and self.heap[largest]<self.heap[right]:
            largest=right
        if largest!=index:
            tmp=self.heap[largest]
            self.heap[largest]=self.heap[index]
            self.heap[index]=tmp
            self.__maxHeapify(largest)
    def buildHeap(self,arr):
        self.heap=arr
        for i in range (len(arr)-1,-1,-1):
            self.__maxHeapify(self,i)


heap = MaxHeap()