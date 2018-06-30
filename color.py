import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('frame') # create win with win name

cv2.createTrackbar('R','frame',0,100,myfunc)
cv2.createTrackbar('G','frame',0,100,myfunc)
cv2.createTrackbar('B','frame',0,100,myfunc)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue

    r = cv2.getTrackbarPos('R','frame')/100
    g = cv2.getTrackbarPos('G','frame')/100
    b = cv2.getTrackbarPos('B','frame')/100
    frame = frame/255
	
    frame[:,:,0] *= b
    frame[:,:,1] *= g
    frame[:,:,2] *= r
   
    cv2.imshow('frame', frame)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
