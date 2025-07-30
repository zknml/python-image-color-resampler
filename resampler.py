from PIL import Image
import numpy as np
from scipy import spatial as sp
import time

colorsource_filename = input("Input filename of color source image, including file extension: ")
target_filename = input("Input filename of target image, including file extension: ")
output_filename = input("Input desired filename and file extension for output image: ")

t = time.time()

colorsource_image = np.asarray(Image.open(colorsource_filename))
colorsource_image_size = len(colorsource_image)*len(colorsource_image[0])
colorsource_image_flatten = np.reshape(colorsource_image, (colorsource_image_size, 3))
colorsource_image_flatten = np.unique(colorsource_image_flatten, axis=0)
colorsource_image_data = sp.KDTree(colorsource_image_flatten)

target_image = np.array(Image.open(target_filename))
colormap = np.full((256,256,256,3), -1)

for i in range(len(target_image)):
    for j in range(len(target_image[0])):
        targetpx = target_image[i][j]
        if colormap[targetpx[0]][targetpx[1]][targetpx[2]][0] == -1:
            loc = colorsource_image_data.query(target_image[i][j])[1]
            colormap[targetpx[0]][targetpx[1]][targetpx[2]] = colorsource_image_flatten[loc]
        target_image[i][j] = colormap[targetpx[0]][targetpx[1]][targetpx[2]]

output_image = Image.fromarray(target_image)
output_image.save(output_filename)

t = time.time() - t

print('\n>> File saved at ' + output_filename)
print('>> Runtime: %f seconds' %t)
input("Press any key to close")
