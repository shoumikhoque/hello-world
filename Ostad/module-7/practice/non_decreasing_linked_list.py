class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
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
def is_non_decreasing(ll):
    if ll.size<2:
        return 'YES'
    curr=ll.head
    while curr.next is not None:
        if curr.val> curr.next.val:
            return 'NO'
        curr=curr.next
    return 'YES'


if __name__ == '__main__':
    n=int(input())
    nums=input().strip().split(' ')
    ll=LinkedList()
    for i in nums:
        ll.add(int(i))
    print(is_non_decreasing(ll))
