#!/bin/bash

# Path to the directory containing all the images
image_path="/home/aswin/PycharmProjects/yolov9/akhil/5"

# Path to the YOLOv9 script
yolov9_script="/home/aswin/PycharmProjects/yolov9/detect.py"  # Replace with the actual path

# YOLOv9 configuration
weights="/home/aswin/PycharmProjects/yolov9/yolov9-c.pt"
device="cpu"
save_conf="--save-conf"

# Loop through each image and run the YOLOv9 detection
for image in "$image_path"/*; do
    python3 "$yolov9_script" --weights "$weights" --source "$image" --device "$device" "$save_conf" --save-txt
done
: <<'COMMENT'
echo "Folder 1 done" >> "/home/aswin/PycharmProjects/yolov9/result_varsha.csv"

image_path="/home/aswin/PycharmProjects/yolov9/varsha/2"
for image in "$image_path"/*; do
    python3 "$yolov9_script" --weights "$weights" --source "$image" --device "$device" "$save_conf" --save-txt
done

echo "Folder 2 done" >> "/home/aswin/PycharmProjects/yolov9/result_varsha.csv"

image_path="/home/aswin/PycharmProjects/yolov9/varsha/3"
for image in "$image_path"/*; do
    python3 "$yolov9_script" --weights "$weights" --source "$image" --device "$device" "$save_conf" --save-txt
done

echo "Folder 3 done" >> "/home/aswin/PycharmProjects/yolov9/result_varsha.csv"

image_path="/home/aswin/PycharmProjects/yolov9/varsha/4"
for image in "$image_path"/*; do
    python3 "$yolov9_script" --weights "$weights" --source "$image" --device "$device" "$save_conf" --save-txt
done

echo "Folder 4 done" >> "/home/aswin/PycharmProjects/yolov9/result_varsha.csv"

image_path="/home/aswin/PycharmProjects/yolov9/varsha/5"
for image in "$image_path"/*; do
    python3 "$yolov9_script" --weights "$weights" --source "$image" --device "$device" "$save_conf" --save-txt
done

echo "Folder 5 done" >> "/home/aswin/PycharmProjects/yolov9/result_varsha.csv"
