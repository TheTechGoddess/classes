import random

name = input('What is your name: ')

print(f'GoodLuck! {name}')

words = ['lissa', 'kaykay', 'cheta', 'presh', 'emma', 'iyke']

word = random.choice(words)

print('Guess the characters of a word')

guesses = ''

turns = 5

while turns > 0:
	failed = 0

	for i in word:

		if i in guesses:
			print(i)
		else:
			print('_')
			failed+=1

	if failed == 0:
		print('You win')
		print(f'The word is {word}')
		break	

	guess = input('guess a character: ')
	guesses += guess

	if guess not in word:
		turns -= 1

		print('Wrong')
		print(f'You have {turns} more guesses')

		if turns == 0:
			print('You Loose')
			print(f'The word is {word}')
