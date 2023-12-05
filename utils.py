import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
from PIL import Image

def show_image(image):
    plt.imshow(image)
    plt.show()

def rotate_image(image, angle):
    imageToArray = np.array(image)
    rotatedImage = rotate(imageToArray, angle, reshape=False)
    return rotatedImage


def scaling(image, scale):
    scaled_image = image.resize((int(image.width * scale), int(image.height * scale)))
    return scaled_image



