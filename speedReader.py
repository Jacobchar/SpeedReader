import sys
import Tkinter

# Create list for words\
listOfWords = []

def speedReader():
	# Get the file path from system arguments
	filePath = "./" + sys.argv[1]

	# Convert .EPUB .MOBI to .txt for ease of use

	# Read the file and parse all the text elements 
	readFile(filePath)

	# Create GUI to read words 

	for word in listOfWords:
		print word


def readFile(path):
	for line in open(path, 'r'):
		# Parse by space and store in a list
		for word in line.split():
			listOfWords.append(word)

speedReader()