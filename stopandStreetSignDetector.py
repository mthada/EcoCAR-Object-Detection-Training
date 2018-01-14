import cv2
import numpy as np

#THIS FUNCTION WILL:
#   1. select a region of interest on parameter "gray"
#   2. detect speed limit and stop signs in gray scaled image
#   3. return an image "frame" with all objects outlined with a bounding box
def stopandStreetSignDetector(gray, frame):
    #DETECTOR SETUP: initialize detectors for stop and speed limit signs
    #-------------------------------------------------------------------
    database = 'C:\\Users\\estod_000\\Box\\EcoCAR 3\\Electrical\\ADAS\\Current Projects\\Object Detection\\Object Detectors'
    stopDet = cv2.CascadeClassifier('StopSignDetectorHaar.xml')
    #stopDet = cv2.CascadeClassifier('stopsignclassifier.xml')
    speedlimitDet = cv2.CascadeClassifier('speedSign_haar_pos271_neg1344.xml') #TODO

    #VARIABLES AND OBJECTS
    #---------------------
    b = 10 #buffer for threshholding ROI

    #1. EXPECTED REGION OF INTEREST(ROI): create ROI for right side of screen for where speed limit and stop signs would be
    #-----------------------------------------------------------------------------------------------------------
    height, width = gray.shape
    ROIheightstart = (int)(0.2 * height)
    ROIheightEnd = (int)(0.6 * height)
    ROIRightStart = (int)(0.7 * width)

    gray = gray[(int)(ROIheightstart):(int)(ROIheightEnd), ROIRightStart:(int)(width)]
    cv2.rectangle(frame, ((int)(ROIRightStart),(int)(ROIheightstart)), ((int)(width), (int)(ROIheightEnd)), (255, 255, 0), 2) #TODO

    #1. COLOR THRESHOLD ROI: color threshold red to select only ROI with red objects for stop sign detector
    #-----------------------------------------------------------------
    frameGraySize = frame[(int)(ROIheightstart):(int)(ROIheightEnd), ROIRightStart:(int)(width)] #trim size of frame to match gray ROI
    frameHSV = cv2.cvtColor(frameGraySize, cv2.COLOR_BGR2HSV)
    #STOP SIGN(SS)
    SSMaskedFrame = cv2.inRange(frameHSV, np.array([158, 16, 80]), np.array([180, 115, 255])) #threshold for Stop Sign at CAR
    #frame[(int)(ROIheightstart):(int)(ROIheightEnd), ROIRightStart:(int)(width)] = cv2.bitwise_and(frameGraySize, frameGraySize, mask=SSMaskedFrame)

    xSS, ySS, wSS, hSS = cv2.boundingRect(SSMaskedFrame)
    cv2.rectangle(frame, (ROIRightStart + xSS-b, ROIheightstart + ySS-b), (ROIRightStart + xSS + wSS+b, ROIheightstart + ySS + hSS+b), (255, 255, 0), 2) #used to view ROI
    graySS = gray[(int)(ySS-b):(int)(ySS + hSS+b), (int)(xSS-b):(int)(xSS+wSS+b)]
    #else:
       # graySS = gray[0:0,0:0]
    #2. OBJECT DETECTION: set up object detectors to detect objects in their ROIs
    #-------------------------------------------------------------------------
    stopFound = stopDet.detectMultiScale(graySS, scaleFactor=1.10, minNeighbors=3, minSize=(1, 1), flags=cv2.CASCADE_SCALE_IMAGE)
    speedFound = speedlimitDet.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=4, minSize=(1, 1), flags=cv2.CASCADE_SCALE_IMAGE)
    #add found objects to "frame"
    for (speedX, speedY, speedW, speedH) in speedFound:
        speedX += ROIRightStart
        speedY += ROIheightstart
        cv2.rectangle(frame, (speedX, speedY), (speedX + speedW, speedY + speedH), (255, 0, 0), 2) #can return "frame" depending on version
    for (stopX, stopY, stopW, stopH) in stopFound:
        stopX += ROIRightStart + (xSS-b)
        stopY += ROIheightstart + (ySS-b)
        cv2.rectangle(frame, (stopX,stopY), (stopX+stopW,stopY+stopH), (0,0,255), 2) #can return "frame" depending on version

    #3: RETURN: return frame with bounding boxes
    #----------------------------------------
    return frame