def determine_status(expression):
	if(expression[0] == "*" or expression[0] == "/" or expression[0] == "+" or expression[0] == "-"):
		return 0;
	return 1

def reverse_expression(expression):
	new_expression = ""
	for i in range(len(expression)):
		if(expression[len(expression) - 1 - i] == "("):
			new_expression += ")"
		elif(expression[len(expression) - 1 - i] == ")"):
			new_expression += "("
		else:
			new_expression += expression[len(expression) - 1 - i]
	return new_expression

def get_priority(character):
	if(character == "+" or character == "-"):
		return 1
	elif(character == "*" or character == "/"):
		return 2
	return 0

def is_operand(character):
	if(character == "+" or character == "-" or character == "*" or character == "/" or character == "(" or character == ")"):
		return False
	return True

def add_remaining(stack , stack_top , prefix):
	while(stack_top != 0):
		prefix += stack.pop()[0]
		stack_top -= 1
	return prefix

def infix2prefix(expression):
	new_expression = reverse_expression(expression)
	prefix = ""

	stack = []
	stack_top = 0

	for i in range(len(new_expression)):
		if(is_operand(new_expression[i])):
			prefix += new_expression[i]
		else:
			if(new_expression[i] == "("):
				stack.append(("(" , 0 , len(expression) - 1 - i))
				stack_top += 1
			elif(new_expression[i] == ")"):
				while(stack[-1][0] != "("):
					prefix += stack.pop()[0]
					stack_top -= 1
				stack.pop()
				stack_top -= 1
			else:
				if(stack_top == 0):
					stack.append((new_expression[i] , get_priority(new_expression[i]) , len(expression) - 1 - i))
					stack_top += 1
				elif(stack[-1][0] == "("):
					stack.append((new_expression[i] , get_priority(new_expression[i]) , len(expression) - 1 - i))
					stack_top += 1
				else:
					while(stack_top != 0 and stack[-1][1] >= get_priority(new_expression[i])):
						if(stack[-1][1] == get_priority(new_expression[i])):
							if(stack[-1][2] > len(expression) - 1 - i):
								break
						prefix += stack.pop()[0]
						stack_top -= 1
					stack.append((new_expression[i] , get_priority(new_expression[i]) , len(expression) - 1 - i))
					stack_top += 1

	return reverse_expression(add_remaining(stack , stack_top , prefix))


def prefix2postfix(expression):
	stack = []
	stack_top = 0

	for i in range(len(expression)):
		if(is_operand(expression[len(expression) - 1 - i])):
			stack.append(expression[len(expression) - 1 - i])
			stack_top += 1
		else:
			stack.append(stack.pop() + stack.pop() + expression[len(expression) - 1 - i])
			stack_top -= 1

	return stack.pop()


expression = input()
if(determine_status(expression)):
	print(infix2prefix(expression))
else:
	print(prefix2postfix(expression))