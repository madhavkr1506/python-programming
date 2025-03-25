import numpy as np
import cv2

image1 = np.zeros((500, 500, 3), dtype="uint8")
image2 = np.zeros((500, 500, 3), dtype="uint8")

cv2.rectangle(image1, (50, 50), (250, 250), (255, 255, 255), -1)
cv2.circle(image2, (150, 150), 100, (255, 255, 255), -1)

# bitwise_and = cv2.bitwise_and(image1, image2)  # Keeps only the common area
# bitwise_or = cv2.bitwise_or(image1, image2)  # Merges both shapes
# bitwise_xor = cv2.bitwise_xor(image1, image2)  # Keeps non-common areas
# bitwise_not = cv2.bitwise_not(image1, image2)  # Inverts the colors of image1

bitwise_not = cv2.bitwise_not(image2)  #Inverts the color of image2 with background color

# cv2.imshow("image", bitwise_and)
# cv2.imshow("image", bitwise_or)
# cv2.imshow("image", bitwise_xor)
cv2.imshow("image", bitwise_not)

# cv2.imshow("image1", image1)
# cv2.imshow("image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()