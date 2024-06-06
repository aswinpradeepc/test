import os
from rawpy import imread
from PIL import Image

# Set the input and output directories
input_dir = "/home/aswin/Desktop/raw"
output_dir = "/home/aswin/Desktop/raw/out"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".dng"):
        # Open the DNG file using rawpy
        input_path = os.path.join(input_dir, filename)
        raw = imread(input_path)
        
        # Get the base filename without extension
        base_filename, _ = os.path.splitext(filename)
        
        # Construct the output JPG filename
        output_filename = f"{base_filename}.jpg"
        output_path = os.path.join(output_dir, output_filename)
        
        # Convert the raw data to RGB and save as JPG
        rgb = raw.postprocess()
        img = Image.fromarray(rgb)
        img.save(output_path, "JPEG")
        print(f"Converted {filename} to {output_filename}")
    else:
        print(f"Skipping {filename} (not a DNG file)")
