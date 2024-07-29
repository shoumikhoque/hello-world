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
    def __reversed__(self):
        if self.size < 2:
            return
        rev_ll=self.__copy__()
        prev = rev_ll.head
        current = prev.next
        rev_ll.head.next = None
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        rev_ll.head = prev
        return rev_ll
    def __copy__(self):
        copied=LinkedList()
        curr=self.head
        while curr is not None:
            copied.add(curr.val)
            curr=curr.next
        return copied
def is_palindrome(ll:LinkedList):
    if ll.size<2:
        return 'YES'
    reversed_ll = ll.__reversed__()
    rev_curr=reversed_ll.head
    current = ll.head
    while current is not None:
        if current.val !=rev_curr.val:
            return 'NO'
        current=current.next
        rev_curr=rev_curr.next
    return 'YES'
if __name__ == '__main__':
    n=int(input())
    nums=input().strip().split(' ')
    ll=LinkedList()
    for i in nums:
        ll.add(i)
    print(is_palindrome(ll))
