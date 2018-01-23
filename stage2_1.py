
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
quiz_hard = '''
 '''

answer_hard = ['thoughts', 'definiteness', 'persistence', 'burning', 'one', ]

blank_space1 = ['__1__', '__2__', '__3__', '__4__', '__5__']

maximum_number_of_tries = 5

def is_blank_space(word, blank_space_list):
	for element in blank_space_list:
		if element in word:
			return element
	return False

def check_answer(user_input, answer_list):
	if user_input in answer_list:
		return 'Correct'
	else:
		return 'Wrong'

def prompt_quiz(quiz_string):
	return quiz_string

#def correct_answer(user_input, answer_list, blank_space):
	#for element in blank_space:


def update_quiz(quiz_string, user_input, replacement):
	#quiz_string = quiz_string.split()
	#for element in quiz_string:
	#	replacement = is_blank_space()
	
	quiz_string = quiz_string.replace(replacement, user_input)
	return quiz_string

def wrong_answer(quiz_string):
	print "That isn't the correct answer! Let's try again. You have 4 tries left."
	quiz_string = " ".join(quiz_string)
	print quiz_string







def play_game():
	print "Please select a game difficulty by typing it in! "
	user_input = raw_input("Possible choices include easy, medium, and hard. ")
	if user_input == 'easy':
		print "You've chosen " + user_input + "!\n"
		print game_type(quiz_easy, blank_space1, answer_easy)
	if user_input == 'medium':
		print "You've chosen " + user_input + "!\n"
		print game_type(quiz_medium, blank_space1, answer_medium)
	if user_input == 'hard':
		print "You've chosen " + user_input + "!\n"
		print game_type(quiz_hard, blank_space1, answer_hard)


def game_type(quiz_string, blank_space_list, answer_list):
	print quiz_string
	quiz_string = quiz_string.split()
	for word in quiz_string:
		replacement = is_blank_space(word, blank_space_list)
		if replacement != False:
			user_input = raw_input("What should be substituted in for " + replacement + "? ")
			result_of_answer = check_answer(user_input, answer_list)
			if result_of_answer == 'Correct':
				quiz_string = " ".join(quiz_string)
				quiz_string = update_quiz(quiz_string, user_input, replacement)
				print quiz_string
				quiz_string = quiz_string.split()
			else:
				print wrong_answer(quiz_string)






	'''print quiz_string
	quiz_string = quiz_string.split()
	new_string = []
	for word in quiz_string:
		replacement = is_blank_space(word, blank_space_list)
		if replacement != False:
			user_input = raw_input("What should be substituted for " + replacement + "? ")
			result_of_answer = check_answer(user_input, answer_list)
			if result_of_answer == 'Correct':
				quiz_string = " ".join(quiz_string)
				quiz_string = update_quiz(quiz_string, user_input, replacement)
				print quiz_string

		else:
			new_string.append(word)'''
	



#TESTING	
#print is_blank_space("___5___", blank_space1)
print play_game()


'''sources:


'''

