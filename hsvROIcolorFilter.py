import cv2
import numpy as np

def hsvROIcolorFilter(frame, gray, lower, upper, b):
    frameHSV=cv2.cvtColor(frameGraySize, cv2.COLOR_BGR2HSV)
    frameHSV = cv2.cvtColor(frameGraySize, cv2.COLOR_BGR2HSV)
    SSMaskedFrame = cv2.inRange(frameHSV, np.array([158, 16, 168]), np.array([180, 115, 255])) #threshold for Stop Sign at CAR
    xSS, ySS, wSS, hSS = cv2.boundingRect(SSMaskedFrame)
    #cv2.rectangle(frame, (ROIRightStart + xSS-b, ROIheightstart + ySS-b), (ROIRightStart + xSS + wSS+b, ROIheightstart + ySS + hSS+b), (255, 255, 0), 2) #used to view ROI
    grayROI = gray[(int)(ySS-b):(int)(ySS + hSS+b), (int)(xSS-b):(int)(xSS+wSS+b)]
    return grayROI