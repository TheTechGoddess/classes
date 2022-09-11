def word_count(x):

	file = open(x,'r')
# to get everything in the file
	y =file.read()
# for length of different attributes of the file    	
	unique_words = len(set(y.split()))
	no_lines = len(y.split('\n'))
	no_characters = len(y)
	no_words = len(y.split())

	print(f'It contains {no_words} words and {unique_words} different words.')
	print(f'it also conatins {no_characters} different characters.') 
	print(f'It also contains {no_lines} lines.')

	
word_count('word_count_file.txt')