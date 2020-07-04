from TreeNode import TreeNode
from typing import List
from collections import deque

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
    
    def print_tree_height(self):
        levels = self.__height(self.root)
        print(f'This tree goes at most {levels} levels down')

    def __height(self, root: TreeNode, cur_height: int=0):
        if not root:
            return cur_height
        else:
            return max(self.__height(root.left, cur_height + 1), self.__height(root.right, cur_height + 1))

    def reverse(self):
        root = self._root
        self.__reverse(root.left, root.right)
        self._root = root
        
    def __reverse(self, left, right):
        left, right = right, left
        if left.left is not None or left.right is not None:
            self.__reverse(left.left, left.right)
        if right.left is not None or right.right is not None:
            self.__reverse(right.left, right.right)

    def lowest_common_ancestor(self, val1: int, val2: int):
        root = self._root
        if not root:
            return None
        else:
            return self.__find_lca(val1, val2, root)

    def __find_lca(self, val1: int, val2: int, root: TreeNode):
        if not root:
            return None
        if val1 > root.val and val2 > root.val:
            return self.__find_lca(val1, val2, root.right)
        elif val1 < root.val and val2 < root.val:
            return self.__find_lca(val1, val2, root.left)
        else:
            return root.val

    def contains_subtree(self, subtree):
        if not self._root or not subtree.root:
            return False
        else:
            root = self._root
            sub = subtree.root
            return self.__contains_subtree(root, sub)

    def __contains_subtree(self, root, sub) -> bool:
        if root is None and sub is None:
            return True
        elif (root is None and sub is not None) or (root is not None and sub is None):
            return False
        elif root.val != sub.val:
            return self.__contains_subtree(root.left, sub) or self.__contains_subtree(root.right, sub)
        else:
            # root.val == sub.val
            return self.__contains_subtree(root.left, sub.left) and self.__contains_subtree(root.right, sub.right)

    def print_inorder(self):
        self._inorder = []
        self.__inorder(self._root)
        print(self._inorder)

    def __inorder(self, root):
        if root is not None:
            if root.left:
                self.__inorder(root.left)
            self._inorder.append(root.val)
            if root.right:
                self.__inorder(root.right)

    def print_postorder(self):
        self._postorder = []
        self.__postorder(self._root)
        print(self._postorder)

    def __postorder(self, root):
        if root is not None:
            if root.left:
                self.__postorder(root.left)
            if root.right:
                self.__postorder(root.right)
            self._postorder.append(root.val)

    def print_preorder(self):
        self._preorder = []
        self.__preorder(self._root)
        print(self._preorder)

    def __preorder(self, root):
        if root is not None:
            self._preorder.append(root.val)
            if root.left:
                self.__preorder(root.left)
            if root.right:
                self.__preorder(root.right)

    def print_breadth(self):
        root = self._root
        q = deque()
        q.append(root)
        while len(q) > 0:
            # while nodes in the queue
            cur_level = list()
            for i in range(len(q)):
                # take from the left
                node = q.popleft()
                # check for children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cur_level.append(node.val)
            print(cur_level)
            