import cv2
import time
from overlapFilter import overlapFilter
#THIS FUNCTION WILL:
#   1. select a region of interest(ROI) on parameter "gray"
#   2. detect cars in gray scaled image "gray"
#   3. detect pedestrians in gray scaled image "gray"
#   4. filter out false negative and false positives based on appropriate area of car and overlap
#   5. return an image "frame" with all objects outlined with a bounding box
def rearCarandPeopleDetector(gray, frame):
    #SETUP OBJECT DETECTORS: initialize detectors for pedestrians and cars
    #-----------------------------------------------------------------------
    database = 'C:\\Users\\estod_000\\Box\\EcoCAR 3\\Electrical\\ADAS\\Current Projects\\Object Detection\\Object Detectors'
    pedDet = cv2.HOGDescriptor()
    pedDet.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    rearDet = cv2.CascadeClassifier('rearVehicleDetectorHaar_700sample.xml')
    carDet = cv2.CascadeClassifier('cars.xml')

    #VARIABLES AND OBJECTS
    #-----------------------
    i = 1
    validCarsFound = 0 #TODO limit Cars found to just 5? or allow as many as possible
    AreafilteredCars = []

    #1. REGION OF INTEREST(ROI): create ROI for middle row of screen
    #----------------------------------------------------------------
    height, width = gray.shape
    ROI2end = (int)(5 * height / 6)
    ROIstart = (0.5225 * ROI2end)
    ROI1end = (int)(0.7 * ROI2end)
    gray2 = gray[(int)(ROIstart):(int)(ROI2end), 0:(int)(width)]
    gray1 = gray[(int)(ROIstart):(int)(ROI1end), 0:(int)(width)]
    cv2.rectangle(frame, (0,(int)(ROIstart)), ((int)(width), (int)(ROI2end)), (255, 255, 0), 2) # can return "frame" depending on version. Used to view ROI
    cv2.rectangle(frame, (0,(int)(ROIstart)), ((int)(width), (int)(ROI1end)), (200, 200, 0), 2) # can return "frame" depending on version. Used to view ROI

    #2. CAR OBJECT DETECTION:  detect cars
    #-----------------------------------
    rearOnline = carDet.detectMultiScale(gray1, 1.1, 2)
    rearFound = rearDet.detectMultiScale(gray2, scaleFactor=1.05, minNeighbors=8, minSize=(1, 1), flags=cv2.CASCADE_SCALE_IMAGE)

    #3. PEDESTRIAN DETECTION: detect pedestrians
    #----------------------------------------111
    pedFound, pedW = pedDet.detectMultiScale(gray, winStride=(8, 8), padding=(32, 32), scale=1.05)
    for (pedX, pedY, pedW, pedH) in pedFound:
        pedY += (int)(ROIstart) #adjust ROI offset for displaying on "frame"
        if(pedY <= 266):
            cv2.rectangle(frame, (pedX, pedY), (pedX + pedW, pedY + pedH), (255, 255, 255), 2)

    #4. AREA FILTER: filter cars based on the size of the object and its location on the screen
    #------------------------------------------------------------------------------------------
    for (rx, ry, rw, rh) in rearOnline:
        ry += (int)((ROIstart) + 1/3.0*rh)
        rx += (int)(1/4.0*rw)
        rw = (int)(rw/2.0)
        rh = (int)(rh/3.0)
        area = rw*rh
        #print "area: " +str(area) + "  with y: " + str(ry) #TODO
        far = (ry <= 240)  and area <= 31000
        farther = (ry >= 241 and ry <= 258)
        close = (ry >= 259 and ry <= 266) and area > 2800 and area <= 1000
        if not (farther or far or close):
        #    AreafilteredCars.append([(int)(rx), (int)(ry), (int)(rw), (int)(rh)])
            fileToSave  = frame[(int)(ry):(int)(ry+rh), (int)(rx):(int)(rx+rw)]
        #    name = "images/isCar/image_" + (str)(time.time()) + ".jpeg"
        #    cv2.imwrite(name, fileToSave)
            #cv2.rectangle(frame, (rx, ry), ((rx+rw), (ry+rh)), (0, 255, 255), 2)  # can return "frame" depending on version
            fileToSave  = frame[(int)(ry):(int)(ry+rh), (int)(rx):(int)(rx+rw)]
            name = "images/trash-isNotCar/image_" + (str)(time.time()) + ".jpeg"
            cv2.imwrite(name, fileToSave)

    for (rearX, rearY, rearW, rearH) in rearFound:
        rearY += (int)(ROIstart) #adjust ROI offset for displaying on "frame"
        area = rearW * rearH
        close = (rearY >= 210 and rearY <= 226) and area > 2000 and area <= 12000
        far = (rearY >= 227 and rearY <= 260) and area > 2000 and area <= 31000
        farther = (rearY >= 261 and rearY <= 266) and area > 2800 and area <= 10000
        if not(farther or far or close):
            #AreafilteredCars.append([rearX,rearY,rearW,rearH])
            #fileToSave  = frame[(int)(rearY):(int)(rearY+rearH), (int)(rearX):(int)(rearX+rearW)]
            #name = "images/isCar/image_" + (str)(time.time()) + ".jpeg"
            #cv2.imwrite(name, fileToSave)
            fileToSave  = frame[(int)(rearY):(int)(rearY+rearH), (int)(rearX):(int)(rearX+rearW)]
            name = "images/trash-isNotCar/image_" + (str)(time.time()) + ".jpeg"
            cv2.imwrite(name, fileToSave)


    #5. OVERLAP FILTER: filter objects that overlap. only display the first object of overlapping objects.
    #--------------------------------------------------------------------------------------------------
    #frame = overlapFilter(AreafilteredCars, frame, 0, 255, 255)


    #6: RETURN: return frame with bounding boxes
    #----------------------------------------
    return frame