from BinarySearchTrees.TreeNode import TreeNode
from typing import List

class BinarySearchTree(object):

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node: TreeNode):
        self._root = node

    def create_node(self, val: int):
        if not self._root:
            print(f'Setting root to {val}')
            self._root = TreeNode(val)
        else:
            self.__create_node(val, self._root)

    def __create_node(self, val: int, root: TreeNode):
        if val < root.val:
            if not root.left:
                print(f'Setting {val} to the left of {root.val}')
                root.left = TreeNode(val)
            else:
                self.__create_node(val, root.left)
        elif val > root.val:
            if not root.right:
                print(f'Setting {val} to the right of {root.val}')
                root.right = TreeNode(val)
            else:
                self.__create_node(val, root.right)

    def create_nodes_from_list(self, vals: List):
        for val in vals:
            self.create_node(val)

    def lowest_common_ancestor(self, val1: int, val2: int):
        root = self._root
        if not root:
            print('The tree is empty')
        else:
            lca = self.__find_lca(val1, val2, root)
            print(f'The lowest common ancestor for {val1} and {val2} is {lca}')

    def __find_lca(self, val1: int, val2: int, root: TreeNode):
        if not root:
            return None
        if val1 > root.val and val2 > root.val:
            return self.__find_lca(val1, val2, root.right)
        elif val1 < root.val and val2 < root.val:
            return self.__find_lca(val1, val2, root.left)
        else:
            return root.val
