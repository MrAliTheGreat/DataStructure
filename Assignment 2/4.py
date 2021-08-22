def index2xy(index):
	return index // 3 , index % 3

def xy2index(x , y):
	return x * 3 + y

def is_in_board(next_x , next_y):
	if(next_x >= 0 and next_x < 3 and next_y >= 0 and next_y < 3):
		return True
	return False

def find_num_passwords(current_x , current_y , directions , previous_dir , move_values , used_nodes):
	num_passwords = 0
	if(xy2index(current_x , current_y) in used_nodes):
		return 0
	if(len(directions) == 0):
		possible_num = 0
		if(len(previous_dir) != 0 and is_in_board(current_x + move_values[previous_dir][0] , current_y + move_values[previous_dir][1])):
			possible_num = find_num_passwords(current_x + move_values[previous_dir][0] , current_y + move_values[previous_dir][1] , directions , directions , move_values , used_nodes + [xy2index(current_x , current_y)])
		return possible_num + 1

	if(is_in_board(current_x + move_values[directions[0]][0] , current_y + move_values[directions[0]][1])):
		num_passwords += find_num_passwords(current_x + move_values[directions[0]][0] , current_y + move_values[directions[0]][1] , directions[1:] , directions[0] , move_values , used_nodes + [xy2index(current_x , current_y)])

	if(previous_dir in move_values.keys() and is_in_board(current_x + move_values[previous_dir][0] , current_y + move_values[previous_dir][1])):
		num_passwords += find_num_passwords(current_x + move_values[previous_dir][0] , current_y + move_values[previous_dir][1] , directions , previous_dir , move_values , used_nodes + [xy2index(current_x , current_y)])

	return num_passwords	


directions = input()

move_values = {"R" : [0 , 1] , "L" : [0 , -1] , "U" : [-1 , 0] , "D" : [1 , 0]}
total_passwords = 0

for index in range(9):
	current_x , current_y = index2xy(index)
	total_passwords += find_num_passwords(current_x , current_y , directions , "" , move_values , [])

print(total_passwords)