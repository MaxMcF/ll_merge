
def ll_merge(ll_1, ll_2):
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
