#!/bin/python
from PIL import Image
import os


file_path = input("Enter path of folder which contains images (absolute or relative): ")
new_file_path = os.path.join(file_path, 'resized/')
print(new_file_path)
image_list = []

if not os.path.exists(new_file_path):
    os.makedirs(new_file_path)

for image in os.listdir(file_path):
    if image.endswith(".jpg") or image.endswith(".jpeg"):
        image_list.append(image)

for image_path in image_list:
    image = Image.open(os.path.join(file_path, image_path))
    width, height = image.size
    if(width>400):
        # w -> 400
        # h -> x
        height = int(height/width * 400)
        width = 400
        image = image.resize((width, height))
    if(height>400):
        # h -> 400
        # w -> x
        width = int(width/height * 400)
        height = 400
        image = image.resize((width, height))
    
    new_image_path = os.path.join(new_file_path, image_path)


    low_quality=0
    high_quality = 100
    iter_count = 0
    last_working_quality = 0
    while low_quality<=high_quality and iter_count<=10:
        mid_quality = int((low_quality + high_quality) / 2)
        image.save(new_image_path, quality=mid_quality)
        file_size = os.path.getsize(new_image_path)

        if file_size < 64000:
            low_quality = mid_quality+1
            last_working_quality = mid_quality
        else:
            high_quality = mid_quality-1
    image.save(new_image_path, quality=last_working_quality)
