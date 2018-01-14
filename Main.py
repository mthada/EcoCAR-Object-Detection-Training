import cv2
import numpy as np
import os
from rearCarandPeopleDetector_woverlapfilter import rearCarandPeopleDetector
from stopandStreetSignDetector import stopandStreetSignDetector
# Initialize video capture.
#cap = cv2.VideoCapture(0)
localDatabase = 'C:\\Users\\estod_000\\Box\\'
database = localDatabase + 'EcoCAR 3\\Electrical\\ADAS\\Image&Video Database\\Calibrated Video Database\\CALIBRATION_050817_PARAM_ES_3\\CALIBRATION_050817_TestVideo_ES_3\\'
# noinspection PyArgumentList
for video in os.listdir("C:\\Fw%3a_loopback_files"):
    videoStream = cv2.VideoCapture('Test footage from my in Car Camera FRONT view.avi')

#videoStream = cv2.VideoCapture('VID_20161004_170809.avi')

    fps = videoStream.get(cv2.CAP_PROP_FPS)*0.01
    print(fps)
    video_length=861
    total_frames=video_length*fps
    n=fps
    desired_frames=n*np.arange(total_frames)
    for i in desired_frames:
        videoStream.set (cv2.CAP_PROP_POS_FRAMES, i-1)
        ret, frame=videoStream.read(cv2.CAP_PROP_POS_FRAMES)
        if (frame is not None):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame=rearCarandPeopleDetector(gray, frame)
            cv2.imshow('The Ohio State University EcoCAR3 ADAS', frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    videoStream.release()
    cv2.destroyAllWindows()