"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

dic = []
num = 0

def main():
	"""
	"""
	global dic
	global num
	# dic = ['foil', 'firm', 'form', 'coif', 'moor']
	dic = read_dictionary()
	# print(len(dic))
	letters = input_letters()
	# letters = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	dic = shrink_dic(letters)
	# print(dic)
	find_words(letters)
	print(f'There are {num} words in total.')



def find_words(letters):
	"""
	:param letters: an array, combine all the alphabets input by the user
	:return:
	"""
	ans_word_lst = []
	for i in range(4):
		for j in range(4):
			ans_word = letters[i][j]
			old = [(i, j)]
			find_words_helper(letters, i, j, ans_word, ans_word_lst, old)

def find_words_helper(letters, start_i, start_j, ans_word, ans_word_lst, old):
	global dic
	global num
	if len(ans_word) >= 4:
		if ans_word in dic:
			if ans_word not in ans_word_lst:
				ans_word_lst.append(ans_word)
				print('Found: ' + '\"' + ans_word + '\"')
				num += 1
				return
	else:
		for i in [-1, 0, 1]:
			for j in [-1, 0, 1]:
				if 0 <= (start_i + i) < 4:
					if 0 <= (start_j + j) < 4:
						if (start_i + i, start_j + j) not in old:
							ch = letters[(start_i + i)][(start_j + j)]
							test = ans_word + ch
							# print(test)
							if has_prefix(test) is True:
								ans_word += ch
								# print('--------')
								# print(ans_word)
								# print('--------')
								old.append((start_i + i, start_j + j))
								# print(old)
								find_words_helper(letters, (start_i+i), (start_j+j), ans_word, ans_word_lst, old)
								old = old[0:len(ans_word) - 1]
								ans_word = ans_word[0:len(ans_word) - 1]
								# print('*********')
								# print(ans_word)
								# print(old)



def input_letters():
	"""
	this program could change the input alphabets into an array
	:return: an array, combine all the alphabets input by the user
	"""
	letters = []
	for i in range(4):
		test_row = input(f'{i+1} row of letters: ')  # lst
		test_row = test_row.lower()
		test_row = test_row.split()
		if check_row(test_row) is True:
			letters.append(test_row)
		else:
			print('Illegal input.')
			break
	return letters


def check_row(test_row):
	"""
	this program could check if the row input by the user is effective
	:param test_row: lst, the row input by the user
	:return: bool, return True if the row is effective
	"""
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	if len(test_row) != 4:
		return False
	for j in range(len(test_row)):
		if len(test_row[j]) > 1:
			return False
		if test_row[j] not in alpha:
			return False
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.split('\n')
			dic.append(line[0])
		return dic



def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global dic
	n = 0
	for i in range(len(dic)):
		if dic[i].startswith(sub_s) is True:
			n += 1
		if n > 0:
			return True
	return False

def shrink_dic(letters):
	"""
	this program narrow down the list of the dictionary by choosing the word
	that has same digits of the word keyed in by the user
	:param letters: an array, keyed in by the user
	:return: lst, which only contains the words begin with the digit of the keyed-in word
	"""
	new_dic = []
	letter_lst = []
	for i in range(4):
		for j in range(4):
			ch = letters[i][j]
			letter_lst.append(ch)
	shrink_helper(letter_lst, new_dic)
	return new_dic

def shrink_helper(letter_lst, new_dic):
	global dic
	for w in dic:
		for ch in letter_lst:
			if w[0] == ch:
				new_dic.append(w)
			else:
				pass


if __name__ == '__main__':
	main()
