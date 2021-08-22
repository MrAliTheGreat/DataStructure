class Node():
	def __init__(self, value):
		# 0: Black , 1: Red
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.color = 1

class RB_Tree():
	def __init__(self):
		self.root = None



def right_rotate(tree , target_node):
	replace_node = target_node.left
	if(target_node.parent == None):
		tree.root = replace_node
	else:
		if(target_node.parent.left == target_node):
			target_node.parent.left = replace_node
		else:
			target_node.parent.right = replace_node
	
	replace_node.parent = target_node.parent
	target_node.parent = replace_node

	target_node.left = replace_node.right
	
	if(replace_node.right != None):
		replace_node.right.parent = target_node
	
	replace_node.right = target_node


def left_rotate(tree , target_node):
	replace_node = target_node.right
	if(target_node.parent == None):
		tree.root = replace_node
	else:
		if(target_node.parent.left == target_node):
			target_node.parent.left = replace_node
		else:
			target_node.parent.right = replace_node		
	
	replace_node.parent = target_node.parent
	target_node.parent = replace_node

	target_node.right = replace_node.left
	
	if(replace_node.left != None):
		replace_node.left.parent = target_node
	
	replace_node.left = target_node


def search_BST(bst , node_value):
	if(bst == None):
		return None

	if(bst.value == node_value):
		return bst

	if(node_value < bst.value):
		return search_BST(bst.left , node_value)

	return search_BST(bst.right , node_value)


def insert_BST(bst , node , parent_node):
	if(bst == None):
		node.parent = parent_node
		return node

	if(node.value < bst.value):
		bst.left = insert_BST(bst.left , node , bst)
	elif(node.value > bst.value):
		bst.right = insert_BST(bst.right , node , bst)

	return bst


def make_new_tree_RB_insert(tree , troubled_node):
	if(troubled_node == tree.root):
		troubled_node.color = 0
	else:
		parent = troubled_node.parent
		if(parent.color == 1):
			grandpa = troubled_node.parent.parent
			if(troubled_node.parent == None or troubled_node.parent.parent == None):
				uncle = None
			elif(troubled_node.parent.parent.left == troubled_node.parent):
				uncle = troubled_node.parent.parent.right		
			elif(troubled_node.parent.parent.right == troubled_node.parent):
				uncle = troubled_node.parent.parent.left

			if(uncle != None and uncle.color == 1):
				uncle.color = 0
				grandpa.color = 1
				parent.color = 0
				make_new_tree_RB_insert(tree , grandpa)
			else:
				if(parent.parent.right == parent):
					if(troubled_node.parent.right == troubled_node):
						temp_color = parent.color
						parent.color = grandpa.color
						grandpa.color = temp_color
					
					elif(troubled_node.parent.left == troubled_node):
						right_rotate(tree , parent)
						temp_color = troubled_node.color
						troubled_node.color = grandpa.color
						grandpa.color = temp_color

					left_rotate(tree , grandpa)

				elif(parent.parent.left == parent):
					if(troubled_node.parent.left == troubled_node):
						temp_color = parent.color
						parent.color = grandpa.color
						grandpa.color = temp_color
					
					elif(troubled_node.parent.right == troubled_node):
						left_rotate(tree , parent)
						temp_color = troubled_node.color
						troubled_node.color = grandpa.color
						grandpa.color = temp_color

					right_rotate(tree , grandpa)					


def insert_RBtree(tree , node_value):
	new_node = Node(node_value)  # Color is red by default
	if(tree.root == None):
		new_node.color = 0
		tree.root = new_node
	else:
		insert_BST(tree.root , new_node , None)
		make_new_tree_RB_insert(tree , new_node)


def make_new_tree_RB_delete(tree , node):
	if(node == tree.root):
		return

	if(node.parent == None):
		brother_node = None
	elif(node.parent.left == node):
		brother_node = node.parent.right
	elif(node.parent.right == node):
		brother_node = node.parent.left

	if(brother_node == None):
		make_new_tree_RB_delete(node.parent)
	else:
		if(brother_node.color == 1):
			node.parent.color = 1
			brother_node.color = 0
			if(brother_node.parent.left == brother_node):
				right_rotate(tree , brother_node.parent)
			
			elif(brother_node.parent.right == brother_node):
				left_rotate(tree , brother_node.parent)
			
			make_new_tree_RB_delete(tree , node)

		elif(brother_node.color == 0):
			if(brother_node.left != None and brother_node.left.color == 1):
				parent_node = node.parent
				if(brother_node.parent.left == brother_node):
					brother_node.left.color = brother_node.color
					brother_node.color = brother_node.parent.color
					right_rotate(tree , brother_node.parent)
				
				elif(brother_node.parent.right == brother_node):
					brother_node.left.color = brother_node.parent.color
					right_rotate(tree , brother_node)
					left_rotate(tree , parent_node)
				
				parent_node.color = 0
			
			elif(brother_node.right != None and brother_node.right.color == 1):
				parent_node = node.parent
				if(brother_node.parent.left == brother_node):
					brother_node.right.color = brother_node.parent.color
					left_rotate(tree , brother_node)
					right_rotate(tree , parent_node)
				
				elif(brother_node.parent.right == brother_node):
					brother_node.right.color = brother_node.color
					brother_node.color = brother_node.parent.color
					left_rotate(tree , brother_node.parent)
				
				parent_node.color = 0
			
			else:
				brother_node.color = 1
				if(brother_node.color == 1):
					brother_node.parent.color = 0
				elif(brother_node.color == 0):
					make_new_tree_RB_delete(tree , brother_node.parent)


def delete_RBtree(tree , node_value):
	if(tree.root == None):
		return

	delete_node = search_BST(tree.root , node_value)
	if(delete_node == None):
		return

	if(delete_node.left == None and delete_node.right == None):
		replace_node = None
	elif(delete_node.left == None and delete_node.right != None):
		replace_node = delete_node.right
	elif(delete_node.left != None and delete_node.right == None):
		replace_node = delete_node.left
	else:
		traverse_node = delete_node.right
		while(traverse_node.left != None):
			traverse_node = traverse_node.left
		replace_node = traverse_node

	if(delete_node.right == None and delete_node.left == None):
		if(delete_node == tree.root):
			tree.root = None
		else:
			if(delete_node.color == 0 and (replace_node == None or replace_node.color == 0)):
				make_new_tree_RB_delete(tree , delete_node)
		
		if(delete_node.parent.left == delete_node):
			delete_node.parent.left = None
		elif(delete_node.parent.right == delete_node):
			delete_node.parent.right = None
		del delete_node
	
	elif(delete_node.right == None or delete_node.left == None):
		if(delete_node == tree.root):
			delete_node.value = replace_node.value
			delete_node.left = None
			delete_node.right = None
			del replace_node
		else:
			if(delete_node.parent.left == delete_node):
				delete_node.parent.left = replace_node
			elif(delete_node.parent.right == delete_node):
				delete_node.parent.right = replace_node
			replace_node.parent = delete_node.parent
			del delete_node

			if(delete_node.color == 0 and (replace_node.color == 0 or replace_node == None)):
				make_new_tree_RB_delete(tree , replace_node)
			else:
				replace_node.color = 0
	
	elif(delete_node.right != None and delete_node.left != None):
		temp_value = delete_node.value
		delete_node.value = replace_node.value
		replace_node.value = temp_value
		delete_RBtree(tree , replace_node.value)


def print_RBtree(tree):
	tree_string = ""
	queue = []

	queue.append(tree.root)
	while(len(queue) != 0):
		node = queue.pop(0)
		if(node.color == 0):
			tree_string += (str(node.value) + "b ")
		else:
			tree_string += (str(node.value) + "r ")

		if(node.left != None):
			queue.append(node.left)

		if(node.right != None):
			queue.append(node.right)

	print(tree_string[0 : len(tree_string) - 1])



tree = RB_Tree()
while(True):
	try:
		operation = input().split()

		if(operation[0] == "insert"):
			insert_RBtree(tree , int(operation[1]))
		elif(operation[0] == "delete"):
			delete_RBtree(tree , int(operation[1]))
		elif(operation[0] == "print"):
			print_RBtree(tree)		
	except:
		break
