import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread("D:\\OpenCV\\testing_face_detection.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

for x_cor, y_cor, width, height in faces:
    cv2.rectangle(image, (x_cor, y_cor), (x_cor + width, y_cor + height), (0, 255, 0), 2)

cv2.imshow("face_detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()