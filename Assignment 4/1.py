class Node:
	def __init__(self , number , value1 , value2):
		self.number = number
		self.value1 = value1
		self.value2 = value2
		self.left = None
		self.right = None
		self.parent = 0

	
def insert_to_bst(bst , node , parent_num):
	if bst is None:
		bst = node
		bst.parent = parent_num
	else:
		if(node.value1 < bst.value1):
			bst.left = insert_to_bst(bst.left , node , bst.number)
		else:
			bst.right = insert_to_bst(bst.right , node , bst.number)
	return bst


def print_final_answer(nodes):
	print("YES")
	for node in nodes:
		if(node.left is None and node.right is None):
			print(str(node.parent) + " 0" + " 0")
		elif(node.left is not None and node.right is None):
			print(str(node.parent) + " " + str(node.left.number) + " 0")
		elif(node.left is None and node.right is not None):
			print(str(node.parent) + " 0 " + str(node.right.number))
		else:
			print(str(node.parent) + " " + str(node.left.number) + " " + str(node.right.number))



nodes = []
num_nodes = int(input())

for i in range(num_nodes):
	value1 , value2 = list(map(int , input().split()))
	nodes.append(Node(i + 1 , value1 , value2))

sorted_nodes = sorted(nodes , key = lambda node : node.value2)
for i in range(1 , num_nodes):
	insert_to_bst(sorted_nodes[0] , sorted_nodes[i] , 0)

print_final_answer(nodes)