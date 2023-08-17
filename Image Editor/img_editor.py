from PIL import Image, ImageEnhance
import os

#Specify source and dest directory
source_directory = './image'
destination_directory = './edited-img'

#Ensure the destination directory exists

os.makedirs(destination_directory, exist_ok=True)

#all image files in the src dir
image_files = [f for f in os.listdir(source_directory) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

for image_file in image_files:
    source_path = os.path.join(source_directory, image_file)
    destination_path = os.path.join(destination_directory, image_file)

    image = Image.open(source_path)
    enhancer = ImageEnhance.Color(image)
    red_filtered_image = enhancer.enhance(2.0)
    red_filtered_image.save(destination_path)

    print(f"Processed '{image_file}'")

    print("Image editing and saving complete.")