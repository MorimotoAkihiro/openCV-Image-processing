import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('frame') # create win with win name

cv2.createTrackbar('v', # name of value
                   'frame', # win name
                   0, # min
                   20, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue
	
    v = cv2.getTrackbarPos('v', 'frame')
    N = 2*v + 1
    frame = cv2.medianBlur(frame,ksize=N);
	
    cv2.putText(frame, "N:" + str(N), (20, 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),2)

    cv2.imshow('frame', frame)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()