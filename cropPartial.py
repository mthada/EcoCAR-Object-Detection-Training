import cv2
import csv

imagePath = "C:\\Fw%3a_loopback_files\\sortedCarImages\\positivePartial\\"

coordsList = "C:\\Users\\Manasa\\Downloads\\partialCarCoords2.csv"
croppedPath = "C:\\Fw%3a_loopback_files\\sortedCarImages\\partialToFullCropped\\"
#create lists for image name and coords
imNum = []
coords = []

#open list
with open(coordsList, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='"', quotechar='|')
    for row in spamreader:
        #print row
        imNum.append(row[0][:-1])
        x, y, w, h = row[1].split(",")
        tup = (x[1:],y,w,h[:-1])
        coords.append(tup)

#print imNum
#print coords
i = 0
for imageName in imNum:

    img = imagePath + "" + imageName
    image = cv2.imread(img)

    #read in coordinate values for each image
    tup = coords[i]
    i+=1

    x = int(tup[0])
    y = int(tup[1])
    w = int(tup[2])
    h = int(tup[3])
    #aspect_ratio=float(w)/h
    #print x,y,w,h

    #cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 2)
    crop_img = image[y:y+h, x:x+w]
    #r=100.0/image.shape[1]
    #dim = (100, int(image.shape[0]*r))
    #resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    #cv2.imshow("resized", crop_img)
    cv2.imwrite(croppedPath + "" + imageName, crop_img)
    with open(croppedPath + '\\croppedCoord.csv', 'a') as fCsvFile:
        fWriter = csv.writer(fCsvFile, delimiter=',', lineterminator='\n')
        coordinates = '0,0,{},{}'.format(w, h)
        fWriter.writerow([croppedPath + imageName] + [coordinates])
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

#cropping of the negative images

