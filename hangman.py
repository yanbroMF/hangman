from random import randint

def start_game(word):
	wrong = 0;
	letters = list(word)
	board = ["__"] * len(word)
	stages = [
	"""
	______________
	|
	|
	|
	|
	|
	|
	|
	|
	|________
	""",
	"""
	______________
	|            |
	|            |
	|            |
	|
	|
	|
	|
	|
	|________
	""",
	"""
	______________
	|            |
	|            |
	|            |
	|            0
	|
	|
	|
	|
	|________
	""",
	"""
	______________
	|            |
	|            |
	|            |
	|            0
	|            |
	|
	|
	|
	|________
	""",
	"""
	______________
	|            |
	|            |
	|            |
	|            0
	|           /|
	|
	|
	|
	|________
	""",
	"""
	______________
	|            |
	|            |
	|            |
	|            0
	|           /|\\
	|
	|
	|
	|________
	""",
	"""
	______________
	|            |
	|            |
	|            |
	|            0
	|           /|\\
	|           /
	|
	|
	|________
	""",	
	"""
	______________
	|            |
	|            |
	|            |
	|            0
	|           /|\\
	|           / \\
	|
	|
	|________
	"""]
	while True:
		cur_let = input("-------------------\nEnter the letter: ")
		if cur_let in letters:
			i = letters.index(cur_let)
			board[i] = cur_let
			letters[i] = "$"
		else:
			wrong += 1
		print(" ".join(board))
		print(stages[wrong])
		if "__" not in board:
			print("The word was {}".format(word.upper()))
			print("-------------------\n        YOU WIN!!!\n-------------------")
			break
		elif wrong == len(stages) - 1:
			print("The word was {}".format(word.upper()))
			print("-------------------\n         YOU LOSE\n-------------------")
			break

list_of_words = ["cat", "tree", "house", "elephant", "computer", "user", "mouse", "bread", "bird", "league", "paperwork", "agreement", "mail", "snake", "chiken", "tomato", "music", "advertisement", "horse", "neighbour"]
start_game(list_of_words[randint(0, len(list_of_words) - 1)])

