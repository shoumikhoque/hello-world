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


def rotate(ll, n, k):
    if n==k:
        return ll
    i=1
    curr=ll.head
    kth_node=None
    while curr.next is not None:
        if i==k:
            kth_node=curr
        i+=1
        curr=curr.next
    curr.next=ll.head
    ll.head=kth_node.next
    kth_node.next=None
    return ll


if __name__ == '__main__':
    s1 = input().strip().split()
    n = int(s1[0])
    k = int(s1[1])
    nums = input().strip().split(' ')
    ll = LinkedList()
    for i in nums:
        ll.add(int(i))
    print(rotate(ll, n, k))