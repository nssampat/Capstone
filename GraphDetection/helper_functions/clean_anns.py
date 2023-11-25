import cv2
import tqdm

# Cleaning the real annotations by removing text, converting to ints, and adding class label.
'''lines = None
with open('real_labels_raw.txt', 'r') as rlr:
    lines = rlr.readlines()


string_to_class = {'background': 0, 'line': 1, 'scatter': 2, 'bar': 3, 'pie': 4}

clean_lines = []

for line in lines:
    if len(line) < 3:
        # This is just the value which tells us how many objects there are in that image.
        continue


    if line[:2] == 'no':
        line_clean = "# " + line.split('/')[-1]
        clean_lines.append(line_clean)
        continue
    else:
        # Change the line to be just the 4 numbers and then the class identifier: line, scatter, bar, pie.
        exploded = line.split(" ")
        bbox_vals = [int(float(val)) for val in exploded[:4]]
        last_val = exploded[-1].strip()
        last_val = string_to_class[last_val]
        
        all_vals = bbox_vals + [last_val]
        line_elems = [str(val) for val in all_vals]
        line_clean = " ".join(line_elems) + "\n"
        clean_lines.append(line_clean)

with open('real_labels_clean.txt', 'w') as rlc:
    # Write the clean lines to the new file.
    rlc.writelines(clean_lines)'''


# Cleaning the generated labels by figuring out which label each randomly generated graph is. 
# This is not working, so we need to regenerate whole dataset.

'''# Need to iterate through the entire generated_labels_raw.txt file.
lines = None
with open('generated_labels_raw.txt', 'r') as glr:
    lines = glr.readlines()

clean_lines = []
# Each randomly generated slide has a maximum of 3 graphs - plot them in red, green, then blue.
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
string_to_class = {'l': 1, 's': 2, 'b': 3, 'p': 4}


latest_img_name = None
counter = 0

for i in tqdm.trange(len(lines)):
    line = lines[i]
    
    if line[0] == '#':
        img_name = line.split(" ")[-1].strip()
        latest_img_name = f'generatedSlides/{img_name}'

        clean_lines.append(line)
        #counter = 0

    else:
        exploded = line.split(" ")
        exploded = [int(val) for val in exploded]
        _, x1, y1, w, h = exploded

        # Open up the image. 
        latest_img = cv2.imread(latest_img_name)
        latest_img = cv2.rectangle(latest_img, (x1, y1), (x1 + w, y1 + h), colors[counter], 2)
       
        cv2.imshow('image', latest_img)
        cv2.waitKey()
        #counter += 1

        # Get the input from the user: is it a line, scatter, bar, or pie? (Use first letter)
        graph_type = input('Type?\n')
        graph_type = string_to_class[graph_type]

        clean_line = f"{x1} {y1} {w} {h} {graph_type}\n"
        clean_lines.append(clean_line)


# At the end, write all of the clean lines to the new file.
with open('generated_labels_clean.txt', 'w') as glc:
    # Write the clean lines to the new file.
    glc.writelines(clean_lines)'''

# Transfer all labels from the individual files into the train_label.txt file.
# Completed: 0 to 1, 1 to 2, 2 to 3, 3 to 4, 4 to 5, 5 to 6, 6 to 9, 
'''lines = None
with open('../generatedLabelsFiles/generated_labels_new_9to10.txt', 'r') as gls:
    # Write the clean lines to the new file.
    lines = gls.readlines()

with open('train_label.txt', 'a') as tl:
    # Write the clean lines to the new file.
    tl.writelines(lines)'''











