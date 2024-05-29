from concept.LinkedList.Node import Node


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
    def remove_val(self,val):
        # if list is empty
        if self.is_empty():
            raise BaseException('List is empty.')
        # val is at head
        if self.head.val==val:
            self.head=self.head.next
            return True
        # val is at middle or end
        prev=self.head
        current=self.head.next
        while current is not None:
            if current.val==val:
                prev.next=current.next
                return True
            prev=prev.next
            current=current.next

        # val not found
        raise BaseException(' val: '+str(val)+' not found')
    def search(self,val):
        # if list is empty
        if self.is_empty():
            raise BaseException('List is empty.')
        pos=0
        current=self.head
        while current is not None:
            if current.val == val:
                return pos
            current = current.next
            pos += 1

        # val not found
        raise BaseException(' val: ' + str(val) + ' not found')

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
if __name__ == '__main__':
    ll =LinkedList()

    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(5)
    print(str(ll))
    print(ll.search(5))
    print(str(ll))
