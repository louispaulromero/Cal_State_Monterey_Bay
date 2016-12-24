#LOUIS PAUL ROMERO
#RESOURCES
#https://docs.python.org/2/tutorial/inputoutput.html
#https://docs.python.org/2/library/functions.html
#https://docs.python.org/2/library/stdtypes.html
#http://www.greenteapress.com/thinkpython/thinkpython.pdf 

from PIL import Image

#This function opens a file and reads it then returns list of the words found in that file
def openFileReadText(file):
	fileWithText = open(file, 'r')
	listOfWords = [] #Contains every word in text file
	fileContent = fileWithText.read()
	listOfWords = fileContent.split()
	fileWithText.close()
	return listOfWords

#This function accepts a list of words and converts each word into a string of binary digit and adds a whitespace in binary after each word converted into binary
def makeBinaryListOfWords(wordList):
	oneWordInBinary = ""
	wordsFromFileInBinary = []
	for ix in range(0, len(wordList)):
		word = wordList[ix]
		for jx in range(0, len(word)):
			oneWordInBinary += makeNumberBinary(ord(word[jx]))
		wordsFromFileInBinary.append(oneWordInBinary)
		wordsFromFileInBinary.append("00100000")
		oneWordInBinary = "" #clears word
	return wordsFromFileInBinary

#This function makes a number into its binary representation as a string
def makeNumberBinary(number):
	binaryString = ""
	baseTwoValues = [128, 64, 32, 16, 8, 4, 2, 1] 
	for ix in range(0, 8):
			if(number < baseTwoValues[ix]):
				binaryString += "0"
			else:
				binaryString += "1"
				number -= baseTwoValues[ix]
	return binaryString

#This function takes a binary string of 8-bits and converts it to it's decimal value
def makeBinaryANumber(binaryString):
	baseTwoValues = [128, 64, 32, 16, 8, 4, 2, 1] 
	sumOfValues = 0
	for ix in range(0, len(binaryString)):
		if(binaryString[ix] == "1"):
			sumOfValues += baseTwoValues[ix]
		else:
			sumOfValues += 0
	return sumOfValues

#This functions takes a binary string of 18-bits and converts it to it's decimal value
def make18BitsANumber(binaryString):
	baseTwoValues = [131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1] 
	sumOfValues = 0
	for ix in range(0, len(binaryString)):
		if(binaryString[ix] == "1"):
			sumOfValues += baseTwoValues[ix]
		else:
			sumOfValues += 0
	return sumOfValues

#This function takes a number makes its
def makeNumber18BitBinaryString(number):
	binaryString = ""
	baseTwoValues = [131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1] 
	for ix in range(0, 18):
			if(number < baseTwoValues[ix]):
				binaryString += "0"
			else:
				binaryString += "1"
				number -= baseTwoValues[ix]
	return binaryString

#This function prints a list
def printList(listOfWords):
	for ix in range(0, len(listOfWords)):
		print listOfWords[ix]
