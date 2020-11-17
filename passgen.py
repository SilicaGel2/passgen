import random
import sys

wordLenMin = 5
wordLenMax = 10
badWords = ["ass", "poop", "fucking", "asshole"]

def prompt_for_integer(prompt):
	rawInput = input(prompt)
	try:
		parsed = int(rawInput)
		return parsed
	except ValueError:
		return None


def int_check(prompt, error):
	intInput = prompt_for_integer(prompt)
	while intInput is None:
		print(error)
		intInput = prompt_for_integer(prompt)
	return intInput

	
wrdMinInput = int_check("What is the smallest word length ", "Invalid input! You did not provide an integer")
wordLenMin = wrdMinInput
print("shortest word length is: " + str(wordLenMin))
# set shortest length

wrdMaxInput = int_check("What is the largest word length ", "Invalid input! You did not provide an integer")
wordLenMax = wrdMaxInput
if wrdMaxInput < wrdMinInput:
	wordLenMin = wrdMaxInput
	wordLenMax = wrdMinInput
# flips min/max values
	print("shortest word length was changed to " + str(wordLenMin))
print("longest word length is: " + str(wordLenMax))
# set longest length

def get_words():
	wordList = []
	wordFile = open("word_list.txt", "r")
	for word in wordFile:
		clean_words(word, wordList, wordFile)
	return wordList

def clean_words(wrd, wrdArray, wrdSource):
	strippedWord = wrd.strip('\n') # word defults adds \n
	if len(strippedWord) >= int(wordLenMin) and len(strippedWord) <= int(wordLenMax):
		wrdArray.append(strippedWord) 
		#Adds trimmed words to list
		for xxx in badWords:
			if xxx == strippedWord:
				wrdArray.remove(strippedWord)
				#removes word if it matches with a forbidden word
			elif xxx != strippedWord:
				continue
				#keeps word in list
		return wrdArray

words = get_words()
random.shuffle(words)
selection = words[0:4]
sep = '-'
print('*' * 30)
print(sep.join(selection))

