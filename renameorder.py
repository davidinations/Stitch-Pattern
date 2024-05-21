# # If Folder File There is A Text
# import os
# import glob
# import shutil  # Import the shutil module

# def rename_files_in_order(directory):
#     files = sorted(glob.glob(os.path.join(directory, '*')))
#     for i, file in enumerate(files, start=1):
#         # Use shutil.move() instead of os.rename()
#         shutil.move(file, os.path.join(directory, f'{i}.jpg'))  # Change the extension if needed

# rename_files_in_order('dataset_stitch_detection')

# # If Folder File In Only Number
# import os
# import glob
# import shutil
# import re

# def rename_files_in_order(directory, label):
#     files = glob.glob(os.path.join(directory, '*'))
#     # Sort files in numerical order
#     files.sort(key=lambda x: int(re.search(r'\d+', os.path.basename(x)).group()))
#     for i, file in enumerate(files, start=1):
#         shutil.move(file, os.path.join(directory, f'{i}.jpg'))  # Change the extension if needed

# rename_files_in_order('dataset_stitch_detection', 'label')