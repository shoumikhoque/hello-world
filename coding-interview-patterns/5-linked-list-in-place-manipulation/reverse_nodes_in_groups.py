from concept.LinkedList.LinkedList import LinkedList


def find_group(head,k):
    # start traversing from head
    last_node=head
    k-=1
    while last_node is not None and k>0:
        last_node=last_node.next
        k-=1
    if last_node is None:
        return None
    return last_node
    # return the node at K+1 as next node


def reverse_group_before_node(head, next_node_after_group):
    prev=None
    curr=head

    while curr is not None:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev



def reverse_in_group(linked_list, k):
    prev=None
    current_group_head=linked_list.head
    while current_group_head is not None:
        last_node_of_group=find_group(current_group_head,k)
        if last_node_of_group is not None:
            first_node_of_next_group=last_node_of_group.next
            last_node_of_group.next=None
            reversed_group_head=reverse_group_before_node(current_group_head,last_node_of_group)
            if prev is not None:
                prev.next=reversed_group_head
            else:
                linked_list.head=reversed_group_head
            while reversed_group_head.next is not None:
                reversed_group_head=reversed_group_head.next
            prev=reversed_group_head
            reversed_group_head.next=first_node_of_next_group
            current_group_head=first_node_of_next_group
        else:
            break
    return linked_list
if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8,9]
    linked_list=LinkedList()
    for i in input_list:
        linked_list.add(i)
    print(str(reverse_in_group(linked_list,k=2)))