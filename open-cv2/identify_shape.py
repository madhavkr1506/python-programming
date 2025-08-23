import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("D:\\OpenCV\\50DaysCoding.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, threshold = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_image = image.copy()
cv2.drawContours(contours_image, contours, -1, (0,255,0), 2)

for contour in contours:
    x_cor, y_cor, width, height = cv2.boundingRect(contour)
    cv2.rectangle(image, (x_cor, y_cor), (x_cor + width , y_cor + height), (0, 255, 0), 2)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    sides = len(approx)

    shape = 'unknpwn'
    if sides == 3:
        shape == "triangle"
    elif sides == 4:
        shape = "rectangle"
    elif sides > 4:
        shapes = "circle"

    x_cor, y_cor, width, height = cv2.boundingRect(contour)
    cv2.putText(image, shape, (x_cor , y_cor - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    

# plt.title("threshold_image")
# plt.imshow(contours_image, cmap='gray')
# plt.figure(figsize=(12,10))
# plt.axis('off')
# plt.show()


cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()