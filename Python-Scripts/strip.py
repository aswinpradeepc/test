from PIL import Image
import os

def crop_image_vertically(image_path, crop_height, output_folder):
    # Open the image
    with Image.open(image_path) as img:
        width, height = img.size
        
        # Calculate the number of crops
        num_crops = height // crop_height
        
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Crop and save each section
        for i in range(num_crops):
            top = i * crop_height
            bottom = (i + 1) * crop_height
            cropped_img = img.crop((0, top, width, bottom))
            cropped_img.save(os.path.join(output_folder, f"cropped_{i}.png"))

# Set input image path
input_image_path = "normallist_0.jpg"
# Set the height for each crop
crop_height = 70

# Set output folder
output_folder = "cropped_images_normal_0"

# Perform cropping
crop_image_vertically(input_image_path, crop_height, output_folder)

print("Cropping complete.")
