from concept.LinkedList.LinkedList import LinkedList


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
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_list = LinkedList()
    for i in input_list:
        linked_list.add(i)
    print(str(reverse_in_group(linked_list, left=3,right=7)))