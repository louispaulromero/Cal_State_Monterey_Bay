#Date Last Modified:  February 3, 2016
#Temporal Median Filter On a Series of Images

def createPicture():
  #MUST CALL SET MEDIA PATH TO SPECIFIY LOCATION OF IMAGES
  setMediaPath()
  #MUST CALL SET MEDIA PATH TO SPECIFIY LOCATION OF IMAGES
  
  #CREATES MULTIPLE VARIABLES EACH CONTAINING SPECIFIED IMAGE
  firstImageFile = getMediaPath("1.png")
  firstPic = makePicture(firstImageFile)
  secondImageFile = getMediaPath("2.png")
  secondPic = makePicture(secondImageFile)
  thirdImageFile = getMediaPath("3.png")
  thirdPic = makePicture(thirdImageFile)
  fourthImageFile = getMediaPath("4.png")
  fourthPic = makePicture(fourthImageFile)
  fifthImageFile = getMediaPath("5.png")
  fifthPic = makePicture(fifthImageFile)
  sixthImageFile = getMediaPath("6.png")
  sixthPic = makePicture(sixthImageFile)
  seventhImageFile = getMediaPath("7.png")
  seventhPic = makePicture(seventhImageFile)
  eigthImageFile = getMediaPath("8.png")
  eigthPic = makePicture(eigthImageFile)
  ninthImageFile = getMediaPath("9.png")
  ninthPic = makePicture(ninthImageFile)
  #CREATES MULTIPLE VARIABLES EACH CONTAINING SPECIFIED IMAGE
  
  #ACQUIRES WIDTH AND HEIGHT FOR CREATING NEW IMAGE CANVAS
  width=getWidth(firstPic) #CAN BE ANY OF THE LOADED PICS
  height=getHeight(firstPic)  
  newImage=makeEmptyPicture(width,height)
  #ACQUIRES WIDTH AND HEIGHT FOR CREATING NEW IMAGE CANVAS
  
  #THIS MAKES THE NEW IMAGE PIXEL BY PIXEL
  for x in range(0, width): #range for x axis is 0 - 0
    for y in range(0, height): # range for y is 0 - 0
      redPixelsAllImages = [getRed(getPixel(firstPic, x, y)), getRed(getPixel(secondPic, x, y)), getRed(getPixel(thirdPic, x, y)), getRed(getPixel(fourthPic, x, y)), getRed(getPixel(fifthPic, x, y)), getRed(getPixel(sixthPic, x, y)), getRed(getPixel(seventhPic, x, y)), getRed(getPixel(eigthPic, x, y)), getRed(getPixel(ninthPic, x, y))]
      redPixelsAllImages.sort()
      greenPixelsAllImages = [getGreen(getPixel(firstPic, x, y)), getGreen(getPixel(secondPic, x, y)), getGreen(getPixel(thirdPic, x, y)), getGreen(getPixel(fourthPic, x, y)), getGreen(getPixel(fifthPic, x, y)), getGreen(getPixel(sixthPic, x, y)), getGreen(getPixel(seventhPic, x, y)), getGreen(getPixel(eigthPic, x, y)), getGreen(getPixel(ninthPic, x, y))]
      greenPixelsAllImages.sort()
      bluePixelsAllImages = [getBlue(getPixel(firstPic, x, y)), getBlue(getPixel(secondPic, x, y)), getBlue(getPixel(thirdPic, x, y)), getBlue(getPixel(fourthPic, x, y)), getBlue(getPixel(fifthPic, x, y)), getBlue(getPixel(sixthPic, x, y)), getBlue(getPixel(seventhPic, x, y)), getBlue(getPixel(eigthPic, x, y)), getBlue(getPixel(ninthPic, x, y))]
      bluePixelsAllImages.sort()
      
      setColor(getPixel(newImage, x, y), makeColor(redPixelsAllImages[4], greenPixelsAllImages[4] , bluePixelsAllImages[4]))
      
  #DISPLAYS NEW IMAGE
  show(newImage)
  #DISPLAYS NEW IMAGE
  
  #LOADING INDICATOR / DRAG AND DROP BOX TO LOAD IMAGES
   
createPicture()
