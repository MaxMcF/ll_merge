from .node import Node
from typing import Any


class LinkedList(object):
    def __init__(self, initial_data=None):
        try:
            self.head: Node = None
            self._length: int = 0
            if initial_data is not None:
                for item in initial_data:
                    self.insert(item)
        except TypeError:
            return TypeError

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def insert(self, val: Any) -> Any:
        '''Creates a new node and appends it to the beginning of the list
            This is done by re-stating which node is the head(the one youre appending)
            then setting the previous head equal to the next value of the appended item
        '''
        self.head = Node(val, self.head)
        self._length += 1

    def includes(self, val) -> bool:
        '''Checks to see if a value is contained in the list by iterating through and
        checking every node against the input value. If the value exists in the list
        , the function will return true if it does not exist in the list, it will return false.
        '''
        current = self.head
        while current is not None:
            if current.val is val:
                return True
            current = current.next
        return False

    def append(self, val) -> bool:
        '''Creates a new node and appends it at the end of the linked list
        '''
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(val, None)
        return True

    def insert_before(self, val, target_val) -> bool:
        '''Creates a new node and appends it before the target value
            args:
                new Node value, target Node value to insert before
            returns:
                True if the node was inserted
                False if the target value is not in the SLL
        '''
        current = self.head
        while current.next.val is not target_val:
            current = current.next
            if current.next == None:
                return False
        current.next = Node(val, current.next)
        return True

    def insert_after(self, val, target_val) -> bool:
        '''Creates a new node and appends it after the target value
        '''
        current = self.head
        while current.val is not target_val:
            current = current.next
            if current == None:
                return False
        current.next = Node(val, current.next)
        return True

    def find_k(self, k) ->bool:
        '''Takes in an input value of K, which corresponds to that
        many indexes from the end of the list. This function takes in the input,
        and returns the value of the item at index of length - k.
        '''
        if k < 0:
            raise IndexError
        tortoise = self.head
        hare = self.head
        for i in range(k):
            if hare is not None:
                hare = hare.next
            else:
                raise IndexError
        while hare.next is not None:
            hare = hare.next
            tortoise = tortoise.next
        return tortoise.val



# def small_list():
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(3)
#     ll.insert(4)
#     ll.find_k(2)


# # # def small_list_includes(link_list):
# # #     some_bool = link_list.includes(3)
# # #     print(some_bool)


# if __name__ == '__main__':
#     small_list()


