from Pillow import Image
import numpy as np

img_grey = Image.open('C:/Users/Vincent/Desktop/VR_Experiment/traceMe.png').convert('L')
print(img_grey.size)
# (300, 241)

# Taken from: https://stackoverflow.com/a/60783743/11089932
xy_coords = np.flip(np.column_stack(np.where(np.array(img_grey) >= 0)), axis=1)

# Add pixel numbers in front
pixel_numbers = np.expand_dims(np.arange(1, xy_coords.shape[0] + 1), axis=1)
value = np.hstack([pixel_numbers, xy_coords])
print(value)
# [[    1     0     0]
#  [    2     1     0]
#  [    3     2     0]
#  ...
#  [72298   297   240]
#  [72299   298   240]
#  [72300   299   240]]

# Properly save as CSV
np.savetxt("outputdata.csv", value, delimiter='\t', fmt='%4d')