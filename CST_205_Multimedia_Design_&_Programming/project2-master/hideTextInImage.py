#LOUIS PAUL ROMERO
#RESOURCES
#http://pillow.readthedocs.org/en/3.1.x/handbook/tutorial.html
#http://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil 
#https://docs.python.org/2/tutorial/modules.html

from PIL import Image
import functions

def processingImage(imagepath, txtpath):
	#This loads orignal image
	originalImage = Image.open(imagepath)
	pixel = originalImage.load()
	width, height = originalImage.size

	#A list of words is created from a text file as wordsFromFile
	wordsFromFile = functions.openFileReadText(txtpath)

	#Each word in the list wordsFromFile is converted to it's binary representation 
	binaryListOfWords = functions.makeBinaryListOfWords(wordsFromFile)

	#A list of bits that need to be hidden is created here
	listOfBitsToHide = []
	for binaryWord in binaryListOfWords:
		for bit in binaryWord:
			listOfBitsToHide.append(bit)

	
	#First 18-bits of will contain the decimal values of numberOfPixelsNeeded and numberOfRowsNeeded

	#This creates an integer value that will control the loop that creates a list of RGB values needed
	if(len(listOfBitsToHide) % 3 != 0):
		numberOfPixelsNeeded = (len(listOfBitsToHide) / 3) + 1 
	else: 
		numberOfPixelsNeeded = len(listOfBitsToHide) / 3

	#An additional 12 pixels are needed to hide the decimal values of numberOfPixelsNeeded and numberOfRowsNeeded
	numberOfPixelsNeeded = numberOfPixelsNeeded + 12 

	numberOfRowsNeeded = (numberOfPixelsNeeded/width) + 1

	#numberOfPixelsNeeded and numberOfRowsNeeded are made in to binary strings
	numberOfPixelsNeededBinaryString = functions.makeNumber18BitBinaryString(numberOfPixelsNeeded)
	numberOfRowsNeededBinaryString = functions.makeNumber18BitBinaryString(numberOfRowsNeeded)

	#numberOfPixelsNeeded and numberOfRowsNeeded binary representation is appended to the list of bits to hide.
	for ix in range(0, len(numberOfPixelsNeededBinaryString)):
		listOfBitsToHide.insert(ix, numberOfPixelsNeededBinaryString[ix])
	placeOfInsertion = 18
	for jx in range(0, len(numberOfRowsNeededBinaryString)):
		listOfBitsToHide.insert(placeOfInsertion, numberOfRowsNeededBinaryString[jx])
		placeOfInsertion+=1

	listOfRGBValues = []
	counter = numberOfPixelsNeeded
	#This loop creates a list of the RGB values needed
	for y in range(0, numberOfRowsNeeded):
		for x in range(0, width):
			if(counter != 0):
				redValue, greenValue, blueValue = originalImage.getpixel((x, y))
				binaryRed = functions.makeNumberBinary(redValue)
				binaryGreen = functions.makeNumberBinary(greenValue)
				binaryBlue = functions.makeNumberBinary(blueValue)
				listOfRGBValues.append(binaryRed)
				listOfRGBValues.append(binaryGreen)
				listOfRGBValues.append(binaryBlue)
				counter -= 1
			else:
				break

	binaryListOfHiddenTextInPixels = []
	stringOfHiddenBits = ""
	#For each iteration this loop creates a string of 8 bits bits 1-7 are from RGB values and bit 8 is the bit that needs to be hidden
	for ix in range(0, len(listOfBitsToHide)):
		for jx in range (0, 7): #grabs 8 bits
			stringOfHiddenBits += listOfRGBValues[ix][jx]
		stringOfHiddenBits += listOfBitsToHide[ix]
		binaryListOfHiddenTextInPixels.append(stringOfHiddenBits)
		stringOfHiddenBits = ""

	#This loops gets all decimal values of each binary string and creates a new list
	listOfNewRGBValues = []
	for ix in range(0, len(binaryListOfHiddenTextInPixels)):
		listOfNewRGBValues.append(functions.makeBinaryANumber(binaryListOfHiddenTextInPixels[ix]))

	#Creates a new black image
	img = Image.new( 'RGB', (width, height), "black")

	#Creates a pixel map
	pixels = img.load() 

	#This loop creates a copy of the original image
	otherCounter = numberOfPixelsNeeded
	for y in range(0, height):
		for x in range(0, width):
			redValue, greenValue, blueValue = originalImage.getpixel((x, y))
			pixels[x,y] = (redValue, greenValue, blueValue)

	#This loop replaces pixels with manipulated pixels.
	#Try and except are used for the last pixel because in some cases only the R value for the last pixels is needed, but not the G and B values
	#In another case R and B maybe needed, but not the G value.  The except part replaces the GB or G value in both cases with the pixel's original value.
	incrementer = 0
	for y in range(0, numberOfRowsNeeded):
		for x in range(0, width):
			if(otherCounter != 0):
				try:
					newRedValue = listOfNewRGBValues[incrementer]
					finalXValue = x
					finalYValue = y
				except IndexError:
					redValue, greenValue, blueValue = originalImage.getpixel((x, y))
					newRedValue = redValue
					finalXValue = x
					finalYValue = y
				try:
					newGreenValue = listOfNewRGBValues[incrementer+1]
					finalXValue = x
					finalYValue = y
				except IndexError:
					redValue, greenValue, blueValue = originalImage.getpixel((x, y))
					newGreenValue = greenValue
					finalXValue = x
					finalYValue = y
				try:
					newBlueValue = listOfNewRGBValues[incrementer+2]
					finalXValue = x
					finalYValue = y
				except IndexError:
					redValue, greenValue, blueValue = originalImage.getpixel((x, y))	
					newBlueValue = blueValue
					finalXValue = x
					finalYValue = y
				pixels[x,y] = (newRedValue, newGreenValue, newBlueValue) # set the color accordingly
				otherCounter -= 1
			incrementer += 3

	#This saves image with hidden text to the same location as the .py files
	img.save(fp="imageWithHiddenText.png", format= "PNG")
	print "DONE"
