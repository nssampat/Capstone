# This is to convert the current annotations into YOLOv5 format.
# We need to first go through train_label.txt and do 2 things:
# 1. Once we have an image name and its corresponding annotations:
    # a. Copy the image to yolov5_gd/data/images/training.
    # b. Create a txt file with the image name in yolov5_gd/data/labels/training.
        # i. Each object annotation should be a new line in the format class_id center_x center_y width height
        # ii. Note that these values should be normalized by width and height of the image. 

import cv2
import numpy as np
import tqdm

# ----------------------------------- BEGIN CLEANING TRAIN DATA -------------------------------------------------
'''
train_lines = None
with open('../train_label.txt', 'r') as tl:
    train_lines = tl.readlines()

num_lines = len(train_lines)
for idx in tqdm.trange(num_lines):

    line = train_lines[idx]
    if line[0] == "#":
        img_name = line.strip().split(" ")[-1]

        # Figure out if it is a real image or generated image.
        full_path = None
        if img_name[0] == 'g':
            full_path = f"../realSlides/{img_name}"
        else:
            full_path = f"../generatedSlidesLabelled/{img_name}"


        # We need to collect all of the corresponding annotations and parse them.
        annotations_str = []

        for inc in range(1, num_lines - idx):
            next_line = train_lines[idx + inc]

            if next_line[0] != "#":
                annotations_str.append(next_line)
            else:
                break
        
        # Now, we have all of the corresponding annotations in a list.
        
        # Let's first copy over the image, then modify the annotations and write them into the proper file.
        img = cv2.imread(full_path)
        img_height, img_width, _ = img.shape

        cv2.imwrite(f'../../../../Downloads/yolov5_gd/data/images/training/{img_name}', img)

        img_name_no_ext = img_name.split(".")[0]
        ann_path = f'../../../../Downloads/yolov5_gd/data/labels/training/{img_name_no_ext}.txt'

        new_lines = []
        for i in range(len(annotations_str)):
            annotation_i = annotations_str[i].split(" ")
            annotation_i = [int(val) for val in annotation_i]
            x1, y1, w, h, l = annotation_i

            # Right now the annotations are in the format: x1 y1 w h label
            # We want them in the format: label center_x center_y w h
            x_center = x1 + (float(w) / 2)
            y_center = y1 + (float(h) / 2)

            # Normalize all values by the image's width and height.
            x_center /= img_width
            y_center /= img_height
            w /= img_width
            h /= img_height

            new_line = f"{l} {x_center} {y_center} {w} {h}\n"
            new_lines.append(new_line)


        with open(ann_path, 'w') as af:
            
            # Finally, write the lines to the file. 
            af.writelines(new_lines)


'''
# ----------------------------------- END CLEANING TRAIN DATA -------------------------------------------------







# ----------------------------------- BEGIN CLEANING VAL DATA -------------------------------------------------

val_lines = None
with open('../val_label.txt', 'r') as vl:
    val_lines = vl.readlines()

num_lines = len(val_lines)
for idx in tqdm.trange(num_lines):

    line = val_lines[idx]
    if line[0] == "#":
        img_name = line.strip().split(" ")[-1]

        # Figure out if it is a real image or generated image.
        full_path = None
        if img_name[0] == 'g':
            full_path = f"../realSlides/{img_name}"
        else:
            full_path = f"../generatedSlidesLabelled/{img_name}"


        # We need to collect all of the corresponding annotations and parse them.
        annotations_str = []

        for inc in range(1, num_lines - idx):
            next_line = val_lines[idx + inc]

            if next_line[0] != "#":
                annotations_str.append(next_line)
            else:
                break
        
        # Now, we have all of the corresponding annotations in a list.
        
        # Let's first copy over the image, then modify the annotations and write them into the proper file.
        img = cv2.imread(full_path)
        img_height, img_width, _ = img.shape

        cv2.imwrite(f'../../../../Downloads/yolov5_gd/data/images/validation/{img_name}', img)

        img_name_no_ext = img_name.split(".")[0]
        ann_path = f'../../../../Downloads/yolov5_gd/data/labels/validation/{img_name_no_ext}.txt'

        new_lines = []
        for i in range(len(annotations_str)):
            annotation_i = annotations_str[i].split(" ")
            annotation_i = [int(val) for val in annotation_i]
            x1, y1, w, h, l = annotation_i

            # Right now the annotations are in the format: x1 y1 w h label
            # We want them in the format: label center_x center_y w h
            x_center = x1 + (float(w) / 2)
            y_center = y1 + (float(h) / 2)

            # Normalize all values by the image's width and height.
            x_center /= img_width
            y_center /= img_height
            w /= img_width
            h /= img_height

            new_line = f"{l} {x_center} {y_center} {w} {h}\n"
            new_lines.append(new_line)


        with open(ann_path, 'w') as af:
            
            # Finally, write the lines to the file. 
            af.writelines(new_lines)


# ----------------------------------- END CLEANING VAL DATA -------------------------------------------------

'''Let's just make sure that the normalization and everything happened correctly. Delete this later.'''
'''test_lines = None
with open('../../../../Downloads/yolov5_gd/data/labels/training/graph_slide835.txt', 'r') as test:
    test_lines = test.readlines()

img = cv2.imread('../realSlides/graph_slide835.png')
height, width, _ = img.shape
for line in test_lines:
    vals = line.strip().split(" ")
    label, x_c, y_c, w, h = [float(val) for val in vals]
    print(f"Label is {label}")
    
    # Unnormalize it.
    x1 = int((x_c - (w / 2)) * width)
    y1 = int((y_c - (h / 2)) * height)

    w = int(w * width)
    h = int(h * height)

    print(x1, y1, w, h)
    
    img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 2)


cv2.imwrite('../../../../Downloads/graph_slide835_vis.png', img)'''