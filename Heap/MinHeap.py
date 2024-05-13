class MinHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,val):
        if self.heap:
            self.heap.append(val)
            self.__perlocateUp(len(self.heap)-1)
    def getMin(self):
        if self.heap and len(self.heap)>0:
            return self.heap[0]
        return None
    def removeMin(self):
        if self.heap:
            if len(self.heap)==1:
                min_value=self.heap[0]
                del self.heap[0]
                return min_value
            elif len(self.heap)>1:
                min_value=self.heap[0]
                self.heap[0]=self.heap[len(self.heap)-1]
                del self.heap[-1]
                self.__minHeapify(0)
                return min_value
            else:
                return None

    def __perlocateUp(self, index):
        if index<=0:
            return
        parent=(index-1)//2
        if self.heap and self.heap[parent]>self.heap[index]:
            tmp=self.heap[parent]
            self.heap[parent]=self.heap[index]
            self.heap[index]=tmp
            self.__perlocateUp(parent)

    def __minHeapify(self, index):
        left=(index*2)+1
        right=left+1
        smallest=index
        if len(self.heap)>left and self.heap[left]<self.heap[smallest]:
            smallest=left
        if len(self.heap)>right and self.heap[right]<self.heap[smallest]:
            smallest=right
        if smallest!=index:
            tmp=self.heap[smallest]
            self.heap[smallest]=self.heap[index]
            self.heap[index]=tmp
            self.__minHeapify(smallest)
    def buildHeap(self,arr):
        self.heap=arr
        for i in range (len(arr)-1,-1,-1):
            self.__minHeapify(self,i)