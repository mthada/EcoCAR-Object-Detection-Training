import cv2
import csv
import os

imagePath = "C:\\Fw%3a_loopback_files\\sortedCarImages\\negative\\"

resizedPath = "C:\\Fw%3a_loopback_files\\sortedCarImages\\allNegativeResizedIm\\"

##create lists for image name and coords
imNum = []
coords = []


i = 0
for imageName in os.listdir(imagePath):

    img = imagePath + "" + imageName
    image = cv2.imread(img)

    #resize after current width and height
    #print x,y,w,h
    currentWidth = image.shape[1]
    currentHeight = image.shape[0]

    aspectRatio = float(currentWidth/currentHeight)
    area = 60*60

    height = int((area/aspectRatio)**0.5)
    width = int(height*aspectRatio)
    #print(width)
    #print (height)

    resizedIm = cv2.resize(image, (width, height))
    #cv2.imshow("resized", resizedIm)
    cv2.imwrite(resizedPath + "" + imageName, resizedIm)
    #print (imageName)
    #with open(resizedPath + 'resizedCoords2.csv', 'a') as fCsvFile:
    #    fWriter = csv.writer(fCsvFile, delimiter=',', lineterminator='\n')
    #    coordinates = '1,1,{},{}'.format(width, height)
    #    fWriter.writerow([resizedPath + imageName] + [coordinates])

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
