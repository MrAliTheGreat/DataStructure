def index2xy(index , board_size):
	return index // board_size , index % board_size

def xy2index(x , y , board_size):
	return x * board_size + y

def is_in_board(board_size , x , y):
	if(x >= 0 and x < board_size and y >= 0 and y < board_size):
		return True
	return False

board_size , win_amount = list(map(int , input().split()))
board = []
for element in range(board_size):
	board.extend(input())

i = 0; k = 0 ; t = 0
num_X = 1
num_O = 1
moves_x = [0 , 0 , -1 , 1 , -1 , -1 , 1 , 1]
moves_y = [1 , -1 , 0 , 0 , 1 , -1 , -1 , 1]
possible_X = False
possible_O = False

while(i < len(board)):
	if(board[i] == 'X'):
		while(k < len(moves_x)):
			pos_x , pos_y = index2xy(i , board_size)
			for _ in range(win_amount - 1):
				if(is_in_board(board_size , pos_x + moves_x[k] , pos_y + moves_y[k])):
					if(board[xy2index(pos_x + moves_x[k] , pos_y + moves_y[k] , board_size)] == 'X'):
						num_X += 1				
					elif(board[xy2index(pos_x + moves_x[k] , pos_y + moves_y[k] , board_size)] == 'O'):
						pos_x += moves_x[k]
						pos_y += moves_y[k]						
						break
				pos_x += moves_x[k]
				pos_y += moves_y[k]
			
			if(num_X == win_amount):
				break
			elif(num_X == win_amount - 1 and is_in_board(board_size , pos_x , pos_y )):
				if(board[xy2index(pos_x , pos_y , board_size)] != 'O'):
					possible_X = True
			num_X = 1
			k += 1
		k = 0
	
	if(num_X == win_amount):
		print("Finished")
		break

	if(board[i] == 'O'):
		while(t < len(moves_x)):
			pos_x , pos_y = index2xy(i , board_size)
			for _ in range(win_amount - 1):
				if(is_in_board(board_size , pos_x + moves_x[t] , pos_y + moves_y[t])):
					if(board[xy2index(pos_x + moves_x[t] , pos_y + moves_y[t] , board_size)] == 'O'):
						num_O += 1
					elif(board[xy2index(pos_x + moves_x[t] , pos_y + moves_y[t] , board_size)] == 'X'):
						pos_x += moves_x[t]
						pos_y += moves_y[t]						
						break
				pos_x += moves_x[t]
				pos_y += moves_y[t]
			
			if(num_O == win_amount):
				break
			elif(num_O == win_amount - 1 and is_in_board(board_size , pos_x , pos_y)):
				if(board[xy2index(pos_x , pos_y , board_size)] != 'X'):
					possible_O = True
			num_O = 1
			t += 1
		t = 0
	
	if(num_O == win_amount):
		print("Finished")
		break
	i += 1

if(not(num_X == win_amount or num_O == win_amount) ):
	if(possible_X and possible_O):
		print("Both")
	elif(possible_X and (not(possible_O)) ):
		print("X")
	elif(possible_O and (not(possible_X)) ):
		print("O")
	else:
		print("None")
