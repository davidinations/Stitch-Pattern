import os
import pickle

objects = []
file_path = os.path.join('output', 'recognizer.pickle')

with open(file_path, "rb") as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

# Save objects to a text file
with open('recognizer.txt', 'w') as f:
    for obj in objects:
        f.write(str(obj) + '\n')