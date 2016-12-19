#Date Last Modified:  February 12, 2016
#Temporal Median Filter On a Series of Images

import sys 

def medianOdd(myList):
  listLength = len(myList)
  sortedValues = sorted(myList)
  middleIndex = (listLength + 1) / 2
  return sortedValues[middleIndex]
  
def createPicture():
  #MUST CALL SET MEDIA PATH TO SPECIFIY LOCATION OF IMAGES
  setMediaPath()
  
  #CREATES AN ARRAY WITH EACH ELEMENT CONTAINING SPECIFIED IMAGE
  allPictures = []
  redPixelsAllImages = []
  greenPixelsAllImages = []
  bluePixelsAllImages = []
  
  #CREATES AN ARRAY WITH EACH ELEMENT CONTAINING SPECIFIED IMAGE
  for ix in range(0,9):
    allPictures.append(makePicture(getMediaPath(str((ix+1)) + ".png")))
  
  #ACQUIRES WIDTH AND HEIGHT FOR CREATING NEW IMAGE
  width=getWidth(allPictures[0])
  height=getHeight(allPictures[0])  
  newImage=makeEmptyPicture(width,height)
  
  #THIS NESTED LOOP GRABS THE SAME PIXEL FOR EACH IMAGE AND SPITS THE RGB VALUES AND PUTS INTO 3 SEPARATE ARRAYS
  #IT SORTS EACH ARRAY AND FINDS THE MEDIAN R, G, AND B VALUES AND OUTPUTS TO A NEW CANVAS
  for x in range(0, width):
    for y in range(0, height):
      for jx in range (0, 9):
        pixelOfImage = getPixel(allPictures[jx], x, y)
        redValueOfPixel = getRed(pixelOfImage)
        greenValueOfPixel = getGreen(pixelOfImage)
        blueValueOfPixel = getBlue(pixelOfImage)
        redPixelsAllImages.append(redValueOfPixel)
        greenPixelsAllImages.append(greenValueOfPixel)
        bluePixelsAllImages.append(blueValueOfPixel) 
      redPixel = medianOdd(redPixelsAllImages)
      greenPixel = medianOdd(greenPixelsAllImages)
      bluePixel = medianOdd(bluePixelsAllImages)
      redPixelsAllImages = []
      greenPixelsAllImages = []
      bluePixelsAllImages = []
      newColor = makeColor(redPixel, greenPixel, bluePixel)
      setColor(getPixel(newImage, x, y), newColor)
      #IMAGE GENERATION COMPLETE HERE
  print "STANDARD IMAGE GENERATED"
  return newImage
    
#THIS FUCNTION TAKES IN AN IMAGE AND MAKES A NEAGTIVE OF IT PIXEL BY PIXEL   
def makePictureNegative(image):
  for ix in getPixels(image):
    #THIS IS WHERE THE NEGATION OF THE PIXEL HAPPENS
    negativePixel = makeColor(255 - getRed(ix), 255 - getGreen(ix), 255 - getBlue(ix))
    setColor(ix, negativePixel)
  print "NEGATIVE GENERATED"
  show(image)
  repaint(image)
  return image
  
#THIS FUCNTION TAKES IN AN IMAGE AND MAKES A REDUCED RED VERSION OF IT PIXEL BY PIXEL  
def makePictureReducedRed(image):
  for ix in getPixels(image):
    redValue = getRed(ix)
    setRed(ix,(redValue*0.5))
  print "REDUCED RED IMAGE GENERATED"
  show(image)
  repaint(image)
  return image

#THIS FUCNTION TAKES IN AN IMAGE AND MAKES A GRAYSCALE VERSION OF IT PIXEL BY PIXEL  
def makePictureGrayscale(image):
  for ix in getPixels(image):
    #THE RGB VALUES OF EACH PIXEL ARE MODIFIED HERE
    redValue = getRed(ix) * 0.299
    greenValue = getGreen(ix) * 0.587
    blueValue = getBlue(ix) * 0.114
    #SUM IS TAKEN OF ALL THOSE NEW RGB VALUES
    luminance = redValue + greenValue + blueValue
    #THAT VALUE IS USED FOR R, G, AND B
    newPixel = makeColor(luminance, luminance, luminance)
    setColor(ix, newPixel)
  print "GRAYSCALE IMAGE GENERATED"
  show(image)
  repaint(image)
  return image

#THIS FUCNTION TAKES IN AN IMAGE AND MAKES A BLENDED WHITE VERSION OF IT PIXEL BY PIXEL 
def makeBlendedWithWhite(image, amount):
  for ix in getPixels(image):
    redValue = 255*amount + getRed(ix)*(1-amount)
    greenValue = 255*amount + getGreen(ix)*(1-amount)
    blueValue = 255*amount + getBlue(ix)*(1-amount)
    setColor(ix, makeColor(redValue, greenValue, blueValue))
  print "IMAGE BLENDED WITH WHITE GENERATED"
  show(image)
  repaint(image)
  return image

#THIS FUCNTION TAKES IN ANY IMAGE AND LETS USER CHOOSE TO NEGATE, REDUCE RED, MAKE GRAYSCALE, OR BLEND WHITE
def manipulateAnyPicture(image):
  choice = 0
  terminateChoice = false
  print "WHAT WOULD YOU LIKE TO DO WITH SELECTED IMAGE"
  while(choice <= 0 or choice > 6):
    choice = displayMenuAnyImage()
  if(choice == 1):
    negativeImage = makePictureNegative(image)
    saveAnyImage(negativeImage)
  elif(choice == 2):
    reducedRedImage = makePictureReducedRed(image)
    saveAnyImage(reducedRedImage)
  elif(choice == 3):
    grayscaleImage = makePictureGrayscale(image)
    saveAnyImage(grayscaleImage)
  elif(choice == 4):
    print "Enter a value for the amount of white to be blended"
    print "To Blend 20% white, use 80% (1 - 0.20) = 0.80"
    whiteValue = float(input())
    whiteBlendedImage = makeBlendedWithWhite(image, whiteValue)
    saveAnyImage(whiteBlendedImage)
  return image

#THIS FUNCTIONS GIVES THE USER OPTIONS TO DO WITH FILTERED IMAGE  
def displayMenu():
  print "Enter 1 for a STANDARD image: "
  print "Enter 2 for a NEGATIVE of image: "
  print "Enter 3 for a REDUCED RED image: "
  print "Enter 4 for a GRAYSCALE image: "
  print "Enter 5 to blend with WHITE: "
  print "Enter 6 to MANIPULATE ANY IMAGE: "
  menuChoice = int(input())  
  return menuChoice
  
#THIS FUNCTIONS GIVES THE USER OPTIONS TO DO WITH FILTERED IMAGE  
def displayMenuAnyImage():
  print "Enter 1 for a NEGATIVE of image: "
  print "Enter 2 for a REDUCED RED image: "
  print "Enter 3 for a GRAYSCALE image: "
  print "Enter 4 to blend with WHITE: "
  menuChoice = int(input())  
  return menuChoice

#THIS FUNCTION GIVES THE USER THE OPTION TO SAVE, QUIT, OR CONTINUE
def saveNewImage(image):
  saveImage = -1
  while(saveImage < 0 or saveImage > 3):
    print "Would you like to save image?"
    print "Enter 1 to SAVE image"
    print "Enter 2 to QUIT"
    print "Enter 3 to CONTINUE"
    saveImage = int(input())
    if(saveImage == 1):
      writePictureTo(image, pickAFile())
    elif(saveImage == 2):
      sys.exit()
    elif(saveImage == 3):
      print ""

#THIS FUNCTION GIVES THE USER THE OPTION TO SAVE OR QUIT PROGRAM     
def saveAnyImage(image):
  saveImage = -1
  while(saveImage < 0 or saveImage > 2):
    print "Would you like to save image?"
    print "Enter 1 to SAVE image"
    print "Enter 2 to QUIT"
    saveImage = int(input())
    if(saveImage == 1):
      writePictureTo(image, pickAFile())
    elif(saveImage == 2):
      sys.exit()
      
#THIS FUNCTION GIVES THE USER A NICE WELCOMING MESSAGE
def welcome():
  print "WELCOME TO MY PROGRAM"
  print "THIS SOFTWARE WILL PERFORM A TEMPORAL MEDIAN FILTRATION ON A SERIES OF IMAGES"
  print "YOU WILL HAVE THE CHOICE TO SAVE MULTIPLE VARATIONS OF THE FILTERED IMAGE"

#THIS IS THE MAIN WHERE USER CAN DO A TEMPORAL MEDIAN FILTRATION OF A SERIES OF 9 IMAGES 
#THE USER ALSO HAS THE OPTION TO HAVE IMAGE DELIVERED AS NEGATED, REDUCED RED, GRAYSCALE, OR BLENDED WHITE
def main():
  choice = 0
  terminateChoice = false
  while(choice <= 0 or choice > 6):
    choice = displayMenu()
  if(choice == 1):
    standardImage = createPicture()
    show(standardImage)
    saveNewImage(standardImage)
  elif(choice == 2):
    standardImage = createPicture()
    negativeImage = makePictureNegative(standardImage)
    saveNewImage(negativeImage)
  elif(choice == 3):
    standardImage = createPicture()
    reducedRedImage = makePictureReducedRed(standardImage)
    saveNewImage(reducedRedImage)
  elif(choice == 4):
    standardImage = createPicture()
    grayscaleImage = makePictureGrayscale(standardImage)
    saveNewImage(grayscaleImage)
  elif(choice == 5):
    standardImage = createPicture()
    print "Enter a value for the amount of white to be blended"
    print "To Blend 20% white, use 80% (1 - 0.20) = 0.80"
    whiteValue = float(input())
    whiteBlendedImage = makeBlendedWithWhite(standardImage, whiteValue)
    saveNewImage(whiteBlendedImage)
  elif(choice == 6):
    image = makePicture(pickAFile())
    newImage = manipulateAnyPicture(image)
    saveNewImage(newImage)
    
#FUNCTION CALLS   
welcome()
while(true):
  main()
#FUNCTION CALLS
  
