import unittest
from BinarySearchTree import BinarySearchTree

class TestBST(unittest.TestCase):

    def setUp(self):
        """
        Runs before every test
        :return:
        """
        self.bst = BinarySearchTree()
        self.bst.create_nodes_from_list(vals=[10, 15, 8, 9, 7, 13, 17, 16, 19])

    def test_contains_subtree_true(self):
        sub = BinarySearchTree()
        sub.create_nodes_from_list(vals=[17, 16, 19])
        self.assertTrue(self.bst.contains_subtree(sub))

    def test_contains_subtree_false(self):
        sub = BinarySearchTree()
        sub.create_nodes_from_list(vals=[15, 16, 19])
        self.assertFalse(self.bst.contains_subtree(sub))

    def test_lowest_common_ancestor_happy(self):
        self.assertEquals(self.bst.lowest_common_ancestor(val1=16, val2=19), 17)

    def test_lowest_common_ancestor_negative(self):
        self.assertNotEquals(self.bst.lowest_common_ancestor(val1=16, val2=19), 19)

    def tearDown(self):
        """
        Runs after every test
        :return:
        """
        pass