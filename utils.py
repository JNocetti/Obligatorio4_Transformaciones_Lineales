import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
from PIL import Image
from skimage import io
from skimage import transform as tf
from skimage.color import rgb2gray

def show_image(image, tittle):
    plt.imshow(image,"gray")
    plt.title(tittle)
    plt.show()


def svd(image):
    imageToArray = np.array(image)
    U, S, V = np.linalg.svd(imageToArray, full_matrices=False)
    return U, S, V


def compress_image(image, k):
    image = rgb2gray(image)
    imageToArray = np.array(image)
    U, S, V = np.linalg.svd(imageToArray, full_matrices=False)
    result = np.dot(U[:, :k], np.dot(np.diag(S[:k]), V[:k, :]))
    return result


def rotate_image(image, angle):
    image = np.array(image)
    rotation_rad = angle * np.pi / 180.0

    height, width, channels = image.shape

    max_len = int(math.sqrt(height*height + width*width))
    rotated_image = np.zeros((max_len, max_len, channels))

    rotated_height, rotated_width, _ = rotated_image.shape
    mid_row = int( (rotated_height+1)/2 )
    mid_col = int( (rotated_width+1)/2 )
    for r in range(rotated_height):
        for c in range(rotated_width):
            y = (r-mid_col)*math.cos(rotation_rad) + (c-mid_row)*math.sin(rotation_rad)
            x = -(r-mid_col)*math.sin(rotation_rad) + (c-mid_row)*math.cos(rotation_rad)

            y += mid_col
            x += mid_row

            x = round(x)
            y = round(y)


            if (x >= 0 and y >= 0 and x < width and y < height):
                rotated_image[r][c][:] = image[y][x][:]


    result = Image.fromarray(rotated_image.astype("uint8"))
    return result


def scaling(image, k):
    result = image.resize(
        (int(image.width * k), int(image.height * k)))
    return result


def shearing(image, shearInput):
    image = np.array(image)
    afine_tf = tf.AffineTransform(shear=shearInput)
    result = tf.warp(image, inverse_map=afine_tf)
    return result



