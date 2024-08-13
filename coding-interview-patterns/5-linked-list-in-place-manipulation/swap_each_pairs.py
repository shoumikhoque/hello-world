from concept.LinkedList.LinkedList import LinkedList


def swap_pairs(linked_list):
    cur=linked_list.head
    prev=None
    while cur is not None and cur.next is not None:
        if prev is not None:
            prev.next=cur.next
        else:
            linked_list.head=cur.next
        temp=cur
        cur=cur.next
        nxt_pair_start=cur.next
        cur.next=temp
        temp.next=nxt_pair_start
        prev=temp
        cur=nxt_pair_start
    return linked_list


if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    linked_list = LinkedList()
    for i in input_list:
        linked_list.add(i)
    print(str(swap_pairs(linked_list)))