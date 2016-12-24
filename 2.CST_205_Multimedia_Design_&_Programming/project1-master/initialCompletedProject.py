#Date Last Modified:  February 3, 2016
#Temporal Median Filter On a Series of Images

def createPicture():
  #MUST CALL SET MEDIA PATH TO SPECIFIY LOCATION OF IMAGES
  setMediaPath()
  #MUST CALL SET MEDIA PATH TO SPECIFIY LOCATION OF IMAGES
  
  #CREATES MULTIPLE VARIABLES EACH CONTAINING SPECIFIED IMAGE
  firstImageFile=getMediaPath("1.png")
  firstPic=makePicture(firstImageFile)
  secondImageFile=getMediaPath("2.png")
  secondPic=makePicture(secondImageFile)
  thirdImageFile=getMediaPath("3.png")
  thirdPic=makePicture(thirdImageFile)
  fourthImageFile=getMediaPath("4.png")
  fourthPic=makePicture(fourthImageFile)
  fifthImageFile=getMediaPath("5.png")
  fifthPic=makePicture(fifthImageFile)
  sixthImageFile=getMediaPath("6.png")
  sixthPic=makePicture(sixthImageFile)
  seventhImageFile=getMediaPath("7.png")
  seventhPic=makePicture(seventhImageFile)
  eigthImageFile=getMediaPath("8.png")
  eigthPic=makePicture(eigthImageFile)
  ninthImageFile=getMediaPath("9.png")
  ninthPic=makePicture(ninthImageFile)
  #CREATES MULTIPLE VARIABLES EACH CONTAINING SPECIFIED IMAGE
  
  #ACQUIRES WIDTH AND HEIGHT FOR CREATING NEW IMAGE
  width=getWidth(firstPic)
  height=getHeight(firstPic)  
  newImage=makeEmptyPicture(width,height)
  #ACQUIRES WIDTH AND HEIGHT FOR CREATING NEW IMAGE
  
  #THIS MAKES THE NEW IMAGE PIXEL BY PIXEL
  for x in range(0, width): #range for x axis is 0 - 0
    for y in range(0, height): # range for y is 0 - 0   
      firstPicPixel = getPixel(firstPic, x, y)
      secondPicPixel = getPixel(secondPic, x, y)
      thirdPicPixel = getPixel(thirdPic, x, y)
      fourthPicPixel = getPixel(fourthPic, x, y)
      fifthPicPixel = getPixel(fifthPic, x, y)
      sixthPicPixel = getPixel(sixthPic, x, y)
      seventhPicPixel = getPixel(seventhPic, x, y)
      eigthPicPixel = getPixel(eigthPic, x, y)
      ninthPicPixel = getPixel(ninthPic, x, y)
      firstPicPixelRed = getRed(firstPicPixel)
      firstPicPixelGreen = getGreen(firstPicPixel)
      firstPicPixelBlue = getBlue(firstPicPixel)
      secondPicPixelRed = getRed(secondPicPixel)
      secondPicPixelGreen = getGreen(secondPicPixel)
      secondPicPixelBlue = getBlue(secondPicPixel)
      thirdPicPixelRed = getRed(thirdPicPixel)
      thirdPicPixelGreen = getGreen(thirdPicPixel)
      thirdPicPixelBlue = getBlue(thirdPicPixel)
      fourthPicPixelRed = getRed(fourthPicPixel)
      fourthPicPixelGreen = getGreen(fourthPicPixel)
      fourthPicPixelBlue = getBlue(fourthPicPixel)
      fifthPicPixelRed = getRed(fifthPicPixel)
      fifthPicPixelGreen = getGreen(fifthPicPixel)
      fifthPicPixelBlue = getBlue(fifthPicPixel)
      sixthPicPixelRed = getRed(sixthPicPixel)
      sixthPicPixelGreen = getGreen(sixthPicPixel)
      sixthPicPixelBlue = getBlue(sixthPicPixel)
      seventhPicPixelRed = getRed(seventhPicPixel)
      seventhPicPixelGreen = getGreen(seventhPicPixel)
      seventhPicPixelBlue = getBlue(seventhPicPixel)
      eigthPicPixelRed = getRed(eigthPicPixel)
      eigthPicPixelGreen = getGreen(eigthPicPixel)
      eigthPicPixelBlue = getBlue(eigthPicPixel)
      ninthPicPixelRed = getRed(ninthPicPixel)
      ninthPicPixelGreen = getGreen(ninthPicPixel)
      ninthPicPixelBlue = getBlue(ninthPicPixel)
      redPixelsAllImages = [firstPicPixelRed, secondPicPixelRed, thirdPicPixelRed, fourthPicPixelRed, fifthPicPixelRed, sixthPicPixelRed, seventhPicPixelRed, eigthPicPixelRed, ninthPicPixelRed]
      redPixelsAllImages.sort()
      greenPixelsAllImages = [firstPicPixelGreen, secondPicPixelGreen, thirdPicPixelGreen, fourthPicPixelGreen, fifthPicPixelGreen, sixthPicPixelGreen, seventhPicPixelGreen, eigthPicPixelGreen, ninthPicPixelGreen]
      greenPixelsAllImages.sort()
      bluePixelsAllImages = [firstPicPixelBlue, secondPicPixelBlue, thirdPicPixelBlue, fourthPicPixelBlue, fifthPicPixelBlue, sixthPicPixelBlue, seventhPicPixelBlue, eigthPicPixelBlue, ninthPicPixelBlue]
      bluePixelsAllImages.sort()
      
      redPixel = redPixelsAllImages[4]
      greenPixel = greenPixelsAllImages[4] 
      bluePixel = bluePixelsAllImages[4]
      
      newColor = makeColor(redPixel, greenPixel, bluePixel)
      
      setColor(getPixel(newImage, x, y), newColor)
   
  #DISPLAYS NEW IMAGE
  show(newImage)
  #DISPLAYS NEW IMAGE
  
  #writePictureTo(newImage, pickAFile())
    
createPicture()
#shorten code arrays
