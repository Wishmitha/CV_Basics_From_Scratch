import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from img_preprocess import grayscale_avg
from sobel_filter import sobel_filter_horizontal
from sobel_filter import  sobel_filter_vertical
from sobel_filter import sobel_filter
from gaussian_filter import gaussian_filter
from laplacian_of_gaussian_filter import log_filter

# read the RGB images
img = mpimg.imread('data/checkerbox.jpg') # converts the input image to np.array of 3 dimensions (height, width, 3) where 3 stands for RGB channels

plt.figure()
imgplot0 = plt.imshow(img) #display original image

img_gray = grayscale_avg(img) # converts the input image to gayscale using average method

plt.figure()
imgplot1 = plt.imshow(img_gray, cmap="gray") #display grayscaled image

plt.figure()
imgplot2 = plt.imshow(gaussian_filter(img_gray), cmap="gray") #apply gaussian filter to smooth the image

plt.figure()
imgplot3 = plt.imshow(sobel_filter_vertical(img_gray), cmap="gray") #apply vertical sobel filter to detect horizontal edges

plt.figure()
imgplot4 = plt.imshow(sobel_filter_horizontal(img_gray), cmap="gray") #apply horizontal sobel filter to detect verticle edges

plt.figure()
imgplot5 = plt.imshow(sobel_filter(img_gray), cmap="gray") #detect edges in the image using both verticle and horizontal sobel filters

plt.figure()
imgplot6 = plt.imshow(log_filter(img_gray), cmap="gray") #detect edges in the image using both verticle and horizontal sobel filters

plt.show()