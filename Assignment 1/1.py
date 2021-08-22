list_numbers = list(map(int , input().split()))
unique_numbers = set(list_numbers)
dict_nums = {}
diff_nums = {}

for num in unique_numbers:
	dict_nums[num] = [-1]
	diff_nums[num] = []

i = 0

while(i < len(list_numbers)):
	diff_nums[list_numbers[i]].append(i - dict_nums[list_numbers[i]][-1])
	dict_nums[list_numbers[i]].append(i)
	i += 1

minimum = len(list_numbers) + 1
for num in dict_nums:
    diff_nums[num].append(len(list_numbers) - dict_nums[num][-1])
    max_diff = max(diff_nums[num])
    if(max_diff < minimum):
    	minimum = max_diff

print(minimum)