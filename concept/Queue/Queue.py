from concept.LinkedList.DoublyLinkedList import DoublyLinkedList


class Queue:
    def __init__(self):
        self.queue=DoublyLinkedList()
        self.size=self.queue.size
    def get_size(self):
        return self.queue.get_size()
    def is_empty(self):
        return self.queue.is_empty()
    def get_front(self):
        return self.queue.head
    def get_back(self):
        return self.queue.tail
    def enqueue(self,val):
        self.queue.insert_at_tail(val)
    def dequeue(self):
        return self.queue.pop_from_head()
    def __str__(self):
        return self.queue.__str__()
if __name__ == '__main__':
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(str(q))
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(str(q))


