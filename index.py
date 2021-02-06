import cv2
import numpy as np
import argparse
import sys
import os

def empty(a):
    pass

def run(img_path):
    img = cv2.imread(img_path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #create sliders
    cv2.namedWindow("HSV_Finder")
    cv2.resizeWindow("HSV_Finder", 640, 240)
    cv2.createTrackbar("Hue Min", "HSV_Finder", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "HSV_Finder", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "HSV_Finder", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "HSV_Finder", 255, 255, empty)
    cv2.createTrackbar("Val Min", "HSV_Finder", 0, 255, empty)
    cv2.createTrackbar("Val Max", "HSV_Finder", 255, 255, empty)
    cv2.createTrackbar("Nothing", "HSV_Finder", 255, 255, empty)

    while True:
        #get trackbar values
        hue_min = cv2.getTrackbarPos("Hue Min", "HSV_Finder")
        hue_max = cv2.getTrackbarPos("Hue Max", "HSV_Finder")
        sat_min = cv2.getTrackbarPos("Sat Min", "HSV_Finder")
        sat_max = cv2.getTrackbarPos("Sat Max", "HSV_Finder")
        val_min = cv2.getTrackbarPos("Val Min", "HSV_Finder")
        val_max = cv2.getTrackbarPos("Val Max", "HSV_Finder")
        #generate masks
        lower = np.array([hue_min, sat_min, val_min])
        upper = np.array([hue_max, sat_max, val_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        #show result
        cv2.imshow("Original", img)
        cv2.imshow("Mask", mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

parser = argparse.ArgumentParser(description='List image path')

parser.add_argument('--path', type=str, required=True)

args = parser.parse_args()

run(args.path)