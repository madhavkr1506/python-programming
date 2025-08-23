import cv2  # Importing OpenCV library for image processing
import tkinter as tk  # Importing Tkinter (not used in this script)

# Reading the image from the specified path
image = cv2.imread("D:\\OpenCV\\50DaysCoding.png")

# Uncomment the following line to display the original image
# cv2.imshow("image1", image)

# Uncomment the following lines to convert the image to grayscale and display it
# blur_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("image2", blur_image)

# Uncomment the following lines to resize the image to a fixed size (300x400) and display it
# change_size = cv2.resize(image, (300, 400))
# cv2.imshow("image3", change_size)

# Uncomment the following lines to scale the image by 50% of its original size and display it
# scale_percent = 50  # Scaling percentage
# width = int(image.shape[1] * scale_percent / 100)  # New width
# height = int(image.shape[0] * scale_percent / 100)  # New height
# scaled_image = cv2.resize(image, (width, height))
# cv2.imshow("image4", scaled_image)

# Uncomment the following lines to crop the image (from row 50-100 and column 200-300) and display it
# crop_image = image[50:100, 200:300]
# cv2.imshow("image5", crop_image)

# Uncomment the following lines to apply Gaussian blur to the image and display it
# blurred_image = cv2.GaussianBlur(image, (15, 15), 0)  # Applying Gaussian blur with a 15x15 kernel
# cv2.imshow("image6", blurred_image)  # Displaying the blurred image
# cv2.imwrite("image6.png", blurred_image)  # Saving the blurred image

# Displaying the original image in a window
cv2.imshow("image7", image)

# Moving the image window to position (500, 300) on the screen
cv2.moveWindow("image7", 500, 300)

# Waiting indefinitely for a key press
cv2.waitKey(0)

# Closing all OpenCV windows
cv2.destroyAllWindows()


