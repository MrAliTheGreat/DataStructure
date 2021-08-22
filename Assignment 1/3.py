def index2xy(index , board_y):
	return index // board_y , index % board_y

def xy2index(x , y , board_y):
	return x * board_y + y

def is_in_board(index , length_board):
	if(index >= 0 and index < length_board):
		return True
	return False

def covered_row(board , element , element_x , board_x , board_y):
	counter = 0
	if(board_y == 1):
		for i in range(board_x):
			if(is_in_board(element_x + i , len(board)) ):
				if(board[element_x + i] == element):
					counter += 1
		if(counter == 1):
			return True
		return False

	for i in range(board_y):
		if(is_in_board(element_x * board_y + i , len(board)) ):
			if(board[element_x * board_y + i] == element):
				counter += 1
	
	if(counter == board_y):
		return True
	return False	

def covered_column(board , element , element_y , board_x , board_y):
	counter = 0
	if(board_x == 1):
		for i in range(board_y):
			if(is_in_board(element_x + i , len(board)) ):
				if(board[element_x + i] == element):
					counter += 1
		if(counter == 1):
			return True
		return False
	
	for i in range(board_x):
		if(is_in_board(element_y + i * board_y , len(board)) ):
			if(board[element_y + i * board_y] == element):
				counter += 1
	
	if(counter == board_x):
		return True
	return False
	

board_x , board_y = list(map(int , input().split()))
board = []
for _ in range(board_x):
	board.extend(list(map(int , input().split())))

order_colors = []

while(len(board) > 0):

	elements_board = list(set(board))
	elements_board.sort(reverse = True)
	for element in elements_board:

		element_index = board.index(element)
		element_x , element_y = index2xy(element_index , board_y)

		if(covered_row(board , element , element_x , board_x , board_y) ):
			del board[element_index : element_index + board_y]
			order_colors.append(element)
			board_x -= 1
			break
		elif(covered_column(board , element , element_y , board_x , board_y)):
			del board[element_index : element_index + board_x * board_y : board_y]
			order_colors.append(element)
			board_y -= 1
			break

print(' '.join(list(map(str , order_colors[::-1]))))