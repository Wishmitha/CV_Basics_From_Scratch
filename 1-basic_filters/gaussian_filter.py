import numpy as np

def gaussian_filter(img):
    '''
    Detects vertical edges of an image
    :param img: input image
    :return: edge detected image
    '''
    height = img.shape[0]
    width = img.shape[1]

    gaussian_filter_1x3 = (1/4)*np.array([[1, 2, 1]])

    gaussian_filter_3x3 = np.transpose(gaussian_filter_1x3) * gaussian_filter_1x3

    gaussian_res = np.empty((height, width),dtype=np.float64)

    #convolution operation
    for y in range(height):
        for x in range(width):
            if (x + 3 < width and y + 3 < height):
                gaussian_res[y, x] = np.sum(img[y:y + 3, x:x + 3] * gaussian_filter_3x3)

    return gaussian_res