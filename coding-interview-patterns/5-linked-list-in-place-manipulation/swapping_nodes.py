from concept.LinkedList.LinkedList import LinkedList


def swap_postions(linked_list, k):
    prev1=None
    front=linked_list.head
    n=1
    while front.next is not None:
        n+=1
        front=front.next
    if k>n+1-k:
        k=n+1-k
    count=1
    front = linked_list.head
    while count<k:
        count+=1
        prev1=front
        front=front.next
    front_next = front.next
    prev2 = linked_list.head
    while front_next.next is not None:
        front_next = front_next.next
        prev2 = prev2.next
    end = prev2.next
    front_next = front.next
    end_next = end.next

    if prev1 is not None:
        prev1.next=end
    else:
        linked_list.head=end
    prev2.next = front
    if end is front_next:
        end.next = front
    else:
        end.next=front_next
    front.next = end_next

    return linked_list


if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6,7,8]
    linked_list = LinkedList()
    for i in input_list:
        linked_list.add(i)
    print(str(swap_postions(linked_list,k=8)))