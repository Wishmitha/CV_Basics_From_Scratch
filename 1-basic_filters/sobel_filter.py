import numpy as np

#applies 3x3 horizontal sobel filter for the input image
def sobel_filter_horizontal(img):
    '''
    Detects vertical edges of an image
    :param img: input image
    :return: edge detected image
    '''
    height = img.shape[0]
    width = img.shape[1]

    gaussian_filter = np.array([[1, 2, 1]])
    deravative_filter = np.array([[1, 0, -1]])

    sobel_filter = np.transpose(gaussian_filter) * deravative_filter

    sobel_res = np.empty((height, width),dtype=np.float64)

    # convolution operation
    for y in range(height):
        for x in range(width):
            if (x + 3 < width and y + 3 < height):
                sobel_res[y, x] = np.average(img[y:y + 3, x:x + 3] * sobel_filter)

    return sobel_res


# applies 3x3 vertical sobel filter for the input image
def sobel_filter_vertical(img):
    '''
    Detects horizontal edges of an image
    :param img:input image
    :return: edge detected image
    '''
    height = img.shape[0]
    width = img.shape[1]

    gaussian_filter = np.array([[1, 2, 1]])
    deravative_filter = np.array([[1, 0, -1]])

    sobel_filter = np.transpose(deravative_filter) * gaussian_filter

    sobel_res = np.empty((height, width),dtype=np.float64)

    # convolution operation
    for y in range(height):
        for x in range(width):
            if (x + 3 < width and y + 3 < height):
                sobel_res[y, x] = np.average(img[y:y + 3, x:x + 3] * sobel_filter)

    return sobel_res

# computes edges using vertical and horizontal sobel filters
def sobel_filter(img):
    '''
    Detects edges of an image
    :param img: input image
    :return: edge detected image
    '''
    height = img.shape[0]
    width = img.shape[1]

    sobel_res = np.empty((height, width),dtype=np.float64)

    sobel_y = sobel_filter_horizontal(img)
    sobel_x = sobel_filter_vertical(img)

    # convolution operation
    for y in range(height):
        for x in range(width):
                sobel_res[y,x] = np.sqrt(np.power(sobel_y[y,x],2)+np.power(sobel_x[y,x],2))

    return sobel_res