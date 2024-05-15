from imutils import paths
import imutils, os, cv2, pickle
from transformers import AutoImageProcessor, RegNetForImageClassification

imagePaths = list(paths.list_images("dataset"))

# Initialize the list of extracted face embeddings and
# corresponding names
knownEmbeddings = []
knownNames = []

# Initialize the total number of faces processed
total = 0

def detect_stitch_area(image):

    return image

def crop_image(image, stitch_area):

    return image

def resize_image(image):

    return image

def extract_embedding(image):

    return image

# Loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    print("[INFO] processing image {} / {}".format(i + 1, len(imagePaths)))
    name = imagePath.split(os.path.sep)[-2]

    # Augment the image
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Detect The Stitch Area Of The Image
    stitch_area = detect_stitch_area(image)
    
    # Crop The Stitch Area
    cropped_image = crop_image(image, stitch_area)
    
    # Resize The Stitch Area
    resized_image = resize_image(cropped_image)
    
    # Extract Embedding
    embedding = extract_embedding(resized_image)
    
    # Append The Embedding And Name To The List
    knownEmbeddings.append(embedding)
    knownNames.append(name)

    # Crop The Stitch Area
    # Resize The Stitch Area
    # Extract Embedding
    # Append The Embedding And Name To The List

    total += 1

# Dump the face embeddings + names to disk
data = {"embeddings": knownEmbeddings, "names": knownNames}
f = open("output/embeddings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()