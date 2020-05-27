import matplotlib.pyplot as plt
from img_preprocess import grayscale_avg
import numpy as np

def gray_channel_scatter_visualizer(img):

    img = grayscale_avg(img)

    fig = plt.figure()

    height = img.shape[0]
    width = img.shape[1]

    ax = fig.add_subplot(111, projection='3d')

    for y in range(height):
        for x in range(width):
                ax.scatter(y,x,img[y,x],c="gray",s=0.1)
    plt.show()

def gray_channel_surface_visualizer(img):
    img_gray = grayscale_avg(img)
    xx, yy = np.mgrid[0:img_gray.shape[0], 0:img_gray.shape[1]]
    fig = plt.figure(figsize=(15,15))
    ax = fig.gca(projection='3d')
    ax.plot_surface(xx, yy, img_gray ,rstride=1, cstride=1, cmap=plt.cm.gray,linewidth=2)
    ax.view_init(80, 30)
    plt.show()