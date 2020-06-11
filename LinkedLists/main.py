from LinkedLists.LinkedList import LinkedList

ll = LinkedList()
# ll.insert_at_head(0)
# ll.insert_at_head(2)
# ll.insert_at_head(4)
# ll.insert_at_head(6)
ll.append_from_list([0, 2, 4, 6])
ll.append_from_list([8, 10, 12, 14])
print(ll)