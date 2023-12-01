import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate


def show_image(image):
    plt.imshow(image)
    plt.show()

def rotate_image(image, angle):
    imageToArray = np.array(image)
    rotatedImage = rotate(imageToArray, angle, reshape=False)
    return rotatedImage



