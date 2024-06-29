import numpy as np
import cv2

# loads the image in color
img = cv2.imread('Pipe1.jpg')

# Show image
cv2.imshow('Nombre de ventana', img)

# Wait to show it
cv2.waitKey(0)  # Waits for a key
cv2.destroyAllWindows()
