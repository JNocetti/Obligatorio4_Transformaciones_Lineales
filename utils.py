import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
from PIL import Image
from skimage import io
from skimage import transform as tf
from skimage.color import rgb2gray

def show_image(image):
    plt.imshow(image,"gray")
    plt.show()


def svd(image):
    imageToArray = np.array(image)
    U, S, V = np.linalg.svd(imageToArray, full_matrices=False)
    return U, S, V


def compress_image(image, k):
    image = rgb2gray(image)
    imageToArray = np.array(image)
    U, S, V = np.linalg.svd(imageToArray, full_matrices=False)
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


def shearing(image, shearInput):
    image = np.array(image)
    afine_tf = tf.AffineTransform(shear=shearInput)
    modified = tf.warp(image, inverse_map=afine_tf)
    return modified



