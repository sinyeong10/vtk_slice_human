import numpy as np

# Define the normal vectors
normal_vector1 = np.array([2.0, 4.0, 6.0])  # Given normal vector
normal_vector2 = np.array([0.0, 0.0, 1.0])  # Target normal vector

# Normalize the vectors
normal_vector1 /= np.linalg.norm(normal_vector1)
normal_vector2 /= np.linalg.norm(normal_vector2)

# Compute the rotation axis using cross product
rotation_axis = np.cross(normal_vector1, normal_vector2)

# Compute the rotation angle using dot product
rotation_angle = np.arccos(np.dot(normal_vector1, normal_vector2))

# Normalize the rotation axis
rotation_axis /= np.linalg.norm(rotation_axis)

# Compute the elements of the rotation matrix using Rodrigues' rotation formula
c = np.cos(rotation_angle)
s = np.sin(rotation_angle)
t = 1 - c
x, y, z = rotation_axis
rotation_matrix = np.array([[t*x*x + c, t*x*y - z*s, t*x*z + y*s],
                            [t*x*y + z*s, t*y*y + c, t*y*z - x*s],
                            [t*x*z - y*s, t*y*z + x*s, t*z*z + c]])

print("Rotation Matrix:")
print(rotation_matrix)

import numpy as np

# Load the numpy array from file
transformed_colors_np_loaded = np.load('transformed_colors.npy')

# Print the loaded numpy array
print(transformed_colors_np_loaded.shape)
print(transformed_colors_np_loaded)

import cv2
import numpy as np

# Load the grayscale image data
grayscale_image_np = np.load('transformed_grayscale.npy')

# Reshape the 1D array to a 2D array (image)
height = 50  # Example height
width = grayscale_image_np.size // height
grayscale_image_np = grayscale_image_np.reshape((height, width))

# Display the image
cv2.imshow('Grayscale Image', grayscale_image_np)
cv2.waitKey(0)
cv2.destroyAllWindows()
