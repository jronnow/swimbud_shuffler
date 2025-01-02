import os
import random
import shutil

# Path to the folder containing MP3 files
mp3_folder = "G:\\"

# Check if the folder exists
if not os.path.exists(mp3_folder):
    print(f"The folder {mp3_folder} does not exist!")
    exit()

# Get a list of all MP3 files in the folder
mp3_files = [f for f in os.listdir(mp3_folder) if f.lower().endswith('.mp3')]

if len(mp3_files) == 0:
    print("No MP3 files found in the folder.")
    exit()

# Remove the leading index and underscore from each MP3 file name
for index, file in enumerate(mp3_files):
    src = os.path.join(mp3_folder, file)
    dst = os.path.join(mp3_folder, file.split('_', 1)[-1])
    shutil.move(src, dst)

# Get the new list of MP3 files
mp3_files = [f for f in os.listdir(mp3_folder) if f.lower().endswith('.mp3')]

# Shuffle the MP3 files
random.shuffle(mp3_files)

# Create a temporary folder to store the shuffled files
# temp_folder = mp3_folder + "_temp"
# os.makedirs(temp_folder, exist_ok=True)

# Move the files into shuffled order
for index, file in enumerate(mp3_files):
    src = os.path.join(mp3_folder, file)
    dst = os.path.join(mp3_folder, f"{index+1}_{file}")
    shutil.move(src, dst)

# Optionally, you can move the shuffled files back to the original folder
# shutil.move(temp_folder, mp3_folder)
print(f"Shuffled {len(mp3_files)} MP3 files.")
