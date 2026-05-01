import random


## 3.5.2

# lst = [2,4,6,8,10]
# for i in range (len(lst)-1):
#     if lst[i] > lst[i+1]:
# 	    lst[i] = lst[i+1]
# 	    lst[i+1] = lst[i]
# print(lst)

##3.5.2
# lst =[9,3,7,5]
# swapped = True
# while swapped:
# 	swapped = False
# 	for i in range(len(lst)-1):
# 		if lst[i] <  lst[i+1]:
# 			swapped = True
# 			lst[i],lst[i+1] = lst[i+1],lst[i]
# print(lst)

##3.5.3
# lst = []
# swapped = True
# list_len = int(input("Enter the Number of the Items that a lis would contain"))
#
# for i in range(list_len):
# 	list_item = int(input("Enter the Item Number"))
# 	lst.append(list_item)
# while swapped:
# 	swapped = False
# 	for i in range(len(lst) - 1):
# 		if lst[i] > lst[i + 1]:
# 			swapped = True
# 			lst[i], lst[i + 1] = lst[i + 1], lst[i]
#
# print(lst)


# Selection sort
# arr = [29, 10, 14, 37, 13]
# swap = 0
# for i in range (len(arr)):
# 	min_indx= i
# 	for j in range(i+1, len(arr)):
# 		if arr[j] > arr[min_indx]:
# 			min_indx = j
# 	if min_indx != i:
# 		swap += 1
# 	arr[i] ,arr[min_indx] = arr[min_indx],arr[i]
# print(arr, swap)
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-1:1]
# print(new_list)

#3.6.5
# lst = [17,3,5,18,9]
# to_find = 20
# found = False
# for i in range(len(lst)):
# 	found =  lst[i] == to_find
# 	if found:
# 		break
# if found:
# 	print("Element found at index: ", i)
# else:
# 	print("Element not found")

#3.6.6
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# temp_list = []
#
# for item in my_list:
# 	if item not in temp_list:
# 		temp_list.append(item)
# print(temp_list)

# ## 3.7 List Comprehension
# lst = [3,-1,5,-2,0,8]
# nums = [x for x in lst if x > 0]
# print(nums)

#2
# words =["hello", "hi", "Bye"]
# lengths = [len(x) for x in words]
# print(lengths)

#3
# words = ["hey", "hello", "ttt"]
# loud = [x.upper() for x in words if len(x) > 4]
# print(loud)

# #4
# #FizzBuzz
# fizz = ["FizzBuzz" if x % 3 == 0 and x % 5 ==0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else  x for x in range(1,21) ]
# print(fizz)


#2D Lists
# twoDlist = [[0 for x in range(3)] for x in range(2)]
# print(twoDlist)

# twoDlist = [[x * 2 for x in range(1,3)] for x in range(3)]
# sum = 0
# for i in twoDlist:
# 	for j in i:
# 		sum += j
# print(sum)

# tic = [['.' for col in range(3)] for row in range(3)]
# tic[0][2] = 'O'
# tic[1][1] = 'X'
# for row in tic:
# 	print(row)




def draw_board(board):
	for i in range (3):
		print ("+------", end="")
	print ("+")
	for j in range (len(board)):
		for i in range(len(board[j])):
			print ("|      ", end="")
		print ("|")
		for i in range (3):
			counter = board[j][i]
			print ("|" + counter.center (6), end="")
		print ("|")
		for i in range (3):
			print ("|      ", end="")
		print ("|")
		for i in range (3):
			print ("+------", end="")
		print ("+")

def user_input():
	try:
		input_user = int (input ("Enter Number between 1 and 9: "))
		if input_user < 1 or input_user > 9:
			print ("Please enter a number between 1 and 9.")
			return user_input ()
		else:
			row = (input_user - 1) // 3
			col = (input_user - 1) % 3
			return (row, col)
	except ValueError:
		print ("Please enter a number between 1 and 9. Not a string or Character")
		return user_input ()

def make_user_move(board):
	input_validation_flag = True
	while input_validation_flag:
		option = user_input()
		if board[option[0]][option[1]] == "X" or board[option[0]][option[1]] == "O":
			print("This option on the board is already taken.\n")
			continue
		else:
			board[option[0]][option[1]] = "X"
			break
	return board


def make_computer_move(board):
	empty_cells = [(row,col) for row in range (3) for col  in range(3) if board[row][col] != "X" and board[row][col] != "O"]
	winning_cells = []
	for i in range(len(empty_cells)):
		original_val = board[empty_cells[i][0]][empty_cells[i][1]]
		board[empty_cells[i][0]][empty_cells[i][1]] = "O"
		result = check_winner(board)
		board[empty_cells[i][0]][empty_cells[i][1]] = original_val
		if result == 'O':
			winning_cells.append(empty_cells[i])
	blocking_cells = []
	for i in range(len(empty_cells)):
		original_val = board [empty_cells [i] [0]] [empty_cells [i] [1]]
		board[empty_cells[i][0]][empty_cells[i][1]] = "X"
		result = check_winner(board)
		board[empty_cells[i][0]][empty_cells[i][1]] = original_val
		if result == "X":
			blocking_cells.append(empty_cells[i])
	if winning_cells:
		option = random.choice(winning_cells)
	elif blocking_cells:
		option = random.choice(blocking_cells)
	else:
		option = random.choice(empty_cells)
	board[option[0]][option[1]] = "O"
	return board


def check_winner(board):
	# Row Check
	for row in range (3):
		row_list = []
		for col in range (3):
			if board[row][col] not in row_list:
				row_list.append(board[row][col])
		if len(row_list) == 1:
			return row_list[0]
	# Column Check
	for row in range (3):
		col_list = []
		for col in range (3):
			if board[col][row] not in col_list:
				col_list.append(board[col][row])
		if len(col_list) == 1:
			return col_list[0]
	# Diagonal Check
	diagonal_list_a = []
	for row in range (3):
		if board[row][row] not in diagonal_list_a:
			diagonal_list_a.append(board[row][row])
	if len(diagonal_list_a) == 1:
		return diagonal_list_a[0]
	#Diagonal B
	diagonal_list_b = []
	for row in range (3):
		if board[row][2-row] not in diagonal_list_b:
			diagonal_list_b.append(board[row][2-row])
	if len(diagonal_list_b) == 1:
			return diagonal_list_b[0]

def check_draw(board):
	empty_cells = []
	for row in range (3):
		for col in range (3):
			if board [row] [col] != "X" and board [row] [col] != "O":
				empty_cells.append((row,col))
	winner = check_winner(board)
	return  len(empty_cells) == 0 and winner == None

def play_tic_tac_toe(board):
	# Draw Board
	draw_board(board)
	cont_flag = True
	while cont_flag:
		# Player Move
		make_user_move(board)
		draw_board(board)
		u_winner_flag = check_winner(board)
		u_draw_flag = check_draw(board)
		if u_winner_flag:
			print("Congratulations! You win!")
			cont_flag = False
		elif u_draw_flag:
			print("Its a draw!")
			cont_flag = False
		else:
			# Computer Move
			make_computer_move (board)
			print("---------------- Com puter Move ------------------")
			draw_board (board)
			c_winner_flag = check_winner (board)
			c_draw_flag = check_draw (board)
			if c_winner_flag:
				print ("Computer wins! Try next time.")
				cont_flag = False
			elif c_draw_flag:
				print ("Its a draw!")
				cont_flag = False

def ask_user():
	u_input = input ("Y to play again:  N to Quit")
	if u_input == "y" or u_input == "Y":
		return True
	else:
		return False

while True:
    play_tic_tac_toe([["1","2","3"],
                      ["4","5","6"],
                      ["7","8","9"]])
    if not ask_user():
        print("Thanks for playing! Goodbye!")
        break

	