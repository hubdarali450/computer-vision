import cv2
import numpy as np


capture = cv2.VideoCapture('vtest.avi')
ret, grid1=capture.read()
ret, grid2=capture.read()
while capture.isOpened():
    dif=cv2.absdiff(grid1,grid2)
    gry=cv2.cvtColor(dif,cv2.COLOR_BGR2GRAY)
    blr=cv2.GaussianBlur(gry,(5,5),0)
    _,thrsh=cv2.threshold(blr,20,255,cv2.THRESH_BINARY)
    dilate=cv2.dilate(thrsh,None,iterations=3)
    contours, _ =cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (X,Y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<1100:
            continue
        cv2.rectangle(grid1,(X,Y),(X+w,Y+h),(0,255,0),2)
        cv2.putText(grid1,"status: {}".format('movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    #cv2.drawContours(grid1,contours,-1,(0,255,0),2)
    cv2.imshow("Feed",grid1)
    grid1=grid2
    ret, grid2=capture.read()
    if cv2.waitKey(40) ==  27:
        break
cv2.destroyAllWindows()
capture.release()
