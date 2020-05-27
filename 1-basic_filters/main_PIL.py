from img_preprocess import grayscale_avg
from sobel_filter import sobel_filter_horizontal
from sobel_filter import  sobel_filter_vertical
from sobel_filter import sobel_filter
from gaussian_filter import gaussian_filter
from laplacian_of_gaussian_filter import log_filter
from PIL import Image
import numpy as np

# read the RGB images
img = Image.open('data/checkerbox.jpg') # converts the input image to np.array of 3 dimensions (height, width, 3) where 3 stands for RGB channels
Image._showxv(img,title="original")
img_gray = grayscale_avg(np.asarray(img)) # converts the input image to gayscale using average method
# Image._show(Image.fromarray(img_gray),title="grayscaled")
# Image._show(Image.fromarray(gaussian_filter(img_gray)),title="gaussian filter")
# Image._show(Image.fromarray(sobel_filter_vertical(img_gray)),title="sobel vertical filter")
# Image._show(Image.fromarray(sobel_filter_horizontal(img_gray)),title="sobel horizontal filter")
Image._show(Image.fromarray(sobel_filter(img_gray)),title="sobel filter")
Image._show(Image.fromarray(log_filter(img_gray)),title="log filter")

