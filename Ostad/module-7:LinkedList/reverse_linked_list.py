class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    def __str__(self):
        return str(self.val)
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.head is None
    def add(self,val):
        if self.head is None:
            self.head=Node(val)
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=Node(val)
        self.size += 1
        return True
    def __reversed__(self):
        if self.size<2:
            return
        prev=self.head
        current=prev.next
        self.head.next=None
        while current is not None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.head=prev
        return self
    def to_array(self):
        arr = []
        cur=self.head
        while cur is not None:
            arr.append(cur.val)
            cur=cur.next
        return arr


if __name__ == '__main__':
    nums=[1,2,3,4,5]
    if len(nums)==0:
        print(nums)
    else:
        linked_list = LinkedList()
        for i in nums:
            linked_list.add(i)
        print(reversed(linked_list).to_array())

