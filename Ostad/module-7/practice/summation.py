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
            sb+=str(current.val)+''
            current=current.next
        return sb
    def __reversed__(self):
        if self.head is None or self.head.next is  None :
            return self
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


def summation(ll1, ll2):
    if ll1.head is None:
        return 'ostad'+str(ll2.__reversed__())
    if ll2.head is None:
        return 'ostad'+str(ll1)
    ll1=ll1.__reversed__()
    ll2=ll2.__reversed__()
    cur1=ll1.head
    cur2=ll2.head
    carry=0
    while cur1 is not None and cur2 is not None:
        s=cur1.val+cur2.val+carry
        if(s>9):
            carry=1
            s=s%10
        else:
            carry=0
        cur1.val=s
        cur2.val=s
        cur1=cur1.next
        cur2=cur2.next
    if cur2 is None:
        while cur1 is not None:
            s=cur1.val+carry
            if(s>9):
                carry=1
                s=s%10
            else:
                carry=0
            cur1.val=s
            cur1=cur1.next
        if carry==1:
            ll1.add(1)
        return 'ostad'+str(ll1.__reversed__())

    if cur1 is None:
        while cur2 is not None:
            s=cur2.val+carry
            if(s>9):
                carry=1
                s=s%10
            else:
                carry=0
            cur2.val=s
            cur2=cur2.next
        if carry==1:
            ll2.add(1)
        return 'ostad'+str(ll2.__reversed__())


if __name__ == '__main__':
    nums1=input().strip()
    nums2=input().strip()
    ll1=LinkedList()
    ll2=LinkedList()
    for i in nums1:
        ll1.add(int(i))
    for i in nums2:
        ll2.add(int(i))
    print(summation(ll1,ll2))
