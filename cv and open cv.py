import cv2

# Load the image
image = cv2.imread('example.jpg')

# Resize the window to a specific size without resizing the image
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)  # Create a resizable window
cv2.resizeWindow('Loaded Image', 800, 500)  # Set the window size to 800x500 (width x height)

# Display the image in the resized window
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the window

# Print image properties
print(f"Image Dimensions: {image.shape}")  # Height, Width, Channels
# ACTIVITY-2

import cv2

# Load the image
image = cv2.imread('example.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize the grayscale image to 224x224
resized_image = cv2.resize(gray_image, (224, 224))

# Display the resized grayscale image in a single window
cv2.imshow('Processed Image', resized_image)

# Wait for a key press
key = cv2.waitKey(0)  # Wait indefinitely for a key press

# Check if the "S" key was pressed (ASCII for 'S' is 83)
if key == ord('s'):
    # Save the processed image when "S" is pressed
    cv2.imwrite('grayscale_resized_image.jpg', resized_image)
    print("Image saved as grayscale_resized_image.jpg")
else:
    print("Image not saved")

# Close the window
cv2.destroyAllWindows()

# Print processed image properties
print(f"Processed Image Dimensions: {resized_image.shape}")
