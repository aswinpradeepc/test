import os
import random

# Define the source directory containing subfolders
source_dir = "/home/aswin/Downloads/plant_dataset/dataset/valid"

# Define the number of images to keep in each subfolder
num_images_to_keep = 350

# Function to delete excess images from a folder
def delete_excess_images(folder_path, num_images_to_keep):
    # Get list of all images in the folder
    images = os.listdir(folder_path)
    # Check if the number of images exceeds the limit
    if len(images) > num_images_to_keep:
        # Calculate the number of excess images
        num_excess_images = len(images) - num_images_to_keep
        # Randomly select excess images to delete
        images_to_delete = random.sample(images, num_excess_images)
        # Delete excess images
        for image in images_to_delete:
            os.remove(os.path.join(folder_path, image))

# Iterate through each subfolder
for folder_name in os.listdir(source_dir):
    # Get the full path of the subfolder
    subfolder_path = os.path.join(source_dir, folder_name)
    # Check if it's a directory
    if os.path.isdir(subfolder_path):
        # Call the function to delete excess images from this subfolder
        delete_excess_images(subfolder_path, num_images_to_keep)
