def get_max_remaining(heights , stack_heights , stack_heights_top , index , largest_poster):
	while(stack_heights_top != 0):
		if(stack_heights_top == 1):
			poster = heights[stack_heights.pop()] * index
			stack_heights_top -= 1
		else:
			poster = heights[stack_heights.pop()] * (index - 1 - stack_heights[-1])
			stack_heights_top -= 1

		if(poster > largest_poster):
			largest_poster = poster

	return largest_poster


def find_largest_poster(heights):
	# Initializing Stack
	stack_heights = []
	stack_heights_top = 0
	largest_poster = -1

	stack_heights.append(0)
	stack_heights_top += 1

	index = 1
	while index < len(heights):
		if(stack_heights_top == 0):
			stack_heights.append(index)
			stack_heights_top += 1
			index += 1

		elif(heights[index] >= heights[stack_heights[-1]]):
			stack_heights.append(index)
			stack_heights_top += 1
			index += 1

		elif(heights[index] < heights[stack_heights[-1]]):
			if(stack_heights_top == 1):
				poster = heights[stack_heights.pop()] * index
				stack_heights_top -= 1
			else:
				poster = heights[stack_heights.pop()] * (index - 1 - stack_heights[-1])
				stack_heights_top -= 1

			if(poster > largest_poster):
				largest_poster = poster

	return get_max_remaining(heights , stack_heights , stack_heights_top , index , largest_poster)

answers = []
num_posters = int(input())
for _ in range(num_posters):
	answers.append(find_largest_poster(list(map(int , input().split()))))

for i in range(num_posters):
	print(answers[i])