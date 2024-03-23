
#!/bin/bash

# Specify the path to the parent folder
parent_folder="/path/to/folder"

# Move all image files from subfolders to the parent folder
find "$parent_folder" -mindepth 2 -type f \( -iname \*.png -o -iname \*.jpg -o -iname \*.jpeg -o -iname \*.gif -o -iname \*.bmp \) -exec mv -t "$parent_folder" {} +

