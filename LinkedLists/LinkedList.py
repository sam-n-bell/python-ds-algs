from LinkedLists.IndexOutOfLinkedListBoundsError import IndexOutOFLinkedListBoundsError
from LinkedLists.ListNode import ListNode


class LinkedList(object):

    def __init__(self):
        self._root = None
        self._length = 0

    @property
    def root(self):
        return self._root

    @property
    def length(self):
        return self._length

    def __repr__(self):
        current = self._root
        nodes = []
        while current is not None:
            nodes.append(str(current.val))
            current = current.next
        return '->'.join(nodes)

    def insert_at_head(self, val: int):
        old_root = self.root
        new_root = ListNode(val)
        new_root.next = old_root
        self._root = new_root
        self._length += 1

    def get_node_at_index(self, index: int):
        if index >= self._length:
            raise IndexOutOFLinkedListBoundsError("Index is out of bounds")
        count = 0
        current = self._root
        while count < index:
            count += 1
            current = current.next
        return current
