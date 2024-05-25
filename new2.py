import numpy as np

image = np.array(Image.open('traceMe.png'))
pixel_intensity = image[1, 385]
print("Intensity of pixel at ({}, {}):".format(1, 385), pixel_intensity)
