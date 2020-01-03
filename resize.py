#!/bin/python
from PIL import Image
import os

max_file_size = 64 * 1024
max_dimen = 400

file_path = input("Enter path of folder which contains images (absolute or relative): ")
new_file_path = os.path.join(file_path, 'resized/')
image_list = []

if not os.path.exists(new_file_path):
    os.makedirs(new_file_path)

for image in os.listdir(file_path):
    if image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".png"):
        image_list.append(image)

for image_path in image_list:
    image = Image.open(os.path.join(file_path, image_path))
    width, height = image.size
    if(width>max_dimen):
        height = int(height/width * max_dimen)
        width = max_dimen
        image = image.resize((width, height))
    if(height>max_dimen):
        width = int(width/height * max_dimen)
        height = max_dimen
        image = image.resize((width, height))
    
    new_image_path = os.path.join(new_file_path, image_path)

    if image_path.endswith(".png"):
        image.save(new_image_path)
    else:
        low_quality=0
        high_quality = 100
        iter_count = 0
        last_working_quality = 0
        while low_quality<=high_quality and iter_count<=10:
            mid_quality = int((low_quality + high_quality) / 2)
            image.save(new_image_path, quality=mid_quality)
            file_size = os.path.getsize(new_image_path)

            if file_size < max_file_size:
                low_quality = mid_quality+1
                last_working_quality = mid_quality
            else:
                high_quality = mid_quality-1
        image.save(new_image_path, quality=last_working_quality)
