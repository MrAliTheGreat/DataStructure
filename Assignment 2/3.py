def merge_subarrays(left_subarray , right_subarray , debug_line):
	merged_array = []
	while(len(left_subarray) != 0 and len(right_subarray) != 0):
		if(debug_line[0] == "L"):
			merged_array.append(left_subarray.pop(0))
			debug_line = debug_line[1:]
		elif(debug_line[0] == "R"):
			merged_array.append(right_subarray.pop(0))
			debug_line = debug_line[1:]

	if(len(right_subarray) == 0):
		merged_array.extend(left_subarray)
	elif(len(left_subarray) == 0):
		merged_array.extend(right_subarray)

	return merged_array , debug_line


def recover_array(unsorted_indices , start , end , debug_line):
	if(start >= end):
		return [unsorted_indices[start]] , debug_line

	mid = (start + end - 1) // 2
	left_subarray , debug_line = recover_array(unsorted_indices , start , mid , debug_line)
	right_subarray , debug_line = recover_array(unsorted_indices , mid + 1 , end , debug_line)
	return merge_subarrays(left_subarray , right_subarray , debug_line)

def print_answer(sorted_indices , num):
	final_answer = [""] * num
	for i in range(len(sorted_indices)):
		final_answer[sorted_indices[i]] = str(i + 1)

	print(" ".join(final_answer))


num = int(input())
debug_line = input()

unsorted_indices = list(range(num))
sorted_indices = recover_array(unsorted_indices , 0 , num - 1 , debug_line)[0]
print_answer(sorted_indices , num)