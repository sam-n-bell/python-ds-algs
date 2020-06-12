from LinkedLists.IndexOutOfLinkedListBoundsError import IndexOutOFLinkedListBoundsError
from LinkedLists.ListNode import ListNode
from typing import List


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

    def append(self, val: int):
        self.append_from_list([val])

    def append_from_list(self, vals: List):
        if len(vals) > 0:
            last_node = self.get_node_at_index(self._length - 1)
            if last_node is None:
                last_node = ListNode(vals.pop(0))
                self._root = last_node
                self._length += 1
            for val in vals:
                last_node.next = ListNode(val)
                self._length += 1
                last_node = last_node.next

    def insert_at_index(self, index: int, val: int):
        if index == 0:
            self.insert_at_head(val)
        elif index == self._length:
            self.append(val)
        else:
            prior_node = self.get_node_at_index(index - 1)
            old_next = prior_node.next
            new_node = ListNode(val)
            new_node.next = old_next
            prior_node.next = new_node

    def reverse(self):
        if self._length > 1:
            previous = None
            current = self._root
            next = None
            # 2 -> 4 -> 6 to 2 <- 4 <- 6
            while current is not None:
                next = current.next
                current.next = previous
                previous = current
                current = next
            self._root = previous

    def get_node_at_index(self, index: int):
        if index >= self._length:
            raise IndexOutOFLinkedListBoundsError("Index is out of bounds")
        count = 0
        current = self._root
        while count < index:
            count += 1
            current = current.next
        return current
