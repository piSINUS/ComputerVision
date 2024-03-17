import cv2 

img = cv2.imread('images/154469827_185776066259377_3334682502007735899_n.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces =  cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray,scaleFactor=1.1, minNeighbors = 7)

for(x,y,w,h) in results:
    cv2.rectangle(img, (x,y), (x+w, y+h),(0,0,255),thickness=4)

cv2.imshow("res",img)
cv2.waitKey(0)



