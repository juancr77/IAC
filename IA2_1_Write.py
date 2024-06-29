import numpy as np
import cv2

# loads the image in color
img = cv2.imread('Pipe1.jpg')

# Show image
cv2.imshow('Color image', img)

# Change it to grey
gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Show image
cv2.imshow('Gray image', gray)

# Save it in grey as Out
cv2.imwrite("Out.jpg", gray)

# Wait to show it
cv2.waitKey(0)
cv2.destroyAllWindows()
