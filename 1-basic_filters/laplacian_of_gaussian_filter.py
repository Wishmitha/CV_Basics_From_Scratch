import numpy as np

#applies 3x3 log filter for the input image
def log_filter(img):
    '''
    Detects vertical edges of an image
    :param img: input image
    :return: edge detected image
    '''
    height = img.shape[0]
    width = img.shape[1]

    gaussian_filter = np.array([[1, 2, 1]])
    laplace_filter = np.array([[1,-2,1]])

    log_filter_horizontal = np.transpose(gaussian_filter) * laplace_filter # 3x3 horizontal filter
    log_filter_vertical = np.transpose(laplace_filter) * gaussian_filter # 3x3 vertical filter

    log_res = np.empty((height, width), dtype=np.float64)

    # convolution operation
    for y in range(height):
        for x in range(width):
            if (x + 3 < width and y + 3 < height):
                log_res_horizontal = np.average(img[y:y + 3, x:x + 3] * log_filter_horizontal)
                log_res_vertical = np.average(img[y:y + 3, x:x + 3] * log_filter_vertical)
                log_res[y,x] = np.sqrt(np.power(log_res_horizontal,2)+np.power(log_res_vertical,2))

    return log_res