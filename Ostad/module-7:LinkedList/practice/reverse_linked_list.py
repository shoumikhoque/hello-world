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
    def __str__(self):
        # if list is empty
        if self.is_empty():
            return 'Empty'
        current=self.head
        sb=str('')
        while current is not None:
            sb+=str(current.val)+'->'
            current=current.next
        return sb[:-2]
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
    def remove_head(self):
        self.head=self.head.next
        self.size-=1
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
def reverse_recur(ll:LinkedList):
    if ll.size<2:
        return ll
    temp=ll.head
    ll.remove_head()
    ll=reverse_recur(ll)
    ll.add(temp)
    return ll


if __name__ == '__main__':
    n=int(input())
    nums=input().strip().split(' ')
    ll=LinkedList()
    for i in nums:
        ll.add(i)
    print(reversed(ll))