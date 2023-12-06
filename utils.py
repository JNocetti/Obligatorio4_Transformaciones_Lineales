import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
from PIL import Image


def show_image(image):
    plt.imshow(image)
    plt.show()


def svd(image):
    imageToArray = np.array(image)
    U, S, V = np.linalg.svd(imageToArray, full_matrices=False)
    return U, S, V


def compress_image(U, S, V, k):
    compressed_image = np.dot(U[:, :k], np.dot(np.diag(S[:k]), V[:k, :]))
    return compressed_image


def rotate_image(image, angle):
    imageToArray = np.array(image)
    rotatedImage = rotate(imageToArray, angle, reshape=False)
    return rotatedImage


def scaling(image, scale):
    scaled_image = image.resize(
        (int(image.width * scale), int(image.height * scale)))
    return scaled_image


