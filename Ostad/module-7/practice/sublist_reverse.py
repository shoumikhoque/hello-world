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
            sb+=str(current.val)+' '
            current=current.next
        return sb
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


def reverse_in_group(linked_list, left, right):
    if left==right:
        return linked_list
    ll_head = linked_list.head
    prev_of_range=None
    count = 1
    left_node = linked_list.head
    while count<left:
        prev_of_range=left_node
        left_node=left_node.next
        count+=1
    right_node=left_node
    while count<right:
        right_node=right_node.next
        count+=1
    next_of_range = right_node.next
    if prev_of_range is not None:
        prev_of_range.next=None
    linked_list.head=left_node
    right_node.next=None
    linked_list=reversed(linked_list)
    temp =linked_list.head
    while temp.next is not None:
        temp=temp.next
    temp.next=next_of_range
    if prev_of_range is not None:
        prev_of_range.next=linked_list.head
        linked_list.head=ll_head
    return linked_list

if __name__ == '__main__':
    n=int(input())
    nums=input().strip().split(' ')
    n=input().strip().split(' ')
    ll=LinkedList()
    for i in nums:
        ll.add(int(i))
    print(reverse_in_group(ll,int(n[0]),int(n[1])))