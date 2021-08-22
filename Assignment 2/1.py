import sys

sys.setrecursionlimit(100000)

def get_max_happiness(all_info , index_coworker , tree_level):
	if(all_info[index_coworker][1] == 0 and tree_level == 1):
		return 0 , 0
	elif(all_info[index_coworker][1] == 0 and tree_level != 1):
		return all_info[index_coworker][0] , 0

	node_included_happiness = 0
	node_excluded_happiness = 0

	for i in range(all_info[index_coworker][1]):
		node_happiness , node_child_happiness = get_max_happiness(all_info , all_info[index_coworker][2][i] , tree_level + 1)
		node_included_happiness += node_child_happiness
		node_excluded_happiness += max(node_happiness , node_child_happiness)

	if(tree_level == 1):
		return node_included_happiness , node_excluded_happiness

	return all_info[index_coworker][0] + node_included_happiness , node_excluded_happiness


num_people = int(input())
all_info = {}

for i in range(1 , num_people + 1):
	happiness , num_coworker = list(map(int , input().split()))
	if(num_coworker != 0):
		all_info[i] = (happiness , num_coworker , list(map(int , input().split())))
	else:
		all_info[i] = (happiness , num_coworker , 0)


print(max(get_max_happiness(all_info , 1 , 0)))
