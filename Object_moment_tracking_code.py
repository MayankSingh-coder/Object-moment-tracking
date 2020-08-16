import cv2
import numpy as np
#reading video
cap=cv2.VideoCapture('m.mp4')
while True:
#reading video in two frames
   ret,frame1=cap.read()
   ret,frame2=cap.read()
   # finding the diffrence between the videos
   diff=cv2.absdiff(frame1,frame2)
   gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
   blur=cv2.GaussianBlur(gray,(5,5),0)
   ret,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
   dilate=cv2.dilate(thresh,None,iterations=3)
   #finding countours
   countours,heirarchy=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

   for countour in countours:
       #making left corner point,height and width.
       x,y,w,h=cv2.boundingRect(countour)
       if cv2.contourArea(countour)<700:
           pass
       cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),0)
   #cv2.drawContours(frame1,countours,-1,(0,255,0),0)
   cv2.imshow('FEED',frame1)
   if cv2.waitKey(1) & 0xFF==ord('q'):
       break
cap.release()
cv2.destroyWindow()
