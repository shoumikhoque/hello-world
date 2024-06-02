from concept.LinkedList.DllNode import DllNode
from concept.LinkedList.LinkedList import LinkedList


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail=None
    def get_head(self):
        return self.head
    def get_tail(self):
        return self.tail
    def insert_at_head(self, val):
        if self.is_empty():
            self.head=DllNode(val)
            self.tail=self.head
        else:
            temp=self.head
            self.head.prev=DllNode(val)
            self.head=self.head.prev
            self.head.next=temp
        self.size+=1
    def insert_at_tail(self,val):
        if self.is_empty():
            self.tail=DllNode(val)
            self.head=self.tail
        else:
            temp=self.tail
            self.tail.next=DllNode(val)
            self.tail=self.tail.next
            self.tail.prev=temp
    def pop_from_head(self):
        if self.is_empty() :
            return
        temp=self.head
        self.head.next.prev=None
        self.head=self.head.next
        return temp.val

    def pop_from_tail(self):
        if self.is_empty() :
            return
        temp=self.tail
        self.tail.prev.next=None
        self.tail=self.tail.prev
        return temp.val

    def pop_value(self,val):
        if self.is_empty():
            return
        if self.head.val==val:
            self.pop_from_head()
        elif self.tail.val==val:
            self.pop_from_tail()
        else:
            prev=self.head
            temp=prev.next
            while temp is not None:
                if temp.val==val:
                    prev.next=temp.next
                    temp.next.prev=prev
                    break
                prev=prev.next
                temp=temp.next
        return

    def search(self,val):
        return super().search(val)
    def __str__(self):
        return super().__str__()
if __name__ == '__main__':
    dll=DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_head(9)
    dll.insert_at_head(11)
    dll.insert_at_tail(12)
    print(str(dll))
    # dll.pop_from_head()
    # print(str(dll))
    # dll.pop_from_tail()
    # dll.pop_value(8)
    print(str(dll))
    print(str(dll.search(10)))
