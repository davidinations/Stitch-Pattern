import cv2
import os

# Load the main image
img_rgb = cv2.imread('Image_1.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Path to the directory containing template images
templates_dir = 'templates/'

# Loop through each file in the templates directory
for template_file in os.listdir(templates_dir):
    if template_file.endswith('.png') or template_file.endswith('.jpg'):
        # Load the template
        template_path = os.path.join(templates_dir, template_file)
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        w, h = template.shape
        
        # Perform template matching
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        _, _, _, maxLoc = cv2.minMaxLoc(res)
        
        # Draw rectangle around detected area on the main image
        cv2.rectangle(img_rgb, maxLoc, (maxLoc[0] + h, maxLoc[1] + w), (0, 255, 255), 2)
        
        # Crop the detected area
        crop_img = img_rgb[maxLoc[1]:maxLoc[1] + w, maxLoc[0]:maxLoc[0] + h, :]
        
        # Display the cropped image
        cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)

# Show the main image with detected areas
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
