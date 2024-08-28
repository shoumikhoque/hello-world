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
def middle_of_linked_list(linked_list:LinkedList):
    first=linked_list.head
    second=linked_list.head
    while second!=None and second.next!=None:
        first=first.next
        second=second.next.next
    return first.val

if __name__ == '__main__':
    n=int(input())
    linked_list=LinkedList()
    values=input().strip().split(' ')
    for i in values:
        linked_list.add(i)
    print(middle_of_linked_list(linked_list))