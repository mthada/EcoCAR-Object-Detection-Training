#read imageNames from file and save to folders
import os
import cv2
import csv

def sortAndCropCars():

    #read all imageNames from input file
    path = "C:\\Fw%3a_loopback_files\\images\\Positive-isCar\\"
    sortedPath = "C:\\Fw%3a_loopback_files\\sortedCarImages\\"
    yPath = "positiveFull\\"
    pPath = "positivePartial\\"
    nPath = "negative\\"
    i = 254
    totalImages = len([name for name in os.listdir(path)])
    for imageName in os.listdir(path)[i:]:
        i+=1
        print('Image {} out of {}'.format(i,totalImages))
        #read, print imageName
        img = cv2.imread(path+imageName)
        cv2.imshow('im', img)
        cv2.namedWindow('im', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('im', 400, 400)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

        #save to folder based on f/p/n/r
        saveAs = raw_input('Is image positive full, partial, or negative, or reshow image, or delete? f/p/n/r/d:')

        while(saveAs != 'f' and saveAs != 'p' and saveAs != 'n' and saveAs != 'd'):
            print('Image {} out of {}'.format(i,totalImages))
            cv2.imshow('im', img)
            cv2.namedWindow('im', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('im', 400, 400)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
            saveAs = raw_input('Please enter f/p/n/r/d for positive full/partial/negative/redo/delete:')
        if saveAs == "f":
            #save fileName, imageName coordinates to csv
            width, height, c = img.shape
            with open(sortedPath+yPath+'\\fullCarList.csv', 'a') as fCsvFile:
                fWriter = csv.writer(fCsvFile, delimiter=',', lineterminator='\n')
                coordinates = '0,0,{},{}'.format(width, height)
                fWriter.writerow([sortedPath + yPath + imageName] + [coordinates])
            #save imageName to new file
            print sortedPath + yPath + imageName
            cv2.imwrite(sortedPath + yPath + imageName, img)
        elif saveAs == "p":
            cv2.imwrite(sortedPath + pPath + imageName, img)
        elif saveAs == "n":
            cv2.imwrite(sortedPath + nPath + imageName, img)
def main():
    sortAndCropCars()
if __name__ == '__main__':
    main()

