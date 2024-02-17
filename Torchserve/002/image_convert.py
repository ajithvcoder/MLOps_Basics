import cv2

# Read the image
image = cv2.imread('yolo_image.png')

# Resize the image to 640x640
resized_image = cv2.resize(image, (640, 640))

# Save or display the resized image
cv2.imwrite('resized_image.jpg', resized_image)  # Save the resized image

