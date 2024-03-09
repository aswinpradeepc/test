#!/bin/bash

# YOLOv9 configuration
weights="/home/aswin/PycharmProjects/yolov9/yolov9-c.pt"
device="cpu"
save_conf="--save-conf"

# List of folder names
folder_names=("16_9" "farhan_1" "farhan_2" "s23")

# Loop through each folder name and run YOLOv9 detection
for folder_name in "${folder_names[@]}"; do
    image_path="/home/aswin/PycharmProjects/yolov9/exp_2_lens/$folder_name"
    yolov9_script="/home/aswin/PycharmProjects/yolov9/detect.py"  # Replace with the actual path

    # Loop through each image in the current path
    for image in "$image_path"/*; do
        python3 "$yolov9_script" --weights "$weights" --source "$image" --device "$device" "$save_conf" --save-txt
    done

    echo "Folder $folder_name done" >> "/home/aswin/PycharmProjects/yolov9/result_exp2_lens.csv"
done
