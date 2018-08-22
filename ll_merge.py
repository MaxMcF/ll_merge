
def ll_merge(ll_1, ll_2):
    '''Function that merges two linked lists, using a zipper method. The first linked lists
    head node will be inserted first, followed by the second linked lists head node, followed
    by the following node in the first linked list, and so on
        Args:
            Linked List 1: This should be a singlely linked list of nodes
            Linked List 2: This should also be a singlely linked list of nodes
        Return:
            The head node of the new, merged list
    '''
    actual_head = ll_1.head
    while ll_1.head is not None and ll_2.head is not None:
        temp = ll_1.head.next
        ll_1.head.next = ll_2.head
        ll_2.head = ll_2.head.next
        ll_1.head.next.next = temp
        ll_1.head = temp
    if ll_1.head is None and ll_2.head is not None:
        current_head = actual_head
        while current_head.next is not None:
            current_head = current_head.next
        current_head.next = ll_2.head
    return actual_head
