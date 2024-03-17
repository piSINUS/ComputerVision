import cv2 
import numpy as np

# обработка изображения
# img = cv2.imread('images/573cf9c1f9f60c61b3f1d283a511b548.jpg')
#  img = cv2.GaussianBlur(img,(3,3),0) \\ Размытие
# img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #\\ Перевод к 1 слою

# img = cv2.Canny(img, 250,250)# Нахождение углов обводка

# kernel = np.ones((5,5), np.uint8)# Матрица
# img = cv2.dilate(img,kernel,iterations=1 )#обводка оптимизация жирность

# img = cv2.erode(img,kernel,iterations=1 )#обводка оптимизация уменьшение точек

# cv2.imshow('Jija',img)# Вывод картинки

# print(img.shape)размер
# cv2.waitKey(0)# Время показа

# создание изображения
# photo = np.zeros((500,500,3),dtype='uint8')
# #  В OpenCv система  BGR
# #photo[100:150,200:280] = 73, 235, 73#окраска изобр

# #cv2.rectangle(photo, (350,350), (100,100),(73, 235, 73),thickness=cv2.FILLED)#обводочный квадрат для выделения

# # cv2.line(photo,(0,photo.shape[0]//2),(photo.shape[1],photo.shape[0]//2),(73, 235, 73),thickness=3)

# # cv2.circle(photo,(photo.shape[1]//2,photo.shape[0]//2),50,(73, 235, 73),thickness=5)

# cv2.putText(photo,'Rignul',(100,150), cv2.FONT_HERSHEY_COMPLEX,1,(73, 235, 73),thickness=1)

# cv2.imshow("photo",photo)
# cv2.waitKey(0)

# Трансформация
img = cv2.imread('images/1477076675172219226.jpg')

# img = cv2.flip(img,1)

# def rotate(img_param, angle):#Наклоны
#     height, width = img_param.shape[:2]
#     point = (width//2,height//2)
#     mat = cv2.getRotationMatrix2D(point,angle, 1)
#     return cv2.warpAffine(img_param, mat,(width,height))



# # img = rotate(img,-90)

# def transform(img_param,x,y):#Смещение
#     mat = np.float32([[1,0,x],[0,1,y]])

#     return cv2.warpAffine(img_param,mat,(img_param.shape[1],img_param.shape[0]))

# img =transform(img, 30, 200)
# Kontyrы
new_img = np.zeros(img.shape,dtype='uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img =cv2.GaussianBlur(img,(5,5),0)
img = cv2.Canny(img,50,50)

con, hir =cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE )



cv2.drawContours(new_img,con, -1,(73,190,73),thickness=1)
cv2.imshow("kek",new_img)
cv2.waitKey(0)

# Цветовые форматы
img = cv2.imread('images/1477076675172219226.jpg')
img = cv2.resize(img,dsize=(1000,1000))
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#смена цвета

r,g,b = cv2.split(img)#Разбиение
img = cv2.merge([b,g,r])#Соединение
cv2.imshow("kek",img)
cv2.waitKey(0)
# Побитовые опирации 

photo =  cv2.imread('images/1477076675172219226.jpg')
img = np.zeros(photo.shape[:2],dtype='uint8')

circle = cv2.circle(img.copy(),(200,300), 250,(72,225,72),thickness=-1)
square = cv2.rectangle(img.copy(),(25,25),(250,350),255,-1)

img = cv2.bitwise_and(photo,photo, mask = circle)
# img = cv2.bitwise_or(circle,square)
# img = cv2.bitwise_xor(circle,square)
# img = cv2.bitwise_not(circle,square)

cv2.imshow("kek",img)
cv2.waitKey(0)