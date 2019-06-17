# Tic-Tac-Toe
# By Davis "Lucky" Lai
import sys

def main():
	board = [["A1", "A2","A3"],["B1","B2","B3"],["C1","C2","C3"]]
	turn = 1
	player = 1
	marker = "-"
	while (turn <= 9):
		print("Turn:",turn," - Player",player)
		row, column = printinstructions(player, board)
		if (player==1):
			marker = "X "
		elif(player==2):
			marker = "O "
		board[row][column] = marker
		player = (player%2) + 1
		turn = turn + 1
		checkwin(board)
	printboard(board)
	print("No Winner. Game Ends In Draw")
	sys.exit(0)

def printinstructions(player, board):
	printboard(board)
	searching = True
	column = 10
	row = 10
	while (searching == True):
		choice = input("Player please enter the coordinates of your choice: ")
		if (choice[0]=="A" or choice[0]=="a"):
			row = 0
		elif(choice[0]=="B" or choice[0]=="b"):
			row = 1
		elif(choice[0]=="C" or choice[0]=="c"):
			row = 2
		else:
			print("You did not enter a valid row coordinate!!!")

		try:	
			column = eval(choice[1]) - 1
			if (column>=3):
				print("You did not enter a valid column coordinate!!!")
		except:
			print("You did not enter a valid column coordinate!!!")

		if (column<=2 and row<=2):
			if (board[row][column] != "X " and board[row][column] != "O "):
				searching = False
	return row, column

def printboard(board):
	print("",board[0][0]," | ",board[0][1]," | ",board[0][2])
	print("-------------------")
	print("",board[1][0]," | ",board[1][1]," | ",board[1][2])
	print("-------------------")
	print("",board[2][0]," | ",board[2][1]," | ",board[2][2])

def checkwin(board):
	print("Checking for win")
	winner=""
	for row in range(0,2):
		if (board[row][0]==board[row][1] and board[row][1]==board[row][2]):
			winner = board[row][0]
			break

	for column in range(0,2):
		if (board[0][column]==board[1][column] and board[1][column]==board[2][column]):
			winner = board[0][column]
			break

	if (board[0][0]==board[1][1] and board[1][1]==board[2][2]):
		winner = board[1][1]
	if (board[0][2]==board[1][1] and board[1][1]==board[2][0]):
		winner = board[1][1]

	if (winner=="X "):
		print("Player 1 Wins!!!")
		printboard(board)
		sys.exit(0)
	if (winner=="O "):
		print("Player 2 Wins!!!")
		printboard(board)
		sys.exit(0)


main()
