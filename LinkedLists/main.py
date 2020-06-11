from LinkedLists.LinkedList import LinkedList

ll = LinkedList()
ll.insert_at_head(0)
ll.insert_at_head(2)
ll.insert_at_head(4)
ll.insert_at_head(6)

node_at_2 = ll.get_node_at_index(2)
print(node_at_2)
