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


def scaling(image, k):
    imageToArray = np.array(image)
    scaled_image = imageToArray * k
    # Normaliza los valores para que estén en el rango válido (0 a 255)
    scaled_image = np.clip(scaled_image, 0, 255).astype(np.uint8)
    return scaled_image
