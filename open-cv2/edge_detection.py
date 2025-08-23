import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:\\OpenCV\\50DaysCoding.png", cv2.IMREAD_GRAYSCALE)

# edges = cv2.Canny(image, 100, 200)
# plt.title("image")
# plt.imshow(edges, cmap='gray')
# plt.figure(figsize=(8,6))
# plt.axis('off')
# plt.show()

vertical_edge_detect_lr = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
horizontal_edge_detect_tp = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

combined_edge_detect = cv2.magnitude(vertical_edge_detect_lr, horizontal_edge_detect_tp)


laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow("image", combined_edge_detect)

cv2.waitKey(0)
cv2.destroyAllWindows()