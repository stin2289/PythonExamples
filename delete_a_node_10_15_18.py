class Node():
	def __init__(self, value=None):
		self.value = value
		self.next = None


class NodeOperations():
	def deleteNode(self,head,deleteNode):
		if deleteNode == head:
			print("hitting this!" + str(head))
			del head
			del deleteNode
			#print head
			return

		runnerNode = head
		currentNode = head

		while currentNode != None:
			
			#move runner if it doesn't equal current node
			if currentNode != runnerNode:
				runnerNode = runnerNode.next

			currentNode = currentNode.next

			#make sure we're in valid state to check
			if runnerNode != None and deleteNode == currentNode:
				runnerNode.next = currentNode.next
				currentNode = None
				break

	def deleteNodeWithoutHead(self,deleteNode):
		deleteNode.value = deleteNode.next.value
		deleteNode.next = deleteNode.next.next

	def printNodes(self,head):
		print("Printing linked list")
		
		while head != None:
			print(head.value)
			head = head.next




print("Create linked list")
node1 = Node(1)
node1.next = Node(2)
node1.next.next = Node(3)
node3 = node1.next.next
node3.next = Node(4)

print("Delete node 3")
operations = NodeOperations()
operations.printNodes(node1)
operations.deleteNode(node1,node3)
operations.printNodes(node1)

print("")
print("Create second linked list")
node1 = Node(1)
node1.next = Node(2)
node2 = node1.next

print("Delete node 3, from second linked list")
operations = NodeOperations()
operations.printNodes(node1)
operations.deleteNode(node1,node2)
operations.printNodes(node1)

print("")
print("Create third linked list")
node5 = Node(1)

print("Delete node 1, from third linked list")
operations = NodeOperations()
operations.printNodes(node5)
print(node5)
operations.deleteNode(node5,node5)
print(node5)
operations.printNodes(node5)

print("Create fourth linked list")
operations = NodeOperations()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = None
operations.printNodes(node1)

print("Delete node 2")
operations.deleteNodeWithoutHead(node2)
operations.printNodes(node1)




			