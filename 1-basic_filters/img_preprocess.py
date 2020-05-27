import numpy as np



# convert RGB to grayscale
# 1. average method : get the mean of 3 channels

def grayscale_avg(img):
    '''
    :param img: input image
    :return: grayscaled image
    '''

    height = img.shape[0]
    width = img.shape[1]

    grayscale_avg = np.empty((height,width),dtype=np.float64) # empty array to store grayscaled pixels

    for y in range(height): # treversing through each row
        for x in range(width): # traversing through each pixel in the row
            pixel = np.average(img[y,x]) # taking the average value of each channel value gray=(R+G+B)/3
            grayscale_avg[y,x] = pixel # put averaged grayscaled value to the initiated np array

    return grayscale_avg;

# 1. weighted method : get the weighted averages of 3 channels

def grayscale_wighted(img, weight_R, weight_G, weight_B):
    '''
    :param img: input image
    :param weight_R: weight for red channel
    :param weight_G: weight for green channel
    :param wight_B: weight for blue channel
    :return: grayscaled image
    '''

    height = img.shape[0]
    width = img.shape[1]

    grayscale_luminosity = np.empty((height,width),dtype=np.float64) # empty array to store greyscaled pixels

    red_weight = weight_R/(weight_R+weight_G+weight_B)
    green_weight = weight_G / (weight_R + weight_G + weight_B)
    blue_weight = weight_B / (weight_R + weight_G + weight_B)

    for y in range(height): # treversing through each row
        for x in range(width): # traversing through each pixel in the row
            pixel = red_weight*img[y,x][0] + green_weight*img[y,x][1] + blue_weight*img[y,x][2]  # taking the weighted average value of each channel
            grayscale_luminosity[y,x] = pixel # put averaged grayscaled value to the initiated np array

    return grayscale_luminosity

