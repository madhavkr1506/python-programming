import cv2
import numpy as np

image = cv2.imread("D:\\OpenCV\\50DaysCoding.png")

# Create a blank mask (same size as image, but grayscale)
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (250, 250), 150, 255 , -1)

masked_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("original image", image)
cv2.imshow("mask image", mask)
cv2.imshow("masked image", masked_image)

# The mask is a black image with a white circle in the center.

# The masked image only shows the part of the original image inside the white circle.

# Everything outside the circle is hidden (turned black).

cv2.waitKey(0)
cv2.destroyAllWindows()