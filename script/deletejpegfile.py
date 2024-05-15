import os
import glob

def delete_jpeg_files(directory):
    files = glob.glob(os.path.join(directory, '*.jpeg'))
    for file in files:
        os.remove(file)

delete_jpeg_files('dataset/straight')