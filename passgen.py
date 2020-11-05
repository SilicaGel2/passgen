# this is a comment
import random

def get_words():
	wordList = []
	wordFile = open("word_list.txt", "r")
	for word in wordFile:
		strippedWord = word.strip('\n') # word defults adds /n
		if len(strippedWord) >= 5 and len(strippedWord) <= 10:
			wordList.append(strippedWord)
	wordFile.close()
	return wordList


words = get_words()
random.shuffle(words)
top_3 = words[0:5]


sep = '-'
print(sep.join(top_3))





