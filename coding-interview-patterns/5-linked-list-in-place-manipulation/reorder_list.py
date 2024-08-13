from concept.LinkedList.LinkedList import LinkedList


def merge_linked_lists(first_list, second_list):
    if first_list.head is None:
        return second_list
    cur1 = first_list.head
    while second_list.head is not None:
        cur2=second_list.head
        second_list.head=second_list.head.next
        cur2.next = cur1.next
        cur1.next=cur2
        if cur2.next is not None:
            cur1=cur2.next
        else:
            cur1=cur2

def reorder_list(linked_list):
    fast=linked_list.head
    slow=linked_list.head
    prev=None
    while fast is not None and fast.next is not None:
        prev=slow
        slow=slow.next
        fast = fast.next.next
    second_list=LinkedList()
    second_list.head=slow
    second_list=second_list.__reversed__()
    prev.next=None
    merge_linked_lists(linked_list,second_list)

    return linked_list


if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8,9]
    linked_list = LinkedList()
    for i in input_list:
        linked_list.add(i)
    print(str(reorder_list(linked_list)))