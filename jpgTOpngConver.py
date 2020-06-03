import sys
import os
from PIL import Image

# grab first and second argument

image_foldar = sys.argv[1]
output_folder = sys.argv[2]

# check if output_folder exists

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

# loop through the images

for fileName in os.listdir(image_foldar):
	img = Image.open(f"{image_foldar}{fileName}")
	clean_name = os.path.splitext(fileName)[0]
	img.save(f"{output_folder}{clean_name}.png","png")

print("----------------------------------------------------------------------------------")
print(f"Your images are converted into PNG format and saved in {output_folder}")
print("------------------------Thanks for using the Tool---------------------------------")