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
        if self.size==0:
            return 'Empty'
        current=self.head
        sb=str('')
        while current is not None:
            sb+=str(current.val)+' '
            current=current.next
        return sb


def partition_linked_list(ll, k):
    tail = ll.head
    while tail.next is not None:
        tail = tail.next

    prv=None
    cur=ll.head
    while cur.next is not None and cur.next is not tail.next:
        if cur.val>=k:

            tail.next=cur
            tail=tail.next
            tail.next = None
        else:
            cur=cur.next
            prv=prv.next

    return ll


if __name__ == '__main__':

    n=int(input())
    nums = input().strip().split(' ')
    k = int(input())
    ll = LinkedList()
    for i in nums:
        ll.add(int(i))
    print(partition_linked_list(ll,k))


