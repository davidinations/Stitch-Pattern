import cv2
import os
import glob

def apply_gaussian_blur(image_path, blur_size=(5, 5), sigmaX=0, sigmaY=0):
    # Load the image
    image = cv2.imread(image_path)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, blur_size, 0)

    return blurred_image

image_paths = glob.glob('dataset_stitch_detection/*.*')

for image_path in image_paths:
    blurred_image = apply_gaussian_blur(image_path)
    # Save the blurred image
    cv2.imwrite('process_result/blurred_' + os.path.basename(image_path), blurred_image)