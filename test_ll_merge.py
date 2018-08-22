from .linked_list.linked_list import LinkedList
from .ll_merge import ll_merge
import pytest

@pytest.fixture
def small_list_1():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(3)
    ll.insert(5)
    return ll

@pytest.fixture
def small_list_2():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(4)
    ll.insert(6)
    return ll

@pytest.fixture
def long_list_2():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(4)
    ll.insert(6)
    ll.insert(7)
    ll.insert(8)
    ll.insert(9)
    return ll

def test_ll_merge_works(small_list_1, small_list_2):
    expected = small_list_1.head
    actual = ll_merge(small_list_1, small_list_2)
    assert expected == actual

def test_ll_merge_correct_order(small_list_1, small_list_2):
    actual = ll_merge(small_list_2, small_list_1)
    actual_list = []
    while actual is not None:
        actual_list.append(actual.val)
        actual = actual.next
    expected_list = [6, 5, 4, 3, 2, 1]
    assert actual_list == expected_list

def test_ll_merge_second_list_bigger(small_list_1, long_list_2):
    actual = ll_merge(small_list_1, long_list_2)
    actual_list = []
    while actual is not None:
        actual_list.append(actual.val)
        actual = actual.next
    expected_list = [5, 9, 3, 8, 1, 7, 6, 4, 2]
    assert actual_list == expected_list

def test_ll_merge_first_list_bigger(small_list_1, long_list_2):
    actual = ll_merge(long_list_2, small_list_1)
    actual_list = []
    while actual is not None:
        actual_list.append(actual.val)
        actual = actual.next
    expected_list = [9,5,8,3,7,1,6,4,2]
    assert actual_list == expected_list

def test_ll_merge_second_list_is_null(small_list_1):
    actual = ll_merge(small_list_1, None)
    actual_list = []
    while actual is not None:
        actual_list.append(actual.val)
        actual = actual.next
    expected_list = [5, 3, 1]
    assert actual_list == expected_list
