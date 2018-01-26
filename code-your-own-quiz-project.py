
###EASY
quiz_easy = '''__1__ means friendly association, especially with people who share one's interest.
__2__ means an unusual and exciting or daring experience. 
__3__ is characterized by resolute fearlessness, fortitude, and endurance. 
__4__ is one that is an autonomous creative force or decisive power. 
__5__ is marked by or given to strikingly elaborate or colorful display or behaviour.\n'''

answer_easy = ['fellowship', 'adventure', 'intrepid', 'demiurge', 'flamboyant']

###MEDIUM
quiz_medium = '''	Truly, "__1__ are things." And powerful things, when they are mixed with __2__ of purpose,
__3__ and a __4__ desire for their translation into riches or other material objects.\n

	Some years ago, Edwin C. Barnes discovered how true it is that you really can think and grow rich. His discovery did not come
about at __5__ sitting. It came little by little, beginning with a __4__ desire to become a business associate of the great Thomas Edison.
One of the chief characteristics of Barnes' desire was that it was definite. \n'''

answer_medium = ['thoughts', 'definiteness', 'persistence', 'burning', 'one', ]

###HARD
quiz_hard = '''__1__ is the point in the orbit of an object orbiting the earth that is nearest to the center of the earth.
__2__ is the point in the orbit of an object orbiting the earth that is at the greatest distance from the center of the earth.
__3__ means to be lavish with one's attention, fondness, or affection.
__4__ means exhibiting mature qualities at an unusually early age.
__5__ is an expression of strong disapproval.
 ''' 

answer_hard = ['perigee', 'apogee', 'dote', 'precocious', 'indictment']

blank_space1 = ['__1__', '__2__', '__3__', '__4__', '__5__']



def diff_level():
	#output: difficulty_level of game
	#input: raw_input from the user
	#process:
	'''
	1) prints a statement to the console
	2) prompt the user for an input
	3) store the input collected to variable: difficulty_level
	4) end the function by returning the value of difficulty level
	'''
	print "Please select a game difficulty by typing it in!"
	difficulty_level = raw_input("Possible choices include easy, medium, and hard. ")
	return difficulty_level

def print_quiz(quiz_string):
	#output: updated quiz_string
	#input: quiz_string
	#process
	'''
	
	'''
	return quiz_string
	#if answer == "Correct":

	#if answer == "Wrong":
	#	return quiz_string



def ask_for_answer(quiz_string, blank_space_list, answer_list):
	#output: quiz_string
	#input: quiz_string, blank_space_list, answer_list
	#process
	'''
	1) The function will split quiz_string.
	2) Then, it will loop through the elements in quiz_string.
	3) Inside the loop, it will create a variable called replacement which is a value from the function is_blank_space
	4) Next a conditional statement is entered. If the replacement variable is equal to False, it will execute the block inside.
	5) Inside the block, a print statement is coded for aesthetics.
	6) Next, it will equate user_input with the raw_input from the user.
	7) Then, it will check if the answer is correct using the is_correct function that has inputs: user_input and answer_list.
	8) It will check if the answer_is_right is True.
	9) If it is, it will print a blank space for aesthetics.
	10) Then, join the quiz_string.
	11) Then, replace the replacement string in quiz_string by the user_input
	12) Then, print the quiz_string.
	13)	Then, print a blank space for aesthethics.
	14) Then, split the quiz_string.
	15) Else, it will print the function wrong_answer that has the inputs: replacement, quiz_string, and answer_list
	16) Outside the for loop, it will then join the quiz_string together.
	17) And lastly, return the quiz_string.
	'''
	quiz_string = quiz_string.split()
	for word in quiz_string:
		replacement = is_blank_space(word, blank_space_list)
		if replacement != False:
			print 
			user_input = raw_input("What should be substituted in for " + replacement + "? ")
			answer_is_right = is_correct(user_input, answer_list)
			if answer_is_right == True:
				print 
				quiz_string = " ".join(quiz_string)
				quiz_string = quiz_string.replace(replacement, user_input)
				print quiz_string
				print 
				quiz_string = quiz_string.split()
			else:
				print wrong_answer(replacement, quiz_string, answer_list)
	quiz_string = " ".join(quiz_string)
	return quiz_string


def wrong_answer(replacement, quiz_string, answer_list):
	#output: quiz_string
	#input: replacement, quiz_string, and answer_list
	#process:
	'''
	1) The function will create a variable called number_of_tries_left. The variable is inially equal to 5.
	2) Then the function will enter a while loop. While the number_of_tries_left is not equal to 1, it will execute the block in the while loop.
	3) In the block, the function will subtract 1 to number_of_tries_left
	4) Then, it will print an empty space for aesthetic purposes.
	5) Then, it will print a string with the variable number_of_tries_left that says the user eneter the wrong answer and has x number of tries left.
	6) The function will then join the quiz_string list.
	7) It will print the quiz_string
	8) It will print another blank space for aesthetics.
	9) It will set the value of quiz_string to its splitted version.
	10) The function will then equate user_input to the raw_input that the user will enter. This will be the user's another chance to fill the blank. Then it will print a new line for aesthetics.
	11) It will then enter a conditional statement if the answer_is_right is True.
	12) Inside the conditional statement, it will join the quiz_string.
	13) It will replace the replacement variable with the user_input.
	14) And then it will return the quiz_string.
	15) If the answer is incorrect for 5 times, it will print a string saying it's game over but the user can try again.
	16) Lastly, the program will exit.
	'''
	number_of_tries_left = 5
	while number_of_tries_left != 1:
		number_of_tries_left -= 1
		print 
		print "That's not the correct answer. Let's try again. You have " + str(number_of_tries_left) + " tries left.\n"
		quiz_string = " ".join(quiz_string)
		print quiz_string
		print 
		quiz_string = quiz_string.split()
		user_input = raw_input("What should be substituted in for " + replacement + "? ")
		print
		answer_is_right = is_correct(user_input, answer_list)
		if answer_is_right == True:
			quiz_string = " ".join(quiz_string)
			quiz_string = quiz_string.replace(replacement, user_input)
			return quiz_string
	print "You've failed way too many times. Game over. You can play again though."
	exit()




def is_blank_space(word, blank_space_list):
	#output: either element, or False
	#input: word, blank_space_list
	#process
	'''
	1) it will do a for loop in blank_space_list
	2) if the element in blank_space_list is in word, it will return the element
	3) if not, it will return False.
	'''
	for element in blank_space_list:
		if element in word:
			return element
	return False

def is_correct(user_answer, answer_list):
	#output: either True or False
	#input: user_answer and answer_list
	#process:
	'''
	1) the function will check if the user_answer is in answer_list, if it is, it will return True.
	2) if not, it will return False.
	'''
	if user_answer in answer_list:
		return True 
	else:
		return False

def play_game():
	#output: prints the game to the console
	#input: 
	#process
	'''
	1) Prints "here's the quiz" to the console
	2) Store the value from the function diff_level() to the variable game_level
	3) Checks if the game_level is easy, medium or hard
	4) Prints on the console the value from the function print_quiz() with input depending on game_level value: easy, medium, or hard
	5) Prompts the user for the answer on the blank by returning the value from the function ask_for_answer
	6) After the ask_for_answer works, it will return the string "Congratulations! You have finished the game!"
	'''
	game_level = diff_level()
	print "\nHere's the quiz: \n"
	if game_level == "easy":
		print print_quiz(quiz_easy)
		ask_for_answer(quiz_easy, blank_space1, answer_easy)
	if game_level == "medium":
		print print_quiz(quiz_medium)
		ask_for_answer(quiz_medium, blank_space1, answer_medium)
	if game_level == "hard":
		print print_quiz(quiz_hard)
		ask_for_answer(quiz_hard, blank_space1, answer_hard)
	return "Congratulations! You have finished the game!"
		#correct_answer = is_correct(user_answer, answer_hard)
		#print correct_answer
	

##TEST##
print play_game()
#print ask_for_answer(quiz_easy, blank_space1)
#print is_blank_space("__7__", blank_space1)

#sources:
#Hill, Napoleon (2013). Think and Grow Rich. India: Manjul Publishing House
#Merriam Webster Dictionary