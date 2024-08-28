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

def remove_duplicates(ll, k):
    if ll.size<2:
        return ll
    dp=set()
    dp.add(ll.head.val)
    curr=ll.head
    while curr.next is not None:
        if curr.next.val in dp:
            curr.next=curr.next.next
        else:
            dp.add(curr.next.val)
            curr=curr.next
    return ll
if __name__ == '__main__':
    k= int(input())
    nums = input().strip().split(' ')
    ll = LinkedList()
    for i in nums:
        ll.add(int(i))
    print(remove_duplicates(ll,k))