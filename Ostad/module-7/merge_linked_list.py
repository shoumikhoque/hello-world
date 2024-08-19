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
    def to_array(self):
        arr = []
        cur=self.head
        while cur is not None:
            arr.append(cur.val)
            cur=cur.next
        return arr


def merge_linked_list(ll1, ll2):
    if ll1.head.val>ll2.head.val:
        ll1,ll2=ll2,ll1
    cur1=ll1.head
    cur2=ll2.head
    while cur1.next is not None and cur2 is not None:
        if cur2.val<cur1.next.val:
            temp1=cur1
            temp2 = cur2
            cur2=cur2.next
            temp2.next=cur1.next
            cur1.next=temp2
        else:
            cur1=cur1.next
    if cur1.next is None and cur2 is not None:
        cur1.next=cur2

    return ll1

if __name__ == '__main__':
    nums1 = [0]
    nums2 = []
    if len(nums1) == 0 and len(nums2)==0:
        print([])
    elif len(nums1) == 0:
        print(nums2)
    elif len(nums2)==0:
        print(nums1)
    else:
        linked_list1 = LinkedList()
        for i in nums1:
            linked_list1.add(i)
        linked_list2 = LinkedList()
        for i in nums2:
            linked_list2.add(i)
        print(merge_linked_list(linked_list1,linked_list2).to_array())

