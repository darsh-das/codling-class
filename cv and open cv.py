# import cv2

# # Load the image
# image = cv2.imread('example.jpg')

# # Resize the window to a specific size without resizing the image
# cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)  # Create a resizable window
# cv2.resizeWindow('Loaded Image', 800, 500)  # Set the window size to 800x500 (width x height)

# # Display the image in the resized window
# cv2.imshow('Loaded Image', image)
# cv2.waitKey(0)  # Wait for a key press
# cv2.destroyAllWindows()  # Close the window

# # Print image properties
# print(f"Image Dimensions: {image.shape}")  # Height, Width, Channels
# # ACTIVITY-2

# import cv2

# # Load the image
# image = cv2.imread('example.jpg')

# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Resize the grayscale image to 224x224
# resized_image = cv2.resize(gray_image, (224, 224))

# # Display the resized grayscale image in a single window
# cv2.imshow('Processed Image', resized_image)

# # Wait for a key press
# key = cv2.waitKey(0)  # Wait indefinitely for a key press

# # Check if the "S" key was pressed (ASCII for 'S' is 83)
# if key == ord('s'):
#     # Save the processed image when "S" is pressed
#     cv2.imwrite('grayscale_resized_image.jpg', resized_image)
#     print("Image saved as grayscale_resized_image.jpg")
# else:
#     print("Image not saved")

# # Close the window
# cv2.destroyAllWindows()

# # Print processed image properties
# print(f"Processed Image Dimensions: {resized_image.shape}")




# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# import requests

# #load image from url
# img = cv2.imread('example.jpg')
# #url="https://images.contentstack.io/v3/assets/bltcedd8dbd5891265b/blt5f18c2119ce26485/6668df65db90945e0caf9be6/beautiful-flowers-lotus.jpg?q=70&width=3840&auto=webp"

# # response = requets.get(url)
# image_arr = np.asarra(bu=ytearray(response.content),dtype=np.uint8)
# image =cv2.imdecode(image_arr , cv2.IMREAD_COLOR)

# #Convert to rgb
# image_rgb = cv2.cvtcolor(image , cv2.COLOR_BGR2RGB)
# plt.imshow(image_rgb)
# plt.title('RGB image')
# plt.axis('off')
# plt.show()


import cv2

import matplotlib.pyplot as plt

image=cv2.imread('example.jpg')

# Convert BGR TO RGB

image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)

plt.title('RGB Image')

plt.show()