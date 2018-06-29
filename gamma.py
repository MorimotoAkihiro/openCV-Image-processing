import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('frame') # create win with win name

cv2.createTrackbar('gamma', # name of value
                   'frame', # win name
                   0, # min
                   50, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue


    v = cv2.getTrackbarPos('gamma',  # get the value
                           'frame') *0.01  # of the win
    if v == 0: v = 0.01
    frame = 255 * (frame/255)**(1/v)

    cv2.imshow('frame', frame)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()