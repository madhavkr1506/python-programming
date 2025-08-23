import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:\\OpenCV\\50DaysCoding.png")


gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray_scale, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours_image = image.copy()

cv2.drawContours(contours_image, contours, -1, (0, 255, 0), 2)

# cv2.imshow("contours_image", contours_image)

plt.title("contours_image")
plt.imshow(cv2.cvtColor(contours_image, cv2.COLOR_BGR2RGB))
plt.figure(figsize=(8, 6))
plt.axis('off')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()