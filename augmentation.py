# Make The Same Thing But With Image In Folder dataset
from imutils import paths
import imutils, os, cv2, pickle
from transformers import AutoImageProcessor, RegNetForImageClassification
import matplotlib.pyplot as plt
imagePaths = list(paths.list_images("dataset"))

# Initialize the total number of faces processed
total = 0

# Loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    print("[INFO] processing image {} / {}".format(i + 1, len(imagePaths)))
    # Extract the Image Inside The Folder
    label = imagePath.split(os.path.sep)[-2]
    # Extract the folder name before the image name
    photo = imagePath.split(os.path.sep)[-1]

    # Load The Image Into GrayScale
    image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

    # Apply GaussianBlur and gray effect
    image = cv2.GaussianBlur(image, (5, 5), 0)

    # Save The Processed Image
    cv2.imwrite(os.path.join("processing", f"{label}_{photo}"), image)

    # Update The Total Number Of Faces Processed
    total += 1