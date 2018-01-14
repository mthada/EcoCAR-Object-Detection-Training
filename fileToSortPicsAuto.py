import cv2
import os
import os.path
import shutil

pathToSaveToPositive = "C:\\Fw%3a_loopback_files\\saveToPositiveFolder"
pathToSaveToNegative = "C:\\Fw%3a_loopback_files\\saveToNegativeFolder"
pathToSaveToPartial = "C:\\Fw%3a_loopback_files\\saveToPartialFolder"

pathToImagesPositive = "C:\\Fw%3a_loopback_files\\images\\Positive-isCar"
pathToImagesNegative = "C:\\Fw%3a_loopback_files\\images\\Negative-isNotCar"

for image in imagesPositive:
    cv2.imread('im', image)
    cv2.imshow('im', image)

    getInput = input("Enter y for positive, n for negative, and p for partial")

    while (getInput != 'y' or getInput !='n' or getInput != 'h'):
        print "Not valid input. Try again"
        getInput = input("Enter y for positive, n for negative, and p for partial")

    if getInput = 'y':
        cv2.imsave(pathToSaveToPositive)
    else if getInput='n':
        cv2.imsave(pathToSaveToNegative)
    else:
        cv2.imsave(pathToSaveToPartial)