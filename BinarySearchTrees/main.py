from BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()
bst.create_nodes_from_list(vals=[10, 15, 8, 9, 7, 13, 17, 16, 19])
bst.lowest_common_ancestor(val1=16, val2=19)



# bst.print_inorder()
# bst.print_postorder()
# bst.print_preorder()
# bst.print_breadth()
# bst.print_tree_height()