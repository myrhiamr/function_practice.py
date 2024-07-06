class Node:
	def __init__(self, data, reference=None):
		self.data = data
		self.reference = reference

node1 = Node(5)
node2 = Node(11)
node1.reference = node2
print(node1.reference.data)

class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def print_linked_list(self):
		if self.head = None:
			print('The linked list is empty')
		else:
            current_node = self.head
            print(self.head.data)
			current_node = current_node.reference