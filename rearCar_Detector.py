import cv2
#THIS FUNCTION WILL:
#   1. select a region of interest(ROI) on parameter "gray"
#   2. detect cars in gray scaled image "gray"
#   3. detect pedestrians in gray scaled image "gray"
#   4. filter out false negative and false positives based on appropriate area of car and overlap
#   5. return an image "frame" with all objects outlined with a bounding box
def rearCarDetector(gray, frame, i):
    #SETUP OBJECT DETECTORS: initialize detectors for pedestrians and cars
    #-----------------------------------------------------------------------
    #database = 'C:\\Users\\estod_000\\Box\\EcoCAR 3\\Electrical\\ADAS\\Current Projects\\Object Detection\\Object Detectors'
    rearDet = cv2.CascadeClassifier('rearVehicleDetectorHaar_700sample.xml')

    #1. REGION OF INTEREST(ROI): create ROI for middle row of screen
    #----------------------------------------------------------------
    height, width = gray.shape
    ROI2end = (int)(5 * height / 6)
    ROIstart = (0.5225 * ROI2end)
    gray2 = gray[(int)(ROIstart):(int)(ROI2end), 0:(int)(width)]

    #2. CAR OBJECT DETECTION:  detect cars
    #-----------------------------------
    rearFound = rearDet.detectMultiScale(gray2, scaleFactor=1.05, minNeighbors=8, minSize=(1, 1), flags=cv2.CASCADE_SCALE_IMAGE)

    #3: Print identified objects to display, save images to file
    #------------------------------------------------------------------------------------------
    j = 0
    for (rearX, rearY, rearW, rearH) in rearFound:
        rearY += (int)(ROIstart) #adjust ROI offset for displaying on "frame"
        fileToSave  = frame[(int)(rearY):(int)(rearY+rearH), (int)(rearX):(int)(rearX+rearW)]
        name = "images/image_" + str(i) + "_" + str(j) + ".jpeg"
        cv2.imwrite(name, fileToSave)
        j = j + 1
        cv2.rectangle(frame, (rearX, rearY), (rearX + rearW, rearY + rearH), (255, 255, 255), 2)



        #4: RETURN: return frame with bounding boxes
    #----------------------------------------
    return frame