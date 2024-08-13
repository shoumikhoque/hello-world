from concept.LinkedList.LinkedList import LinkedList


def find_group(head, group_size):
    elem_count = 0
    cur=head
    prev=None
    while cur is not None:
        elem_count+=1
        prev=cur
        cur=cur.next
        if elem_count==group_size:
            break
    if elem_count==group_size:
        return prev,cur
    if cur is None:
        return None, None



def reversed_even_groups(linked_list):
    group_size=2
    cur=linked_list.head.next
    prev=linked_list.head

    while cur is not None:
        # find group according to size from cur
        last_of_cur_group,next_group_head=find_group(cur,group_size)
        if last_of_cur_group is not None and group_size%2==0:
            # reverse this group
            reverse_list=LinkedList()
            reverse_list.head=cur

            last_of_cur_group.next=None
            reverse_list=reverse_list.__reversed__()
            prev.next=reverse_list.head
            last_of_cur_group, _ = find_group(reverse_list.head, group_size)
            last_of_cur_group.next=next_group_head
            cur=next_group_head
        else:
            cur=next_group_head
            prev=last_of_cur_group
        group_size+=1

    return linked_list


if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    linked_list = LinkedList()
    for i in input_list:
        linked_list.add(i)
    print(str(reversed_even_groups(linked_list)))