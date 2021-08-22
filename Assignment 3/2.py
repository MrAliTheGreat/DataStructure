import sys
sys.setrecursionlimit(150000)

# !!! MERGE SORT FOR ARRAY NOT DOUBLY LINKEDLIST !!!
# def merge_subarrays(left_subarray , right_subarray):
# 	merged_array = []
# 	i = 0 ; j = 0
# 	while(i < len(left_subarray) and j < len(right_subarray)):
# 		if(left_subarray[i] <= right_subarray[j]):
# 			merged_array.append(left_subarray[i])
# 			i += 1
# 		else:
# 			merged_array.append(right_subarray[j])
# 			j += 1
# 	if(i == len(left_subarray) and j != len(right_subarray)):
# 		merged_array.extend(right_subarray[j:])
# 	elif(j == len(right_subarray) and i != len(left_subarray)):
# 		merged_array.extend(left_subarray[i:])

# 	return merged_array

# def merge_sort(numbers , start , end):
# 	if(start >= end):
# 		return [numbers[start]]

# 	mid = (start + end) // 2
# 	left_subarray = merge_sort(numbers , start , mid)
# 	right_subarray = merge_sort(numbers , mid + 1 , end)
# 	return merge_subarrays(left_subarray , right_subarray)

class Node:
	def __init__(self , value):
		self.value = value
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self , value):
		new_node = Node(value)
		new_node.next = None

		if(self.head == None):
			new_node.prev = None
			self.head = new_node
			self.tail = new_node
			return

		new_node.prev = self.tail
		self.tail.next = new_node
		self.tail = new_node

	def divide_list(self , head_list):
		head_i = head_list
		head_j = head_list
		while(head_j.next != None and head_j.next.next != None):
			head_i = head_i.next
			head_j = head_j.next.next

		right_head_list = head_i.next
		right_head_list.prev = None
		head_i.next = None
		return right_head_list

	def merge_linkedlists(self , head_list , right_head_list , left_tail , right_tail):
		if(right_head_list == None):
			self.tail = left_tail
			return head_list , self.tail
		elif(head_list == None):
			self.tail = right_tail
			return right_head_list , self.tail

		if(head_list.value < right_head_list.value):
			head_list.next , self.tail = self.merge_linkedlists(head_list.next, right_head_list , left_tail , right_tail) 
			head_list.next.prev = head_list 
			head_list.prev = None
			return head_list , self.tail
		else:
			right_head_list.next , self.tail = self.merge_linkedlists(head_list , right_head_list.next , left_tail , right_tail)
			right_head_list.next.prev = right_head_list
			right_head_list.prev = None
			return right_head_list , self.tail


	def merge_sort(self , head_list):
		if(head_list == None or head_list.next == None):
			return head_list , head_list

		right_head_list = self.divide_list(head_list)
		head_list , left_tail = self.merge_sort(head_list)
		right_head_list , right_tail = self.merge_sort(right_head_list)
		new_head , new_tail = self.merge_linkedlists(head_list , right_head_list , left_tail , right_tail)
		return new_head , new_tail

	def find_target_numbers(self , target_sum):
		help_head = self.head
		help_tail = self.tail

		while(help_head.value < help_tail.value):
			if(help_head.value + help_tail.value < target_sum):
				help_head = help_head.next
			elif(help_head.value + help_tail.value > target_sum):
				help_tail = help_tail.prev
			elif(help_head.value + help_tail.value == target_sum):
				answer = ""
				answer += (str(help_head.value) + " " + str(help_tail.value))
				return answer
		return "NO"



linked_list_len , target_sum = list(map(int , input().split()))
numbers = list(map(int , input().split("-")))

# !!! MERGE SORT FOR ARRAY NOT DOUBLY LINKEDLIST !!!
# numbers = merge_sort(numbers , 0 , linked_list_len - 1)

linked_list = DoublyLinkedList()
for num in numbers:
	if(num > target_sum):
		continue
	linked_list.append(num)

linked_list.head , linked_list.tail = linked_list.merge_sort(linked_list.head)
print(linked_list.find_target_numbers(target_sum))
