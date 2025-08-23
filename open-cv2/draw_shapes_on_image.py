import cv2
import numpy as np

# image = cv2.imread("D:\\OpenCV\\50DaysCoding.png")
# cv2.imshow("image1",image)

# Create a blank black image (500x500 pixels, 3 color channels)

image = np.zeros((500,500,3), dtype="uint8") + 255
# cv2.imshow("image1", image)

# Draw a red line (from top-left to bottom-right)

# cv2.line(image, (50, 50), (450, 450), (0, 255, 0), 3)
# cv2.imshow("image1", image)

# Draw a green rectangle (top-left corner to bottom-right corner)

# cv2.rectangle(image, (50, 50), (450, 450), (0, 255, 0), 3)
# cv2.imshow("image1", image)

# Draw a blue circle (center at (250, 250), radius 100)

# cv2.circle(image, (250, 250), 200, (0, 255, 0), -1) # -1 fills the circle
# cv2.imshow("image1", image)

# Put some text on the image

cv2.putText(image, "Hello Madhav", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
cv2.imshow("image1", image)

cv2.waitKey(0)
cv2.destroyAllWindows()