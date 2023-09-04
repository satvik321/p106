import cv2 
image = cv2.imread("boy.jpg")
grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces= faceCascade.detectMultiScale(grey,1.1,5)
print(len(faces))
for x,y,w,h in faces:
    cv2.rectangle(image,(x,y),((x+w),(y+h)),(255,0,0),2)
    roi=image[y:y+h,x:x+w]
    cv2.imwrite("c106.jpg",roi)
cv2.imshow("firefox",image)
cv2.waitKey(0)
