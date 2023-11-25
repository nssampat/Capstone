# The purpose of this is to split the real slide data into training and validation. 
# We will select 925 images for training and 75 images for validation.
# We then need to write the names and annotations into separate train and val label files. 
import numpy as np
import cv2

'''lines = None
with open('real_labels_clean.txt', 'r') as rlc:
    lines = rlc.readlines()


# Go through each line.
num_lines = len(lines)
annotations = []

for idx in range(num_lines):
    line = lines[idx]

    if line[0] == '#':
        # Get all of the subsequent lines. 
        # We need to collect all of the corresponding annotations and parse them.
        annotations_str = [line]

        for inc in range(1, num_lines - idx):
            next_line = lines[idx + inc]

            if next_line[0] != "#":
                annotations_str.append(next_line)
            else:
                break

        annotations.append(annotations_str)


num_imgs = len(annotations)
inds = np.arange(num_imgs)
np.random.shuffle(inds)

# Now, use inds to rearrange the annotations array.
shuffled_anns = []
for ind in inds:
    shuffled_anns.append(annotations[ind])

# Let's take the first 925 to be the training set, and the next 75 to be the validation set. 
# We will simply append to a copy of the generated graph data labels.


with open('train_label.txt', 'a') as tl:
    train = shuffled_anns[:925]
    flattened_train = []
    for ann in train:
        for elem in ann:
            flattened_train.append(elem)

    tl.writelines(flattened_train)


with open('val_label.txt', 'a') as vl:
    val = shuffled_anns[925:]
    flattened_val = []
    for ann in val:
        for elem in ann:
            flattened_val.append(elem)

    vl.writelines(flattened_val)'''

lines = None
with open('../val_label.txt', 'r') as vl:
    lines = vl.readlines()

for line in lines:
    if line[0] == "#":
        filename = line.split(" ")[-1].strip()
        # Copy this image name into a new folder called val_images.
        val_img = cv2.imread(f"../realSlides/{filename}")
        cv2.imwrite(f"../val_images/{filename}", val_img)
         


                
                