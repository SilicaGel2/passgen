import random
import sys

wordLenMin = 5
wordLenMax = 10
badWords = ["ass", "poop", "fucking", "asshole"]


if len(sys.argv) == 2:
	wordLenMin = int(sys.argv[1])
elif len(sys.argv) > 2:
	wordLenMin = int(sys.argv[1])
	wordLenMax = int(sys.argv[2])		

def get_words():
	wordList = []
	wordFile = open("word_list.txt", "r")
	#wordFile = ["turnbine", "dangerous", "apple", "ass", "fucking", "whenever", "asshole", "grassland", "assassin"]
	for word in wordFile:
		#print("RAW WORD IS: " + word)
		clean_words(word, wordList, wordFile)
	return wordList

def clean_words(wrd, wrdArray, wrdSource):
	strippedWord = wrd.strip('\n') # word defults adds \n
	if len(strippedWord) >= wordLenMin and len(strippedWord) <= wordLenMax:
		wrdArray.append(strippedWord) 
		#Adds trimmed words to list
		for xxx in badWords:
			#print("xxx is: " + xxx)
			if xxx == strippedWord:
				#print(xxx + " is a forbidden word")
				wrdArray.remove(strippedWord)
				#removes word if it matches with a forbidden word
			elif xxx != strippedWord:
				continue
				#keeps word in list
		return wrdArray

words = get_words()
#print(words)
random.shuffle(words)
selection = words[0:4]
sep = '-'
print(sep.join(selection))

#print("minimum word length is: " + str(wordLenMin))
#print("max word length is: " + str(wordLenMax))

