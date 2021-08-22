def combine_and_get_answer(first_stack , second_stack , top_fisrt_stack , top_second_stack):
	answer = ""
	while(top_fisrt_stack != 0):
		second_stack.append(first_stack.pop())
		top_second_stack += 1
		top_fisrt_stack -= 1

	while(top_second_stack != 0):
		answer += second_stack.pop()
		top_second_stack -= 1
	
	return answer

def find_correct_format(word):
	# Initilizing the stacks
	first_stack = []
	top_fisrt_stack = 0
	second_stack = []
	top_second_stack = 0

	for i in range(len(word)):
		if(word[i] == "L"):
			if(top_fisrt_stack != 0):
				second_stack.append(first_stack.pop())
				top_second_stack += 1
				top_fisrt_stack -= 1
		elif(word[i] == "R"):
			if(top_second_stack != 0):
				first_stack.append(second_stack.pop())
				top_fisrt_stack += 1
				top_second_stack -= 1
		else:
			first_stack.append(word[i])
			top_fisrt_stack += 1

	return combine_and_get_answer(first_stack , second_stack , top_fisrt_stack , top_second_stack)

print(find_correct_format(input()))