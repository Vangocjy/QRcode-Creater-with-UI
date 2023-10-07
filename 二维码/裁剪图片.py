import cv2

img = cv2.imread("./20230925173307.jpg")
img_change = cv2.resize(img,(64,64))
cv2.imwrite("./22.png",img_change)